from pymongo import MongoClient
from pymongo.server_api import ServerApi
import datetime
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

    # Find a song to update (you can use any criteria here)
    song_to_update = {"title": “Flowers”}

    # Define the update operation (updating the genre)
    update_operation = {"$set": {"genre": "Rock/Opera"}}

    # Write an expression that updates one document in the 'songs' collection.
    result = songs_collection.update_one(song_to_update, update_operation)

    # Print information about the update result
    pprint(f"Matched {result.matched_count} document(s) and modified {result.modified_count} document(s).")

except Exception as e:
    print(e)
finally:
    client.close()
