import SocketServer
 
class hwRequestHandler( SocketServer.StreamRequestHandler ):
  def handle( self ):
    self.wfile.write("Hello World!\n")
 
 
server = SocketServer.TCPServer( ('localhost', 2525), hwRequestHandler )
server.serve_forever()
