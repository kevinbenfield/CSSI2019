
import webapp2
import jinja2
import os

# This initializes the jinja2 Environment.
# This will be the same in every app that uses the jinja2 templating library.
the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class MainPage(webapp2.RequestHandler):
    def get(self):
        t = the_jinja_env.get_template('templates/welcome.html')
        self.response.write(t.render())

class AboutPage(webapp2.RequestHandler):
    def get(self):
       # self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('<h3>this is the about page</h3>')

class newspage(webapp2.RequestHandler):
    def get(self):
       # self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('<h3>Chicken fingers taste nasty</h3>')

class ResultPage(webapp2.RequestHandler):
    def get(self):
       # self.response.headers['Content-Type'] = 'text/plain'
        t = the_jinja_env.get_template('templates/results.html')
        self.response.write(t.render())

class FavoritePage(webapp2.RequestHandler):
    def get(self):
        t = the_jinja_env.get_template('templates/fav.html')
        favs = {"title":"My Favorite Websites","item1":"Google","item2":"Youtube","item3":"Twiteer","item4":"Facebook"}
        self.response.write(t.render(favs))
    def post(self):
        fn = self.request.get("firstname")
        ln = self.request.get("lastname")
        self.response.write(fn + " " + ln)


routes = [('/', MainPage),
            ('/about', AboutPage),
            ('/news', newspage),
            ('/result', ResultPage),
            ('/fav', FavoritePage)]


app = webapp2.WSGIApplication(routes, debug=True)
