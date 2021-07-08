import base64
import pymongo
from pymongo import MongoClient
import bson
from bson.raw_bson import RawBSONDocument

def writetodb(searchString,searchdata):    
    USR = "webuser"   
    PWD = "####"
    DB_NAME = "ElectronicEcommerce"  # Specifiy a Database Name
    CLUSTER = f"mongodb+srv://{USR}:{PWD}@cluster0.hhuga.mongodb.net/{DB_NAME}?retryWrites=true&w=majority"
    COLLECTION_NAME = "Site"
    dbclient = MongoClient(CLUSTER)
    dataBase = dbclient[DB_NAME]
    collection = dataBase[COLLECTION_NAME]
    for record in collection.find({'Product': searchString}):
        print('found')
    # insert
    rec = collection.insert_many(searchdata)

    dbclient.close()
