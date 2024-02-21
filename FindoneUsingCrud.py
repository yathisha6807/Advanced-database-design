from pymongo import MongoClient
from pymongo.server_api import ServerApi
from pprint import pprint

# Define the MongoDB connection URI
uri = "mongodb+srv://yathishaag:Vinnie$27082001@cluster0.2z6l7np.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    # Send a ping to confirm a successful connection
    client.admin.command('ping')

    # Get reference to 'music_platform' database
    db = client.music_platform

    # Get reference to 'songs' collection
    songs_collection = db.songs

    # Find a single document in the 'songs' collection (you can customize the filter criteria)
    query = {"title": “Flowers”}
    song = songs_collection.find_one(query)

    # Print the found document
    pprint(song)

except Exception as e:
    print(e)
finally:
    client.close()
