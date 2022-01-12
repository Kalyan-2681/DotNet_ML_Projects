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
from sklearn.decomposition import TruncatedSVD
from sklearn.neighbors import NearestNeighbors


class RecommenderModel:
    def __init__(self):        
        self.file_object = './logs/recommendationModelKNN.log'        
        self.log_writer = logger.logger(self.file_object)

    def getDatafromDB(Collectionname):
        # User name
        USR = "webuser" # readWrite for DB
        # PWDPLAINTXT = base64.b64encode("password".encode("utf-8"))
        # PWD = base64.b64decode("cGFzc3dvcmQ=").decode("utf-8")
        # Password
        PWD = "password"
        DB_NAME = "ElectronicCommerce"  # Specifiy a Database Name
        CLUSTER = f"mongodb+srv://{USR}:{PWD}@cluster0.hhuga.mongodb.net/{DB_NAME}?retryWrites=true&w=majority"
        COLLECTION_NAME = Collectionname
        dbclient = MongoClient(CLUSTER)
        dataBase = dbclient[DB_NAME]
        collection = dataBase[COLLECTION_NAME]

       # Get data from MongoDB
        cursor = collection.find()
        # Expand the cursor and construct the DataFrame
        df =  pd.DataFrame(list(cursor))

        dbclient.close()
        return df

    def predictKNN(pivoted_data):
        
        svd = TruncatedSVD(n_components=200)
        latent_matrix = svd.fit_transform(pivoted_data)
        model_knn = NearestNeighbors(metric = 'cosine', algorithm = 'brute')
        model_knn.fit(pivoted_data) 

        query_index = np.random.choice(pivoted_data.shape[0])        
        distances, indices = model_knn.kneighbors(pivoted_data.iloc[query_index,:].values.reshape(1, -1), n_neighbors = 6)

        for i in range(0, len(distances.flatten())):
            if i == 0:
                return (pivoted_data.index[query_index])
            else:
                return (i, pivoted_data.index[indices.flatten()[i]], distances.flatten()[i])