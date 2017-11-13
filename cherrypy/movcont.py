#Andrew Callahan
#CherryPy Primer

import cherrypy
import re
import json

class MovieController(object):
	def __init__(self, mydb):
		self.mydb=mydb
	def GET(self):
		output = {'result':'success'}
		try:
			movies = list()
			for mov in self.mydb.get_movies():
				d = dict()
				d['title'] = self.mydb.get_movie(mov)[0]
				d['genres'] = self.mydb.get_movie(mov)[1]
				with open('/home/paradigms/images.dat') as file:
					for line in file:
						tokens = line.split('::')
						if int(tokens[0]) == mov:
							d['img'] = tokens[2].strip()
				d['id'] = mov
				movies.append(d)
			output['movies'] = movies
		except KeyError as ex:
			output['result'] = 'error'
			output['message'] = 'key not found'
		return json.dumps(output)

	def POST(self):
		cl = cherrypy.request.headers['Content-Length']
		rawbody = cherrypy.request.body.read(int(cl))
		body = json.loads(rawbody)
		try:
			l = list()
			l.append(body['title'])
			l.append(body['genres'])
			id = 1
			for movie in self.mydb.get_movies():
				if movie > id:
					id = movie
			id = id+1
			self.mydb.set_movie(id , l)
			output = {'result':'success'}
			output['id'] =id 
		except:
			output = {'result':'error', 'message':'wrong input'}
		return json.dumps(output)

	def DELETE(self):
		try:
			self.mydb.delete_movies()
			output = {'result':'success'}
		except:
			output = {'result':'error'}
		return json.dumps(output)

	def GET_ID(self,movie_id):
		output = {'result':'success'}
		try:
			l = self.mydb.get_movie(int(movie_id))
			output['title'] = l[0]
			output['genres'] = l[1]
			with open('/home/paradigms/images.dat') as file:
					for line in file:
						tokens = line.split('::')
						if tokens[0] == movie_id:
							output['img'] = tokens[2].strip()
			output['id'] = movie_id
		except:
			output['result'] = 'error'
		return json.dumps(output)

	def PUT_ID(self,movie_id):
		cl = cherrypy.request.headers['Content-Length']
		rawbody = cherrypy.request.body.read(int(cl))
		body = json.loads(rawbody)
		try:
			l = list()
			l.append(body['title'])
			l.append(body['genres'])
			id = int(movie_id)
			self.mydb.set_movie(id , l)
			output = {'result':'success'}
		except:
			output = {'result':'error', 'message':'wrong input'}
		return json.dumps(output)

	def DELETE_ID(self,movie_id):
		output = {'result':'success'}
		try:
			self.mydb.delete_movie(int(movie_id))
		except:
			output['result'] = 'error'
		return json.dumps(output)
