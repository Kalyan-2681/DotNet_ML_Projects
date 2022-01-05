from flask_restful import Api, Resource
from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
import pickle
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

def get_items_from_cart(self,cust_id):
    """ Fetches items from sessions cart"""
    item_list = []
    cart_count = self.session.get('add_to_cart_count')
    if not cart_count: return None;
    for i in range(1, cart_count+1):
        item = self.session.get(str(i))
        if item:
            item_list.append(item)
    return item_list

@app.route('/',methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html") 


@app.route('/recommend/<int:cust_id>',methods=['POST','GET']) # route to show the predictions in UI
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            #  reading the customer id who has logged in to the online grocery store
            cust_id = request.args.get('cust_id')

            # retrieving customer cart details from session
            item_list = get_items_from_cart(cust_id)
            
            if(cust_id!= None):
                research=1
            else:
                research=0
            filename = "recommenderModel_KNN.pkl"
            loaded_model = pickle.load(open(filename, 'rb')) # loading the model file from the storage

            # User based recommend predictions using the loaded KNN model
            prediction=loaded_model.predict([[cust_id]])

            # Item based recommend predictions using the loaded KNN model
            #prediction=loaded_model.predict([[item_list]])

            print('prediction is :', prediction)
            # showing the prediction results in a UI
            return render_template('results.html',prediction=round(100*prediction[0]))
        except Exception as e:
            print('The Exception message is: ',e)
            return 'something went wrong'
    # return render_template('results.html')
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, port=8080)