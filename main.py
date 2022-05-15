from http.server import HTTPServer, CGIHTTPRequestHandler
from sqlalchemy import create_engine

from database import Base

server_address = ("", 8000)
engine = create_engine('sqlite:///my_db.db', echo=True)

httpd = HTTPServer(server_address, CGIHTTPRequestHandler)

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    httpd.serve_forever()
