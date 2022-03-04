from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
app = Flask(__name__)
api = Api(app)
CORS(app)
class status(Resource):
 def get(self):
    try:
        return {'data': 'Api running'}
    except:
        return {'data': 'An error occured'}
class Sum(Resource):
 def get(self, a, b):
    return jsonify({'data': a+b}) 
api.add_resource(status,'/')
api.add_resource(Sum,'/add/<int:a>,<int:b>')
class Diff(Resource):
 def get(self, a, b):
    return jsonify({'data': a-b}) 
api.add_resource(status,'/')
api.add_resource(Diff,'/diff/<int:a>,<int:b>')
class Mult(Resource):
 def get(self, a, b):
    return jsonify({'data': a*b}) 
api.add_resource(status,'/')
api.add_resource(Mult,'/mult/<int:a>,<int:b>')
class Div(Resource):
 def get(self, a, b):
    return jsonify({'data': a/b}) 
api.add_resource(status,'/')
api.add_resource(Div,'/div/<float:a>,<float:b>')
if __name__ == '__main__':
 app.run()

   

