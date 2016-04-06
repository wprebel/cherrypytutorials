import cherrypy
cherrypy.config.update({'server.socket_host': "0.0.0.0",'server.socket_port': 8085})

class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        return "Hello world!"
    

if __name__ == '__main__':
   cherrypy.quickstart(HelloWorld())