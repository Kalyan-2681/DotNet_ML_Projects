from flask import Flask
from flask_restful import Api, Resource
#import dboperations
import logging

app = Flask(__name__)
api = Api(app)

class GetRecommendation(Resource):
    def get(self):
        return {"data": "Hello World"}
    
    def post(self):
        return {"data": "Hello World from post"}
# route
api.add_resource(GetRecommendation, "/helloworld")

if __name__ == "__main__":
    app.run(debug=True, port=8080)