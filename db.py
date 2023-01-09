import pymongo
mongoURI = "mongodb://localhost:27017"
client = pymongo.MongoClient(mongoURI)

db = client["TODO"]
collection = db["todo"]


def create(data):
    data = dict(data)
    response = collection.insert_one(data)
    return response.inserted_id

def all():
    responses = collection.find({})
    data = []
    for response in responses:
        response["_id"] = str(response["_id"])
        data.append(response)
    return list(data)

def get_one(condition):
    response = collection.find_one({"name":condition})
    response["_id"] = str(response["_id"])
    return response

def update(id,data):
    data = dict(data)
    response = collection.update_one({"_id":id},{"$set":data})
    return response.modified_count