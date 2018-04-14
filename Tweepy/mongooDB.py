import mongoDBConfig
import time

db = mongoDBConfig.MongoDB("mongodb://localhost:27017/nuupedb")

# Ingresa un nuevo Tweet
def insert_tweet( tweet, hashtag ):
    # Verifica si exite collection, de no ser asi la crea
    if not db.get_collection("tweets"):
        db.create_collection("tweets")

    result = db.tweets.insert_one(
        {
            "userLocation": tweet.user.location,
            "hashTag": hashtag,
            "tweetText": tweet.text,
            "date": time.strftime("%d/%m/%Y")
        }
    )

    if result.inserted_id:
        return "true"
    else:
        return  "false"

def get_data_tweet():
    collection = db["tweets"]
    cursor = collection.find()
    return cursor