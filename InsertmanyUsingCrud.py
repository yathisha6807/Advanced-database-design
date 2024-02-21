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

    # Inserting multiple songs
    new_songs = [
        {
            "title": "Flowers”,
            "artist": “Miley Cyrus“,
            "genre": "Rock",
            "duration_seconds": 354,
            "created_at": datetime.datetime.utcnow()
        },
        {
            "title": “Baby”,
            "artist": "Justin”,
            "genre": "Pop",
            "duration_seconds": 293,
            "created_at": datetime.datetime.utcnow()
        }
    ]

  # Write an expression that inserts the 'new_songs' documents into the 'songs' collection.
    result = songs_collection.insert_many(new_songs)

    song_ids = result.inserted_ids
    pprint(f"IDs of inserted songs: {song_ids}")

except Exception as e:
    print(e)
finally:
    client.close()
