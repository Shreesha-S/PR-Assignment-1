### Classification of input as diabetic or non-diabetic using SVM's

#Purpose 

To learn to 

 * solve a two-class classification problem
 * work with feature vectors with more than one or two entries (in this case there are eight) 
 * partition a data set to training and test sets  
 * prepare data for and train an off-the-shelf classifier (in this case, a support vector machine or SVM) 
 * create a confusion matrix (see below) to present the results
 * compute classification accuracy from the confusion matrix 
 * experiment with different types of cross validation techniques 
 * understand the effect of changing classifier parameters (in this case, kernals used with the SVM)

# Problem description
A population of women who were at least 21 years old, of Pima Indian heritage and living near Phoenix, Arizona, was tested for diabetes according to World Health Organization criteria. The data were collected by the US National Institute of Diabetes and Digestive and Kidney Diseases. Complete records are available for only 532 samples; the rest have some missing data (mostly, the data on serum insulin).

# Data
These data frames contains the following comma-separated columns:

Attribute 1 - Number of pregnancies
Attribute 2 - Plasma glucose concentration in an oral glucose tolerance test
Attribute 3 - Diastolic blood pressure (mm Hg)
Attribute 4 - Triceps skin fold thickness (mm)
Attribute 5 - 2 hr serum insulin (mu U/ml) 
Attribute 6 - Body mass index (weight in kg/(height in m)\^2)
Attribute 7 - Diabetes pedigree function
Attribute 8 - Age in years

The last column indicates Class 0 ('no diabetes') or Class 1 ('has diabetes') based on the WHO criteria. 

Given: Basic statistics of the data (next time, you should compute this/ whatever variation is necessary to get an insight to the data): 

#Attribute number: Mean: Standard Deviation:
1. 3.8 3.4
2. 120.9 32.0
3. 69.1 19.4
4. 20.5 16.0
5. 79.8 115.2
6. 32.0 7.9
7. 0.5 0.3
8. 33.2 11.8

# Classification using a Support Vector Machine (SVM) 

SVMLight is a classifier that is implemented in C by Thorsten Joachims. You can download this and use the commands to train and test the classifier, without having to implement one from scratch (go through the 'Getting Started' section on the web page to understand the format of the training and test files and function call for svm_learn and svm_classify commands). 

# Preparing the data for training and testing the classifier

1. Create a file with all samples for class 1 (has diabetes) and a separate file for class 0 (no diabetes).
2. Remove those data points that have missing attributes from these files (no entry in a certain column or a NA for 'not applicable' in a certain column).
3. Select 200 samples at random (include a 100 samples from the positive class and as many from the negative class) and create a TrainingSet.
4. Write the remaining samples (those not included in TrainingSet) in a TestingSet file (in this file, there may be more samples from one class compared to the other; it is all right)

# Classifier kernels 

Use the
1. Linear kernel
2. Polynomial kernel
to train and test your classifier.

# Evaluation of the classifier 

Prepare the following table (called a 'confusion matrix) from the output of the SVM for your test data in each of the two cases above (linear and polynomial kernels) -


                   Algorithm Classified as Class 1    |     Algorithm Classified as Class 0
------------------------------------------------------|--------------------------------------
Actual Class 1         True positives                 |         False negatives
------------------------------------------------------|--------------------------------------
Actual Class 0        False positives                 |         True negatives
------------------------------------------------------|--------------------------------------

# Cross-validation 

How do we know the results are not what they are owing to the particular partitioning of data? Create 10 training sets (and correspondingly, 10 test sets) with no overlapping samples between a training and test set pair. Train the classifier with the first training set and obtain the confusion matrix for the first test set. Repeat this for the remaining nine training and test set pairs. Average the ten confusion matrices that you obtain. This is called 10-fold cross validation. 

Leave-one-out cross validation 
If there are 200 samples, leaving one sample out and training with 199 remaining samples and then testing with the sample that has been left out constitutes one run of this leave-one-out cross validation. The final result is the average of the 200 runs (one for each test sample). This is typically used when the initial training data is very limited.

# Answer the following questions - 

1. Which SVM kernel gives a higher accuracy? 
Accuracy = (sum of the elements of the prinicipal diagonal)/ (sum of all the elements in the confusion matrix)

2. Instead of 200 samples (100 +ve and 100 -ve), if you have only 100 samples (50 +ve and 50 -ve) in the training phase, how does the confusion matrix change, if at all? [This is a typical case for leave-one-out cross validation.]
