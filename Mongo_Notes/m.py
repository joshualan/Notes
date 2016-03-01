import pymongo

# Create a client that runs against the mongod service
# that lets you access mongodb
client = pymongo.MongoClient('localhost', 27017)

# Get our RideTime db
database = client['RideTime']

# Get the users collection from the RideTime db
#users = database['users']
    
user = { "user": ["Alan", "Allen", "Allan"],
           "origin": "322 Western Ave, Cambridge MA 02139",
           "desintation": "14 Oak Park Dr, Bedford MA 01730"
}

id = database['users'].insert(user)

print id
print database.collection_names()

