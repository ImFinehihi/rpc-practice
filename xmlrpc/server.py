from xmlrpc.server import SimpleXMLRPCServer

def add(a, b):
    return a + b

server = SimpleXMLRPCServer(("0.0.0.0", 8000))

print("Server đang chạy tại cổng 8000...")

server.register_function(add, "add")

server.serve_forever()
