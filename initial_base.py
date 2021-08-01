from pymongo import MongoClient

client = MongoClient("127.0.0.1:27017")
db = client.forms

initial_set = (
    {'name': 'birthday', 'birthday': 'date', 'tellno': 'phone', 'first_name': 'text', 'last_name': 'text'},
    {'name': 'phonebook', 'work_tel': 'phone', 'cell': 'phone', 'first_name': 'text', 'last_name': 'text'},
    {'name': 'carregistry', 'made': 'date', 'owner': 'phone', 'first_name': 'text', 'last_name': 'text'}
)

if db.variants.find().count() == 0:
    result = db.variants.insert_many(initial_set)
