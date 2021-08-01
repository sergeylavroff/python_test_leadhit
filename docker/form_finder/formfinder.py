from pymongo import MongoClient

client = MongoClient("mongodb:27017")
db = client.forms


def find_form(input):
    cursor = db.variants.find()
    for record in cursor:
        name = record.pop('name')
        record.pop('_id')
        if record.items() <= input.items():
            return name
    return input
