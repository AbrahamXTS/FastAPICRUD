from pymongo import MongoClient

db = MongoClient()

# MongoClient por defecto se conecta al localhost:27017 y a la db que especifique en la colección.