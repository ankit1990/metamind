import tornado.ioloop
import tornado.web

import classifier_handler;
import uploader;

class MainHandler(tornado.web.RequestHandler):
  def get(self):
    self.render("index.html");

application = tornado.web.Application([
  (r"/upload", uploader.Uploader),
  (r"/test", classifier_handler.ClassifierActionHandler),
  (r"/", MainHandler),
], debug=True)

if __name__ == "__main__":
  application.listen(8888)
  tornado.ioloop.IOLoop.instance().start()
