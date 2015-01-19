import model;
import train;
import parser;


def parseFile(f):
  return f.readlines();

def main():
  f = open("data/movie-reviews-dataset.tsv", 'r');
  lines = parseFile(f);
  
  rawX = [];
  rawY = [];
  
  m = model.Model(); 
  for line in lines:
    (f,v) = parser.parseFeature(line);
    m.addPoint(f, v);
 
  print "Reading input data finished.";

  (bow, fvs, labels) = m.getTransformedFeatureVectors();  
  betas = train.logisticRegression(fvs, labels, 10);
  
  misClassified = 0;
  for i in range(1,len(fvs)):
    predicted = train.classify(betas, fvs[i]); 
    if predicted != labels[i]:
      misClassified += 1;
   
  print betas; 
  print misClassified, "/", len(fvs);
   
if __name__ == "__main__":
  main();
