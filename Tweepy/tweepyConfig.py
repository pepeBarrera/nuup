import tweepy

def api():
   consumer_key = "xK7PqXKOkTBqCgV6pWT3LTGjO"
   consumer_secret = "SUQSX1wVkcQNu3iEuvRRdo6zbAHRy5LERiTHtcuD36UDRNKvYx"
   access_token = "779441579152904192-DrR1Oi7KSXit7SZkzI0qUMcQTqOSDEr"
   access_token_secret = "JJZQH6lYSpRXcapogEiAipmg3QhPVtn0u0AN1tL7QGTOC"

   # Creating the authentication object
   auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
   # Setting your access token and secret
   auth.set_access_token(access_token, access_token_secret)
   # Creating the API object while passing in auth information
   api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
   api.rate_limit_status()['resources']['search']

   return api