from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# Restrict to a particular path
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
with SimpleXMLRPCServer(
    ('0.0.0.0', 8000),
    requestHandler=RequestHandler
) as server:

    server.register_introspection_functions()

    # Hàm cộng
    def adder_function(x, y):
        return x + y

    server.register_function(adder_function, 'add')

    # Class nhân
    class MyFuncs:
        def mul(self, x, y):
            return x * y

    server.register_instance(MyFuncs())

    print("Server đang chạy tại cổng 8000...")

    # Run server
    server.serve_forever()
