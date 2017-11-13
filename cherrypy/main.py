import cherrypy
from rescont import ResetController
from ratingscont import RatingsController
from _movie_database import _movie_database
from reccont import RecommendationsController
from usrcont import UserController
from movcont import MovieController
from optcont import OptionController
import re
import json


def CORS():
    cherrypy.response.headers["Access-Control-Allow-Origin"] = "*"
    cherrypy.response.headers["Access-Control-Allow-Methods"] = "GET, PUT, POST, DELETE"
    cherrypy.response.headers["Access-Control-Allow-Credentials"] = "*"
            
def start_service():
	dispatcher = cherrypy.dispatch.RoutesDispatcher()

	mydb = _movie_database()
	mydb.load_all('/home/paradigms/ml-1m/ratings.dat', '/home/paradigms/ml-1m/users.dat' ,  '/home/paradigms/ml-1m/movies.dat')
	resetController = ResetController(mydb = mydb)
	ratingsController = RatingsController(mydb = mydb)
	recommendationsController = RecommendationsController(mydb = mydb)
	userController = UserController(mydb = mydb)
	movieController = MovieController(mydb = mydb)
	optionsController = OptionController(mydb = mydb)

	dispatcher.connect('dict_ratings_get' , '/ratings/:movie_id', controller = ratingsController, action = 'GET' , conditions=dict(method=['GET']))
	dispatcher.connect('dict_put_reset', '/reset/', controller=resetController, action = 'PUT', conditions=dict(method=['PUT']))
	dispatcher.connect('dict_put_reset_mid', '/reset/:movie_id', controller=resetController, action = 'PUT_MID', conditions=dict(method=['PUT']))
	dispatcher.connect('dict_delete_rec', '/recommendations/', controller=recommendationsController, action = 'DELETE', conditions=dict(method=['DELETE']))
	dispatcher.connect('dict_put_rec', '/recommendations/:user_id', controller=recommendationsController, action = 'PUT', conditions=dict(method=['PUT']))
	dispatcher.connect('dict_get_rec', '/recommendations/:user_id', controller=recommendationsController, action = 'GET', conditions=dict(method=['GET']))
	dispatcher.connect('dict_get_usr', '/users/', controller=userController, action = 'GET', conditions=dict(method=['GET']))
	dispatcher.connect('dict_post_usr', '/users/', controller=userController, action = 'POST', conditions=dict(method=['POST']))
	dispatcher.connect('dict_del_usr', '/users/', controller=userController, action = 'DELETE', conditions=dict(method=['DELETE']))
	dispatcher.connect('dict_get_id_usr', '/users/:user_id', controller=userController, action = 'GET_ID', conditions=dict(method=['GET']))
	dispatcher.connect('dict_post_id_usr', '/users/:user_id', controller=userController, action = 'PUT_ID', conditions=dict(method=['PUT']))
	dispatcher.connect('dict_del_id_usr', '/users/:user_id', controller=userController, action = 'DELETE_ID', conditions=dict(method=['DELETE']))
	dispatcher.connect('dict_get_mov', '/movies/', controller=movieController, action = 'GET', conditions=dict(method=['GET']))
	dispatcher.connect('dict_post_mov', '/movies/', controller=movieController, action = 'POST', conditions=dict(method=['POST']))
	dispatcher.connect('dict_del_mov', '/movies/', controller=movieController, action = 'DELETE', conditions=dict(method=['DELETE']))
	dispatcher.connect('dict_get_id_mov', '/movies/:movie_id', controller=movieController, action = 'GET_ID', conditions=dict(method=['GET']))
	dispatcher.connect('dict_post_id_mov', '/movies/:movie_id', controller=movieController, action = 'PUT_ID', conditions=dict(method=['PUT']))
	dispatcher.connect('dict_del_id_mov', '/movies/:movie_id', controller=movieController, action = 'DELETE_ID', conditions=dict(method=['DELETE']))
	dispatcher.connect('opt_usr' , '/users/' , controller = optionsController, action = 'OPTIONS', conditions = dict(method=['OPTIONS']))
	dispatcher.connect('opt_uid' , '/users/:user_id', controller = optionsController, action = 'OPTIONS', conditiions = dict(method=['OPTIONS']))
	dispatcher.connect('opt_mov' , '/movies/', controller = optionsController, action = 'OPTIONS', conditiions = dict(method=['OPTIONS']))
	dispatcher.connect('opt_mid' , '/movies/:movie_id', controller = optionsController, action = 'OPTIONS', conditiions = dict(method=['OPTIONS']))
	dispatcher.connect('opt_uid' , '/users/:user_id', controller = optionsController, action = 'OPTIONS', conditiions = dict(method=['OPTIONS']))
	dispatcher.connect('opt_rec' , '/recommendations/', controller = optionsController, action = 'OPTIONS', conditiions = dict(method=['OPTIONS']))
	dispatcher.connect('opt_uid' , '/recommendations/:user_id', controller = optionsController, action = 'OPTIONS', conditiions = dict(method=['OPTIONS']))
	dispatcher.connect('opt_uid' , '/reset/', controller = optionsController, action = 'OPTIONS', conditiions = dict(method=['OPTIONS']))
	dispatcher.connect('opt_uid' , '/reset/:movie_id', controller = optionsController, action = 'OPTIONS', conditiions = dict(method=['OPTIONS']))
	dispatcher.connect('opt_uid' , '/ratings/:movie_id', controller = optionsController, action = 'OPTIONS', conditiions = dict(method=['OPTIONS']))
	
	conf = { 'global' : {'server.socket_host': 'student04.cse.nd.edu','server.socket_port': 51020 } , '/' : {'request.dispatch': dispatcher, 'tools.CORS.on' : True} }

	cherrypy.config.update(conf)
	app = cherrypy.tree.mount(None,config=conf)


	cherrypy.quickstart(app)

	


if __name__ == '__main__':
	cherrypy.tools.CORS = cherrypy.Tool('before_finalize', CORS)
	start_service()


	
