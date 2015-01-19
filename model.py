import bag_of_dictionary;

"""
  Class encapsulating information between the label, text and their
  representation.
"""
class Model
  
# Let each feature vector be represented in a bag of dictionary model.
  def __init__(self):
    self.dictionary = set();
    self.X = [];
    self.Y = [];
  
# Add each data point to the set of words.
  def addPoint(self, text, label):
    # for each word in label.
    for w in text:
      if w not in self.dictionary
        self.dictionary.add(w);
    
    self.X.append(text);
    self.Y.append(label);
  
"""
  Returns a list of feature vectors. The last element of each of the feature vector is either a +1
  or -1, indicating that the text in question is either positive or negative.
"""
  def getTransformedFeatureVectors(self):
    self.bow = BagOfWords(self.dictionary);
   
    fvs = [];
    for i in range(1,len(self.X)):
      label = getLabel(self.Y(i));
      fv = self.bow.bagify(self.X(i));
      fv.append(self.getLabel(self.Y(i));
      fvs.append(fv);
    return fvs;

  def getLabel(textLabel): 
   if textLabel == "positive":
     return 1; 
   return -1;
