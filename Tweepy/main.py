import tweepyModule
from datetime import datetime
import urllib2
import urllib
import json
import os
import instagram
import mongooDB

# Busca tweets con el Hashtag #Tweepy y son almacenados en la base de datos
tweepyModule.search_by_text("#NecesitoDinero")


def ajaxRequest(url=None):
	"""
	Makes an ajax get request.
	url - endpoint(string)
	"""
	req = urllib2.Request(url)
	f = urllib2.urlopen(req)
	response = f.read()
	f.close()
	return response

access_token = os.getenv("473150523.2b8e0fe.8e85e2e4b9764ee893da3e71360e4082")

# ask for hashtag name
hashtag = "#Dinero"

# url to query for pictures
nextUrl = "https://api.instagram.com/v1/tags/"+hashtag+"/media/recent?access_token="+access_token
print "Cargo"
print nextUrl
# while there is a next url to go to
while nextUrl:
	# request the data at that endpoint
	instagramJSON = ajaxRequest(nextUrl)
	instagramDict = json.loads(instagramJSON)
	# get new  nextUrl
	nextUrl = instagramDict["pagination"]["next_url"]
	instagramData = instagramDict["data"]
	# for every picture
	for picDict in instagramData:
		# get the image url and current time
		print picDict
		image = picDict["images"]["standard_resolution"]
		imageUrl = image["url"]
		coordinates = location.point
		print image
		print coordinates
		time = str(datetime.now())
		# download the photo and save it
		urllib.urlretrieve(imageUrl, time+".jpg")

		success = mongooDB.insert_insta(instagramData, text)