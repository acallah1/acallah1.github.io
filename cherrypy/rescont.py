#Andrew Callahan
#CherryPy Primer

import cherrypy
import re
import json

class ResetController(object):
	def __init__(self, mydb):
		self.mydb=mydb
	def PUT(self):
		self.mydb.load_all('/home/paradigms/ml-1m/ratings.dat', '/home/paradigms/ml-1m/users.dat','/home/paradigms/ml-1m/movies.dat')
		result = dict()
		result['result'] = 'success'
		return json.dumps(result)

	def PUT_MID(self,movie_id):
		self.mydb.load_mid(movie_id,'/home/paradigms/ml-1m/movies.dat')
		result = dict()
		result['result'] = 'success'
		return json.dumps(result)