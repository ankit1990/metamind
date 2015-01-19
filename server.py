import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
  def get(self):
    self.render("index.html");

application = tornado.web.Application([
  (r"/", MainHandler),
])

if __name__ == "__main__":
  application.listen(8888)
  tornado.ioloop.IOLoop.instance().start()
