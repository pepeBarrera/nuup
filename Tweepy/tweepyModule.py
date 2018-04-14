import tweepy
import tweepyConfig
import mongooDB

api = tweepyConfig.api()

def search_by_text( text ):
    #Maximum number of tweets we want to collect
    maxTweets = 1000000
    # Idioma (es)
    lang = "es"

    tweetSuccess = 0
    tweetFailed = 0
    tweetCount = 0

    for tweet in tweepy.Cursor(api.search, q=text, lang=lang).items(maxTweets):

        if tweet.user.location:
            tweetCount += 1
            success = mongooDB.insert_tweet(tweet, text)
            if success == "true":
                print "Tweet Guardado:"
                tweetSuccess += 1
                print '# ',tweetSuccess," > User location:", tweet.user.location,"> HashTag:",text," > Tweet Text:",tweet.text
            else:
                print ""
                print '# ', tweetSuccess, " > User location:", tweet.user.location, "> HashTag:", text, " > Tweet Text:", tweet.text
                tweetFailed += 1

        # Display how many tweets we have collected
    print "Total de tweets almacenados con exito: ",tweetSuccess
    print "Total de tweets fallidos: ", tweetFailed
    print "Total de tweets obtenidos: ", tweetCount
    return