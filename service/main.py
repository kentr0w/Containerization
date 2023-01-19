from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)

CORS(app)

@app.route("/user", methods=['POST'])
def hey():
  print("Hey!")

@app.route("/users")
def hello_world():
    return """
    {"key":[{"description":"qwe","email":"qwe","firstname":"qwe","id":1,"job_title":"qwe","lastname":"qwe"},{"description":"qwe","email":"qwe","firstname":"qwe","id":2,"job_title":"qwe","lastname":"qwe"},{"description":"qwe","email":"qwe","firstname":"qwe","id":3,"job_title":"qwe","lastname":"qwe"},{"description":"qwe","email":"eeee","firstname":"qwe","id":4,"job_title":"qwe","lastname":"qwe"},{"description":"qwe","email":"eeee","firstname":"qwe","id":5,"job_title":"qwe","lastname":"qwe"},{"description":"d","email":"d","firstname":"d","id":6,"job_title":"d","lastname":"d"},{"description":"dfgd","email":"dfgd","firstname":"fgd","id":7,"job_title":"dfgdf","lastname":"dfgdf"}]}
    """
