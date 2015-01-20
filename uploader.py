import uuid;

import tornado.web;

class Uploader(tornado.web.RequestHandler):
  def post(self):
    fileinfo = self.request.files['data'][0];
    fname = fileinfo['filename'];
    cname = str(uuid.uuid4()) + '.tsv';
    fh = open("data/" + cname, 'w');
    fh.write(fileinfo['body']);
    self.finish("<div>"
      + "File upload was successful. Please check <a href=test.html?id=" + cname + ">"
      +  " this </a> link to train/test the classifier. </div>");
