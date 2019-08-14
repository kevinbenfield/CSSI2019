# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import webapp2


class MainPage(webapp2.RequestHandler):
    def get(self):
       # self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('<h1>Hello,Kevin!</h1>')

class AboutPage(webapp2.RequestHandler):
    def get(self):
       # self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('<h3>this is the about page</h3>')

class newspage(webapp2.RequestHandler):
    def get(self):
       # self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('<h3>Chicken fingers taste nasty</h3>')



routes = [('/', MainPage),('/about', AboutPage),("/news", newspage)]
app = webapp2.WSGIApplication(routes, debug=True)
