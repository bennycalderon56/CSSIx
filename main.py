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
import random
#import jinja2
#import os\
from google.appengine.api import users

#jinja_env = jinja2.Enviroment(
#        loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
#        extensions=['jinja2.ext.autoescape'],
#        autoescape=True )
class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Sorry i had to do it to em')
        user = users.get_current_user()
        if user is not None:
            self.response.write('Hello Notes:')
        else:
            login_url = users.create_login_url(self.request.url)
            self.redirect(login_url)
class EmotionHandler(webapp2.RequestHandler):
    def get(self): #for a get request
        a_template = the_jinja_env.get_template('templates/sample_page.html')
        the_variable = {"an_emotion": "happy",
                "a_day_of_week": "Monday"}
        self.response.out.write(a_template.render(the_variables))
                

app = webapp2.WSGIApplication([
    ('/', MainPage),
 #   ('/feelings', EmotionHandler)
], debug=True)
