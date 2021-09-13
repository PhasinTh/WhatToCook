from flask import Flask
from flask_restful import Resource, Api
from api.file import Files, DeleleteFile
from api.process import Process

app = Flask(__name__)
api = Api(app)

@app.after_request

def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
  return response


api.add_resource(DeleleteFile, '/files/delete')
api.add_resource(Files, '/files')
api.add_resource(Process, '/process')

if __name__ == '__main__':
    app.run(debug=True)