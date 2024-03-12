from flask import Flask
from controller import init

app = Flask(__name__, template_folder="views")

init(app)

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)