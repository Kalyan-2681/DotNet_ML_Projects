import base64
import pymongo
from pymongo import MongoClient
import bson
from bson.raw_bson import RawBSONDocument
import logging

logging.info("inside dboperations")

def getcustomer(cust_id):
        logging.info("inside getcustomer")
        results = readfromdb(cust_id)
        return {"data": results}
 

def readfromdb(searchString): 
    logging.info("inside readfromdb")   
    USR = "webuser"   
    PWD = "carnivaL1"
    DB_NAME = "ElectronicEcommerce"  # Specifiy a Database Name
    CLUSTER = f"mongodb+srv://{USR}:{PWD}@cluster0.hhuga.mongodb.net/{DB_NAME}?retryWrites=true&w=majority"
    COLLECTION_NAME = "Site"
    dbclient = MongoClient(CLUSTER)
    dataBase = dbclient[DB_NAME]
    collection = dataBase[COLLECTION_NAME]
    for record in collection.find_all({},{'site_id': searchString}):
        result = []
        result = record.__dict__
        logging.info("records :  " + record.__dict__) 
    return result       

    dbclient.close()

def writetodb(searchString,searchdata):    
    USR = "webuser"   
    PWD = "carnivaL1"
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
