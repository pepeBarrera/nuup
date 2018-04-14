import tweepyModule
import mongooDB
from collections import Counter

# Busca tweets con el Hashtag #Tweepy y son almacenados en la base de datos
tweepyModule.search_by_text("#NecesitoVacaciones")

#cursor = mongooDB.get_data_tweet()

#signs = Counter(k['hashTag'] for k in cursor if k.get('hashTag'))
#for sign, count in signs.most_common():
    #print(sign, count)