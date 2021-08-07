from flask import Flask
from flask_restful import Api, Resource
#import dboperations
import logging

app = Flask(__name__)
api = Api(app)

recommendations = {}
class GetRecommendation(Resource):
    def get(self,cust_id):
        return recommendations[cust_id]
    
    def post(self):
        return {"data": "grocery recommendations"}
# route
api.add_resource(GetRecommendation, "/recommend/<")

if __name__ == "__main__":
    app.run(debug=True, port=8080)