import os
import werkzeug
from flask_restful import Resource, reqparse

FILE_DIR = 'files'
class Files(Resource):
    def get(self):
        return os.listdir(FILE_DIR)

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('file', type=werkzeug.datastructures.FileStorage, location=FILE_DIR)
        args = parser.parse_args()
        file = args['file']
        file.save(os.path.join(FILE_DIR, file.filename))
        return os.listdir(FILE_DIR)
    
class DeleleteFile(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('filename')
        args = parser.parse_args()
        filename = os.path.join(FILE_DIR, str(args['filename']))
        print(filename)
        if os.path.exists(filename):
            os.remove(filename)
            return {"message": "Deleted", "files": os.listdir(FILE_DIR)}
        return "Error file not found!", 404