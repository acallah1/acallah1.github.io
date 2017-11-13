#Andrew Callahan
#CherryPy Primer

import cherrypy
import re
import json

class RecommendationsController(object):
	def __init__(self, mydb):
		self.mydb=mydb
	def GET(self,user_id):
		output = {'result':'success'}
		try:
			output['movie_id'] = self.mydb.get_highest_rated_new_movie(int(user_id))
		except KeyError as ex:
			output['result'] = 'error'
			output['message'] = 'key not found'
		return json.dumps(output)

	def PUT(self,user_id):
		cl = cherrypy.request.headers['Content-Length']
		rawbody = cherrypy.request.body.read(int(cl))
		body = json.loads(rawbody)
		try:
			self.mydb.set_user_movie_rating(int(user_id), int(body['movie_id']), float(body['rating']))
			output = {'result':'success'}
		except:
			output = {'result':'error', 'message':'wrong input'}
		return json.dumps(output)

	def DELETE(self):
		self.mydb.load_ratings('/home/paradigms/ml-1m/ratings.dat')
		result = dict()
		result['result'] = 'success'
		return json.dumps(result)
		
