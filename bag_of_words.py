class BagOfWords:
  def __init__(self, dictionary):
    self.dictionary = dictionary;
    self.mapping = {};
  
    position = 0;
    for word in dictionary:
      self.mapping[word] = position;
      position = position + 1;
   
  """
    Takes a list of words and returns the corresponding representation
    as bag of words feature vector.
  """
  def bagify(self, word_list):
    features = [0] * len(self.dictionary);

    for w in word_list:
      position = self.getPosition(w);
      if not position == -1:
        features[position] = features[position] + 1;     

    return features;

  """
    Returns the position of the word in dictionary, if it exists in the dictionary.
    -1 otherwise.
  """
  def getPosition(self, word):
    if not word in self.mapping:
      return -1;

    return self.mapping[word];
