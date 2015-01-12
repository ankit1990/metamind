def cleanup(features):
  # Remove trailing spaces.
  features = [e.rstrip() for e in features];

  # Decapitalize elements.
  features = [e.lower() for e in features];
 
  return features;
  # TODO(Remove punctuations):
  

# Parse a give .tsv file.
def parseFeature(line):
  label = "";
  features = [];

  tokenizedWords = line.rsplit('\t');

  label = tokenizedWords[0];

  features = tokenizedWords[1].rsplit(" ");

# Cleanup features.
  features = cleanup(features);

  print label, features;

def parseFile(f):
  return f.readlines();

def main():
  f = open("data/movie-reviews-dataset.tsv", 'r');
  lines = parseFile(f);
  for line in lines:
    parseFeature(line);

if __name__ == "__main__":
  main();   
