#Andrew Callahan
#CherryPy Primer

import cherrypy
import re
import json

class OptionController(object):
	def __init__(self, mydb):
		self.mydb=mydb
	def OPTIONS(self, *args, **kargs):
		return ""
