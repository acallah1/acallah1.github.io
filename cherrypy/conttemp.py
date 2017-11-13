#Andrew Callahan
#CherryPy Primer

import cherrypy
import re
import json

class ResetController(object):
	def __init__(self, mydb):
		self.mydb=mydb
	def GET(self,key):
		output = {'result':'success'}
		key = str(key)
		try:
			value = self.myd[key]
			output['key'] = key
			output['value'] = value
		except KeyError as ex:
			output['result'] = 'error'
			output['message'] = 'key not found'
		return json.dumps(output)

	def PUT(self,key):
		cl = cherrypy.request.headers['Content-Length']
		rawbody = cherrypy.request.body.read(int(cl))
		body = json.loads(rawbody)
		try:
			self.myd[key] = body['value']
			output = {'result':'success'}
		except:
			output = {'result':'error', 'message':'wrong input'}
		return json.dumps(output)

	def DELETE(self,key):
		try:
			del self.myd[key]
			output = {'result':'success'}
		except:
			output = {'result':'error', 'message':'key not found'}
		return json.dumps(output)

	def DELETE_ALL(self):
		#for key in self.myd:
			#del self.myd[key]
		self.myd = dict()
		output = {'result':'success'}
		return json.dumps(output)

	def POST(self):
		cl = cherrypy.request.headers['Content-Length']
		rawbody = cherrypy.request.body.read(int(cl))
		body = json.loads(rawbody)
		try:
			self.myd[body['key']] = body['value']
			output =  {'result':'success'}
		except:
			output = {'result':'error', 'message':'wrong input'}
		return json.dumps(output)

	def GET_ALL(self):
		l = list()
		for key in self.myd:
			l.append({'key':key, 'value':self.myd[key]})
		output = dict()
		output['entries'] = l
		output['result']='success'
		return json.dumps(output)
