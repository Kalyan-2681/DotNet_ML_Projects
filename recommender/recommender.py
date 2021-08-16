from flask import Flask
from flask_restful import Api, Resource
#import dboperations
import logging

app = Flask(__name__)
api = Api(app)

recommendations = {"001":{"fruits":{"apple", "mango"}, 
                    "vegetables":{"cabbage", "carrot"},
                    "002":{"fruits":{"apple", "mango"}, 
                    "vegetables":{"cabbage", "carrot"}}}
class GetRecommendation(Resource):
    def get(self,cust_id):
        return {"name":cust_id}
    
    def post(self):
        return {"data": "grocery recommendations"}
# route
api.add_resource(GetRecommendation, "/recommend/<int:cust_id>")

if __name__ == "__main__":
    app.run(debug=True, port=8080)