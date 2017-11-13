#Andrew Callahan
#CherryPy Primer

import cherrypy
import re
import json

class RatingsController(object):
	def __init__(self, mydb):
		self.mydb=mydb
	def GET(self,movie_id):
		result = dict()
		result['rating'] = self.mydb.get_rating(int(movie_id))
		result['movie_id'] = int(movie_id)
		result['result'] = 'success'
		return json.dumps(result)

