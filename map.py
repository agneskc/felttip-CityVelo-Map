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

# Modules needed for code.
import cgi
import cgitb
cgitb.enable()
import webapp2, jinja2, os
import urllib2, json

# Load index.html file
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPage(webapp2.RequestHandler):

	def stations(self, data):
		
		station_dictList = data['stationBeanList'] # list of dictionaries associated with 'stationBeanList'
		
		stations = []
		
		for dictListItem in station_dictList: # for each dictionary item in the list called station_dictList
			
			stationItem = {}
			
			stationItem['stationName'] = dictListItem['stationName']
			stationItem['latitude'] = dictListItem['latitude']
			stationItem['longitude'] = dictListItem['longitude']				
			stationItem['availableBikes'] = dictListItem['availableBikes']
			stationItem['availableDocks'] = dictListItem['availableDocks']
			
			stations.append(stationItem)
		
		return stations
			
	def get(self):
		
		response = urllib2.urlopen('http://www.citibikenyc.com/stations/json')
		data = json.load(response)
		time_stamp = data['executionTime']
		stations = self.stations(data)
		
		# Jinja2 template fields for HTML
		template_fields = {
			'time_stamp': time_stamp,
			'stations': stations,
		}
		
		#render HTML table
		template = JINJA_ENVIRONMENT.get_template('index.html')
		self.response.write(template.render(template_fields))

app = webapp2.WSGIApplication([
    ('/', MainPage)
], debug=True)
