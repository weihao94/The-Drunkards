import urllib
import webapp2
import jinja2
import os

from google.appengine.api import users
from google.appengine.ext import ndb



jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + '/templates'))

# END OF IMPORTS #

# START OF STALLHOLDER MODELLING #

class Stall(ndb.Model):
    name = ndb.StringProperty()
    owner = ndb.StringProperty()
    menu = ndb.TextProperty()

class MainPage(webapp2.RequestHandler): #Handler for the main page
    def get(self):
        user = users.get_current_user()
        if user:  # signed in already
            curr = ndb.Key('Stall', users.get_current_user().nickname())
            person = curr.get()
            template_values = {
                'user_nickname': users.get_current_user().nickname(),
                'logout': users.create_logout_url(self.request.host_url),
                'stall_name': person.name}
            template = jinja_environment.get_template('index.html')
            self.response.out.write(template.render(template_values))
        else:
            curr = ndb.Key('Stall', 'test@example.com')
            person = curr.get()
            template_values = {
                'stall_name': person.name}
            template = jinja_environment.get_template('index.html')
            self.response.out.write(template.render(template_values))

class About(webapp2.RequestHandler): #Handler for the about page
    def get(self):
        template = jinja_environment.get_template('about.html')
        self.response.out.write(template.render())

class stall1(webapp2.RequestHandler): #Handler for the stores
    def get(self):
        user = users.get_current_user()
        if user:  # signed in already
            curr = ndb.Key('Stall', users.get_current_user().nickname())
            person = curr.get()
            if person == None:
                template_values = {
                    'user_nickname': users.get_current_user().nickname(),
                    'logout': users.create_logout_url(self.request.host_url),
                    }
                template = jinja_environment.get_template('stall1.html')
                self.response.out.write(template.render(template_values))
            else:
                template_values = {
                    'user_nickname': users.get_current_user().nickname(),
                    'logout': users.create_logout_url(self.request.host_url),
                    'stall_name': person.name
                    }
                template = jinja_environment.get_template('stall1.html')
                self.response.out.write(template.render(template_values))
        else:
            curr = ndb.Key('Stall', 'test@example.com')
            person = curr.get()
            template_values = {'stall_name': person.name}
            template = jinja_environment.get_template('stall1.html')
            self.response.out.write(template.render(template_values))

class stall1_page(webapp2.RequestHandler): #Handler for the stores
    def get(self):
        user = users.get_current_user()
        if user:  # signed in already
            curr = ndb.Key('Stall', users.get_current_user().nickname())
            person = curr.get()
            if person == None:
                template_values = {
                    'user_nickname': users.get_current_user().nickname(),
                    'logout': users.create_logout_url(self.request.host_url),
                    }
                template = jinja_environment.get_template('stall1_page.html')
                self.response.out.write(template.render(template_values))
            else:
                template_values = {
                    'user_nickname': users.get_current_user().nickname(),
                    'logout': users.create_logout_url(self.request.host_url),
                    'stall_name': person.name
                    }
                template = jinja_environment.get_template('stall1_page.html')
                self.response.out.write(template.render(template_values))
        else:
            self.redirect(self.request.host_url)
            
    def post(self):
        curr = ndb.Key('Stall', users.get_current_user().nickname())
        person = curr.get()
        if person == None:
            person = Stall(id=users.get_current_user().nickname())
            person.email = users.get_current_user().email()
        person.name = self.request.get('name')
        person.put()
        template_values = {
                'user_nickname': users.get_current_user().nickname(),
                'logout': users.create_logout_url(self.request.host_url),
                'stall_name': person.name
                }
        template = jinja_environment.get_template('stall1_page.html')
        self.response.out.write(template.render(template_values))
        

class stall2(webapp2.RequestHandler): #Handler for the stores
    def get(self):
        template = jinja_environment.get_template('stall2.html')
        self.response.out.write(template.render())

class stall2_page(webapp2.RequestHandler): #Handler for the stores

    def get(self):
        user = users.get_current_user()
        if user:  # signed in already
            template_values = {
                'user_nickname': users.get_current_user().nickname(),
                'logout': users.create_logout_url(self.request.host_url),
                }
            template = jinja_environment.get_template('stall2_page.html')
            self.response.out.write(template.render(template_values))
        else:
            template = jinja_environment.get_template('stall2_page.html')
            self.response.out.write(template.render())

class stall3(webapp2.RequestHandler): #Handler for the stores
    def get(self):
        template = jinja_environment.get_template('stall3.html')
        self.response.out.write(template.render())

class stall3_page(webapp2.RequestHandler): #Handler for the stores

    def get(self):
        user = users.get_current_user()
        if user:  # signed in already
            template_values = {
                'user_nickname': users.get_current_user().nickname(),
                'logout': users.create_logout_url(self.request.host_url),
                }
            template = jinja_environment.get_template('stall3_page.html')
            self.response.out.write(template.render(template_values))
        else:
            template = jinja_environment.get_template('stall3_page.html')
            self.response.out.write(template.render())

app = webapp2.WSGIApplication([('/', MainPage),
                               ('/thedrunkards', MainPage),
                               ('/about', About),
                               ('/stall1', stall1),
                               ('/stall1_page', stall1_page),
                               ('/stall2', stall2),
                               ('/stall2_page', stall2_page),
                               ('/stall3', stall3),
                               ('/stall3_page', stall3_page)],
                               debug=True)
