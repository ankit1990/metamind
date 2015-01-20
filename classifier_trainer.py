import threading
import pickle;

import lr;
import model;

class ClassifierTrainer:
   def __init__(self, filename):
     self.filename = filename;
     thread = threading.Thread(target=self.run, ,args=());
     thread.daemon = True;
     thread.start();
  
   def run():
     trainModel();
    
   def trainModel():
     f = open("data/" + self.filename, 'r');
     lines = parseFile(f);
  
     rawX = [];
     rawY = [];
  
     m = model.Model(); 
     for line in lines:
      (f,v) = parser.parseFeature(line);
     m.addPoint(f, v);
 
     print "Reading input data finished.";

    (dictionary, fvs, labels) = m.getTransformedFeatureVectors();  
    betas = lr.trainLogisticRegressionClassifier(fvs, labels, 10);
  
    misClassified = 0;
    for i in range(1,len(fvs)):
      predicted = lr.classify(betas, fvs[i]); 
      if predicted != labels[i]:
        misClassified += 1;
 
    pickle.dump([betas, dictionary], open("classifier/" + filename, 'wb'));
    print betas; 
    print misClassified, "/", len(fvs);
