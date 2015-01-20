import os.path;
import pickle;

import tornado.web

import bag_of_words;
import classifier_trainer;
import model;
import lr;
import parser;


class ClassifierActionHandler(tornado.web.RequestHandler):
  def get(self):
    fileid = self.get_argument("id", None);

    if not fileid:
      self.finish("No id specified. Please specify an id.");
      return;

    if os.path.exists("classifier/" + fileid):
      sentence = self.get_argument("sentence", None);
      if sentence is not None:
        words = parser.parseTestText(sentence);
        print "Trying to classify the words", words;
        [betas, dictionary] = pickle.load(open("classifier/" + fileid, "rb"));
        bow = bag_of_words.BagOfWords(dictionary);
        fv = [1]
        fv.extend(bow.bagify(words))
        predictedClass = lr.classify(betas, fv);
        print "Predicting with a confidence of ", lr.sigmoid(betas, fv);
        if predictedClass == 1:
          self.write("The given sentence was found to be positive.");
        else:
          self.write("The given sentence was found to be negative.");
      else:
        sentence = "";

      self.write("<br/>"
                  + "<div>"
                  +  "<form method='get' action='test'>"
                  +     "<input type='text' name='sentence' value='" + sentence + "'>"
                  +     "<button type='submit'> Test the classifier! </button>" 
                  +     "<input type='hidden' name='id' value='" + fileid + "'>"
                  +   "</form>"
                  + "</div>");
      
    else:
      classifier_trainer.ClassifierTrainer(fileid);
      self.finish("The classifier will be trained right now. This is expected to take a few minutes. Please refresh this page after a few minutes");

