from pymongo import MongoClient
from random import randint
from datetime import datetime 
from twitter import *
import pprint
# Site usado para maior entendimento da teoria: https://www.mongodb.com/blog/post/getting-started-with-python-and-mongodb
# COMO USAR MONGODB:
# No terminal escreva mongo
# Em seguida escreva use db_twitter_emotion
# db.db_twitter_emotion.insert({"name": "testando"})
# liste os bancos de dados e ele aparecera
# show dbs


class Database:
    #Passo 1: Conexao com mongodb
    def __init__(self,dbname):
        self.client = MongoClient(port=27017)
        self.db = self.client[dbname]

    def insert(self, newdata):
        twitter = {
        'date' : newdata.date, 
        'tag' : newdata.tag,
        'emotion' : newdata.emotion,
        'isObjective': newdata.isObjective
        }
        return self.db.twitter.insert_one(twitter)    

    def insertList(self,list):
        count = 0
        for t in list:
            result = self.insert(t)
            print('Created {0} of 500 as {1}'.format(count,result.inserted_id))
            count = count + 1
    
    def findAll(self): 
        return self.db.twitter.find()

    def findBy(self,query):
        return self.db.twitter.find(query) 

    def removeAll(self):
        return self.db.twitter.remove()

    def removeBy(self,query):
        return self.db.twitter.remove(query)

    def updateBy(self, query, newdata): 
        twitter = {
        'date' : newdata.date, 
        'tag' : newdata.tag,
        'emotion' : newdata.emotion,
        'isObjective': newdata.isObjective
        }
        return self.db.twitter.update(query,twitter) 


