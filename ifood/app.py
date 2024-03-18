from flask import Flask
from controller import routes

server = Flask(__name__, template_folder="views")

routes.init(server)

if __name__ == '__main__':
    server.run(host='localhost', port=5000, debug=True)