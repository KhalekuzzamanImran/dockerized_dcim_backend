from pymongo import MongoClient


# Connection string with username and password
connection_string = f"mongodb://iotbuser:iotb123dd!@18.141.132.184:27017"

# Create a MongoClient instance with the connection string
client = MongoClient(connection_string)

# Access the database
db = client['iotbdb']
print('===db====', db)
# Now you can perform operations on the database
collection = db["test"]
document = {"key": "value"}
collection.insert_one(document)

# List all collections in the database
collections = db.list_collection_names()

# Print the list of collections
for collection in collections:
    print(collection)
# Close the connection when you're done
client.close()
