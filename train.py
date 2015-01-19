import math;

"""
 Trains a feature module. Takes as input a list of feature vectors, labels, number of itearation for which gradient descent should be run, number of dimensions etc. and outputs coefficients for linear regression.
"""
def logisticRegression(fvs, labels, numIterations):
  numCoefficients = len(fvs[0]);
  coefficients = [0] * numCoefficients;
# using gradient descent.
  while numIterations > 0:
   print numIterations, "iterations are left."; 
   numIterations = numIterations - 1;
   for i in range(1, len(fvs)):
     fv = fvs[i];
     trainingLabel = labels[i];
     predicted = classify(coefficients, fv);
# If the predictedLabel does not match the actual label, update the coefficients.
     if predicted != trainingLabel:
# Update each of the coefficients.
       confidence = sigmoid(coefficients, fv);
       for j in range(1, numCoefficients):
         coefficients[j] += 0.01  * (trainingLabel - confidence) * fv[j];
  return coefficients;

def classify(coefficients, feature):
  p = sigmoid(coefficients, feature);
  if p > 0.5:
    return 1;
  return 0;

def sigmoid(coefficients, feature):
  logit = 0;
  for i in range(1, len(coefficients)):
    logit += coefficients[i] * feature[i];

  return 1.0/(1.0 + math.exp(-logit));
