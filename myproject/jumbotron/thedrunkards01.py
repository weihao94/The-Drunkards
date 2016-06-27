import urllib
import webapp2
import jinja2
import os

from google.appengine.api import users
from google.appengine.ext import ndb



jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + '/templates'))

class MainPage(webapp2.RequestHandler): #Handler for the main page

    def get(self):
        template = jinja_environment.get_template('index.html')
        self.response.out.write(template.render())



app = webapp2.WSGIApplication([('/', MainPage)],
                               debug=True)
