#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
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
#
import webapp2

form="""
<form method="post" action="/testform">
	What is your birthday?
	<label>
	month
		<input name="month"  value="%(month)s">
	</label>
	<label>
	day
		<input name="day"   value="%(day)s">
	</label>
	<label>
	year
		<input name="year"   value="%(year)s">
	</label>
	
	<div style="color:red">
		%(error)s
	</div>
	
	<input type="submit">
</form>
"""

def valid_year(user_year):
	return True;

import cgi
def escape_html(s):
	return cgi.escape(s, quote = True);
				
class MainHandler(webapp2.RequestHandler):
    def get(self):
        write_form()
		
	def post(self):
		user_month = self.request.get("month")
		user_day = self.request.get("day")
		user_year = self.request.get("year")

		month = valid_month(self.request.get("month"))
		day = valid_day(self.request.get("day"))
		year = valid_year(self.request.get("year"))
		
		if not (month and day and year)
			self.write_form("wrong", user_month, user_day, user_year);
		else
			self.write_form("correct");
		
	def write_form(self, error="", month="", year="", day=""):
		self.response.out.write(form % {"error": error,
										"day": escape_html(day),
										"month": escape_html(month),
										"year": yescape_html(year)})
		

class TestMainHandler(webapp2.RequestHandler):
    def get(self):
		q = self.request.get("q")
		self.response.out.write(q)
		
app = webapp2.WSGIApplication([    
	('/', MainHandler),
	('/testform', TestMainHandler)
], debug=True)
