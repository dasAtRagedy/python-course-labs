import pymongo
import json
import time

"""Naudodamiesi išskirtinai Pythonu (MongoDB valdymo sistemą galima instaliuoti iš https://www.mongodb.com):
Sukurkite restoranų duomenų rinkinį (pridedamas zip failas)
Parašykite užklausą atvaizduojančią visus dokumentus iš restoranų rinkinio
Parašykite užklausą, kuri atvaizduotų laukus - restaurant_id, name, borough ir cuisine - visiems dokumentams
Parašykite užklausą, kuri atvaizduotų laukus - restaurant_id, name, borough ir cuisine -, bet nerodytų lauko _id visiems dokumentams
Parašykite užklausą, kuri parodytų visus miestelio Bronx restoranus
Parašykite užklausą, kuri parodytų restoranus su įvertinimu tarp 80 ir 100 (duomenis gali reikėti agreguoti).
Parašykite užklausą, kad cuisine būtų išdėstyta didėjimo tvarka, o borough - mažėjimo.
"""

# 1.
def db_init_populate():
    with open('./restaurants.json', 'r') as f:
        collection.delete_many({})
        for line in f.readlines():
            print(line)
            d = json.loads(line)
            d['_id'] = d.pop('restaurant_id')
            collection.insert_one(d)
        # print(d)

client = pymongo.MongoClient('localhost', 27017)
db = client['restaurant_database']
collection = db['restaurants']
# db_init_populate()

# 2.
all_objects = list(collection.find({}))
print(all_objects[0])

# 3.
print(list(collection.find({}, {"name": 1, "borough": 1, "cuisine": 1}))[0])

# 4.
print(list(collection.find({}, {"_id": 0, "name": 1, "borough": 1, "cuisine": 1}))[0])

# 5.
print(list(collection.find({"borough": "Bronx"}))[0])

# 6.
aggregator = [
    {
        "$unwind": "$grades"
    },
    {
        "$group": {
            "_id": "$_id",
            "name": {"$first": "$name"},
            "total_score": {"$sum": "$grades.score"}
        }
    },
    {
        "$match": {
            "total_score": {
                "$gte": 80,
                "$lte": 100
            }
        }
    }
]
print(list(collection.aggregate(aggregator))[0])

# 7.
print(list(collection.find().sort([("cuisine", 1), ("borough", -1)]))[0])

print("done")
time.sleep(3)