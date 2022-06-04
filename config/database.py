import os
# from dotenv import load_dotenv
from pymongo import MongoClient

# Unicamente para desarrollo
# load_dotenv()

db = MongoClient(os.getenv("MONGO_URI"))

# MongoClient por defecto se conecta al localhost:27017 y a la db que especifique en la colección.