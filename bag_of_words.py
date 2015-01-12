class BagOfWords:
  def __init__(self, dictionary):
    this.dictionary = dictionary;
    this.mapping = {};
   
    position = 0;
    for word in dictionary:
      mapping[word] = position;
      position = position + 1;
   
  """
    Takes a list of words and returns the corresponding representation
    as bag of words feature vector.
  """
  def bagify(word_list):
    features = [0] * len(dictionary);

    for w in word_list:
      position = getPosition(w);
      if not position == -1:
        features[position] = features[position] + 1;     

    return features;

  """
    Returns the position of the word in dictionary, if it exists in the dictionary.
    -1 otherwise.
  """
  def getPosition(word):
    if not word in mapping:
      return -1;

    return mapping[word];
