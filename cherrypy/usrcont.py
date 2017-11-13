#Andrew Callahan
#CherryPy Primer

import cherrypy
import re
import json

class UserController(object):
	def __init__(self, mydb):
		self.mydb=mydb
	def GET(self):
		output = {'result':'success'}
		try:
			users = list()
			for user in self.mydb.get_users():
				d = dict()
				d['gender'] = self.mydb.get_user(user)[0]
				d['age'] = self.mydb.get_user(user)[1]
				d['occupation'] = self.mydb.get_user(user)[2]
				d['zipcode'] = self.mydb.get_user(user)[3]
				d['id'] = user
				users.append(d)
			output['users'] = users
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
			l.append(body['gender'])
			l.append(int(body['age']))
			l.append(int(body['occupation']))
			l.append(body['zipcode'])
			id = 1
			for user in self.mydb.get_users():
				if user > id:
					id = user
			id = id+1
			self.mydb.set_user(id , l)
			output = {'result':'success'}
			output['id'] =id 
		except:
			output = {'result':'error', 'message':'wrong input'}
		return json.dumps(output)

	def DELETE(self):
		try:
			self.mydb.delete_users()
			output = {'result':'success'}
		except:
			output = {'result':'error'}
		return json.dumps(output)

	def GET_ID(self,user_id):
		output = {'result':'success'}
		try:
			l = self.mydb.get_user(int(user_id))
			output['gender'] = l[0]
			output['age'] = l[1]
			output['occupation'] = l[2]
			output['zipcode'] = l[3]
			output['id'] = user_id
		except:
			output['result'] = 'error'
		return json.dumps(output)

	def PUT_ID(self,user_id):
		cl = cherrypy.request.headers['Content-Length']
		rawbody = cherrypy.request.body.read(int(cl))
		body = json.loads(rawbody)
		try:
			l = list()
			l.append(body['gender'])
			l.append(int(body['age']))
			l.append(int(body['occupation']))
			l.append(body['zipcode'])
			id = int(user_id)
			self.mydb.set_user(id , l)
			output = {'result':'success'}
		except:
			output = {'result':'error', 'message':'wrong input'}
		return json.dumps(output)

	def DELETE_ID(self,user_id):
		output = {'result':'success'}
		try:
			self.mydb.delete_user(int(user_id))
		except:
			output['result'] = 'error'
		return json.dumps(output)
