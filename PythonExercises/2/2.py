import pymongo

dbClient = pymongo.MongoClient("mongodb://localhost:27017/")

restaurantsDb = dbClient["Restaurants"]
restaurantsCollection = restaurantsDb["Restaurants"]

# 1. Parašykite užklausą atvaizduojančią visus dokumentus iš restoranų rinkinio
cursor = restaurantsCollection.find({})

for document in cursor:
    print(document)

# 2. Parašykite užklausą, kuri atvaizduotų laukus - restaurant_id, name, borough ir cuisine - visiems dokumentams
cursor = restaurantsCollection.find({}, {"restaurant_id": 1, "name": 1, "borough": 1, "cuisine": 1})

for data in cursor:
    print(data)

# 3. Parašykite užklausą, kuri ayvaizduotų laukus - restaurant_id, name, borough ir cuisine -, bet nerodytų lauko field_id visiems dokumentams
cursor = restaurantsCollection.find({}, {"_id": 0, "restaurant_id": 1, "name": 1, "borough": 1, "cuisine": 1})

for data in cursor:
    print(data)

# 4. Parašykite užklausą, kuri parodytų visus miestelio Bronx restoranus
cursor = restaurantsCollection.find({"borough": "Bronx"})

for document in cursor:
    print(document)

# 5. Parašykite užklausą, kuri parodytų restoranus su įvertinimu tarp 80 ir 100.
cursor = restaurantsCollection.find({"grades": {"$elemMatch": {"score": {"$gte": 80, "$lte": 100}}}})

for document in cursor:
    print(document)
