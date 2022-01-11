import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pymongo import MongoClient
import dns
# import excel2json
import json
import os
from itertools import groupby
from logger import logger


class RecommenderModel:
    def __init__(self):        
        self.file_object = './logs/recommendationModelKNN.log'        
        self.log_writer = logger.logger(self.file_object)

    def getDatafromDB(COLLECTION_NAME):
        # User name
        USR = "webuser" # readWrite for DB
        # PWDPLAINTXT = base64.b64encode("password".encode("utf-8"))
        # PWD = base64.b64decode("cGFzc3dvcmQ=").decode("utf-8")
        # Password
        PWD = "password"
        DB_NAME = "ElectronicCommerce"  # Specifiy a Database Name
        CLUSTER = f"mongodb+srv://{USR}:{PWD}@cluster0.hhuga.mongodb.net/{DB_NAME}?retryWrites=true&w=majority"
        COLLECTION_NAME = "Customer"
        dbclient = MongoClient(CLUSTER)
        dataBase = dbclient[DB_NAME]
        collection = dataBase[COLLECTION_NAME]

       # Get data from MongoDB
        cursor = collection.find()
        # Expand the cursor and construct the DataFrame
        df =  pd.DataFrame(list(cursor))

        dbclient.close()
        return df

        