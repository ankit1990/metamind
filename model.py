import bag_of_words;

"""
  Class encapsulating information between the label, text and their
  representation.
"""
class Model:
  
# Let each feature vector be represented in a bag of dictionary model.
  def __init__(self):
    self.dictionary = set();
    self.X = [];
    self.Y = [];
  
# Add each data point to the set of words.
  def addPoint(self, text, label):
    # for each word in label.
    for w in text:
      if w not in self.dictionary:
        self.dictionary.add(w);
    
    self.X.append(text);
    self.Y.append(label);

  def getTransformedFeatureVectors(self):
    bow = bag_of_words.BagOfWords(self.dictionary);
    fvs = [];
    labels = [];
    for i in range(1,len(self.X)):
      label = self.getLabel(self.Y[i]);
      fv = [1];
      fv.extend(bow.bagify(self.X[i]));
      fvs.append(fv);
      labels.append(self.getLabel(self.Y[i]));
    return self.dictionary, fvs, labels;

  def getLabel(self, textLabel): 
    if textLabel == "positive":
      return 1; 
    return 0;
