from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
import requests
from urllib.request import urlopen as uReq
import dboperations
import pandas as pd
import logging

app = Flask(__name__)


@app.route('/', methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")


@app.route('/review', methods=['POST', 'GET'])  # route to show the review comments in a web UI
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            reviews = ""
            return render_template('results.html', reviews])

        except Exception as e:
            print('The Exception message is : ', e)
            return 'something is wrong'
    # return render_template('results.html')

    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)