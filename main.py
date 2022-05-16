from http.server import HTTPServer, CGIHTTPRequestHandler

from htbin.database import Base, engine

server_address = ("", 8000)

httpd = HTTPServer(server_address, CGIHTTPRequestHandler)

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    httpd.serve_forever()
