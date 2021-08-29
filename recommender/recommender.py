from flask import Flask
from flask_restful import Api, Resource
import dboperations
import logging

app = Flask(__name__)
api = Api(app)

#dummy data
recommendations = {"001":{"fruits":{"apple", "mango", "fig", "guava"}, "vegetables":{"cabbage","onion", "garlic", "carrot", "potato"}},
                   "002":{"fruits":{"apricot", "mango", "plum"}, "vegetables":{"cabbage", "carrot"}},
                   "003":{"fruits":{"banana", "mango", "nectarine"}, "vegetables":{"cabbage","garlic", "carrot"}},
                   "004":{"fruits":{"apple", "mango", "grapes"}, "vegetables":{"cabbage", "carrot", "potato"}},
                   "005":{"fruits":{"blackberry", "mango", "orange", "cherry"}, "vegetables":{"cabbage","onion", "carrot"}}
                   }

logging.basicConfig(filename='recommender.log', encoding='utf-8', level=logging.DEBUG)
logging.info("check 1")
class GetRecommendation(Resource):
    def get(self,cust_id):
        try:
            sitedata = dboperations.getcustomer(cust_id)
            logging.info("getting site information")
            return sitedata["site_name"]      
        except:
            logging.info("default site information")    
            return {"Site Name":"Catering"}
    
# route
api.add_resource(GetRecommendation, "/recommend/<int:cust_id>")

if __name__ == "__main__":
    app.run(debug=True, port=8080)