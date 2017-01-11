from pymongo import MongoClient,ASCENDING
from time_trans import *
import datetime
class dataBase(object):
    def __init__(self):
        self.hostname="localhost"
        self.port=27017
        self.db=""
        self.col=""
        
    def welcome(self):
        print("###############")
        print("speed-up-input!")
        print("###############")
        print("Please make sure that a MongoDB instance is running on a host!!!!!!!!\n") 

    def preDB(self):
        hostname=input("please input your hostname,d for default")
        if hostname[0]=='d':
            self.hostname="localhost"
        port=input("please input port number,d for default\n")
        try:
            port=int(port)
        except Exception as err:
            self.port=27017
        self.db=input("please input your name of database: ")
        self.col=input("please input your name of collections: ")
        return self                         

    def openDB(self,dataext):
        client = MongoClient(self.hostname,self.port)
        dbs_name=self.db
        db=client[dbs_name]
        collections_name=self.col
        col=db[collections_name]
        col.create_index([("timeStamp", ASCENDING)])
        startDate=datetime_timestamp(input("please input startDate(YYYY-MM-DD HH:MM:SS): "))
        endDate=datetime_timestamp(input("please input endDate(YYYY-MM-DD HH:MM:SS): "))
        cursor=col.find({'timeStamp':{'$gte': startDate,'$lte': endDate}})   
        result=dataext.result(cursor)
        return result
        
   
    def __str__(self):
        return self.hostname+"  "+str(self.port)
