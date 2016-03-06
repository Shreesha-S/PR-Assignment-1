import pandas as pd
import matplotlib.pyplot as plt
import scipy
from sklearn.svm import SVC
import numpy as np

data = pd.read_csv("pima-indians-diabetes.data")
dat = open("pima-indians-diabetes.data", "r")
dia = open("diabetic.csv", "w")
ndia = open("non-diabetic.csv", "w")

# Classify all diabetic records to diabetic.csv and all...
# ... non-diabetic records to non-diabetic.csv
for record in dat:
  if record[-2] == "0":
    ndia.write(record)
  else:
    dia.write(record)

# Close the .csv files.
dia.close()
ndia.close()

# Read the .csv files into DataFrames
dia_data = pd.read_csv("diabetic.data")
ndia_data = pd.read_csv("non-diabetic.data")

# Shuffle the data present in diabetic.data and non-diabetic.data 
dia_data = dia_data.iloc[np.random.permutation(len(dia_data))]
ndia_data = ndia_data.iloc[np.random.permutation(len(ndia_data))]

# Categorize first 100 records and training data and rest as test data excluding result.
d_train = dia_data.iloc[:100,:8]
d_test = dia_data.iloc[100:,:8]
n_train = ndia_data.iloc[:100,:8]
n_test = ndia_data.iloc[100:,:8]

# Take the (classification) result into a separate DataFrame.
d_train_class = dia_data.iloc[:100,8:]
d_test_class = dia_data.iloc[100:,8:]
n_train_class = ndia_data.iloc[:100,8:]
n_test_class = ndia_data.iloc[100:,8:]

# Concatenate diabetic.cs and non-diabetic.csv train and test data along with the results. 
train_frames = [d_train, n_train]
train_frame_class = [d_train_class, n_train_class]
test_frames = [d_test, n_test]
test_frame_class = [d_test_class, n_test_class]

train = pd.concat(train_frames)
train_class = pd.concat(train_frame_class)
test = pd.concat(test_frames)
test_class = pd.concat(test_frame_class)

# Change to 1D Array. 
train_class = train_class.as_matrix().ravel()

# Use SVM with linear kernel class.
classifier = SVC(kernel="linear")
# Train the data.
classifier.fit(train, train_class)
# Predict the test data.
class_ans = classifier.predict(test)
# The test data result to compare with.
act_ans = test_class.as_matrix().ravel()

# Report the Confusion matrix.
tp = list(class_ans[:168]).count(1) * 100.0 / 168.0
fn = list(class_ans[:168]).count(0) * 100.0 / 168.0
fp = list(class_ans[168:]).count(1) * 100.0 / 400.0
tn = list(class_ans[168:]).count(0) * 100.0 / 400.0
print "True Positive %s" % tp
print "False Negatives %s" % fn
print "False Positives %s" % fp
print "True Negatives %s" % tn


