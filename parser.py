import re;
import nltk.corpus;

def cleanup(text):
  text = text.lower();
  text = re.sub("[^a-z]", " ", text);

  # Remove trailing spaces.
  words = [e.rstrip() for e in text.rsplit()];

  # Remove stopwords.
  stopwords = nltk.corpus.stopwords.words('english');
  words = [w for w in words if not w in stopwords] ;

  # Maybe have a better set of features consisting of porter
  # stemming etc.
  return words;

# Parse a give .tsv file.
def parseFeature(line):
  label = "";
  text = [];

  tokenizedWords = line.rsplit('\t');

  label = tokenizedWords[0];

  text = tokenizedWords[1];

# Returns a comma separated list of words.
  words = cleanup(text);
  
  print label, words;
  return label, words;

def parseFile(f):
  return f.readlines();

def main():
  f = open("data/movie-reviews-dataset.tsv", 'r');
  lines = parseFile(f);
  for line in lines:
    parseFeature(line);

if __name__ == "__main__":
  main();   
