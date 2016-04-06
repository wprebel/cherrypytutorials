import random
import string

import cherrypy

cherrypy.config.update({'server.socket_host': "0.0.0.0",'server.socket_port': 8085})

class StringGenerator(object):
    @cherrypy.expose
    def index(self):
        return "Hello world!"

    @cherrypy.expose
    def generate(self):
        return ''.join(random.sample(string.hexdigits, 8))

if __name__ == '__main__':
    cherrypy.quickstart(StringGenerator())
