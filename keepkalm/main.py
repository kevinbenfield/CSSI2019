import webapp2
import jinja2
import os

jinja_env =  jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

    class MainPage(webapp2.RequestHandler):
        def get(self):
            t = jinja_env.get_template('/templates/index.html')
            seed_data()
            self.response.write(t.render())

        def post(self):
            t = jinja_env.get_template('/templates/index.html')
            self.response.write(t.render())


routes = [('/',MainPage)]
app = webapp2.WSGIApplication(routes, debug=True)
