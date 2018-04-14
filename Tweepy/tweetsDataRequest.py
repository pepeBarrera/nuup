from collections import Counter
import sys, json
import mongooDB

# Load the data that PHP sent us
try:
    dataService = sys.argv[1]
    dataState = sys.argv[2]
    #data = sys.argv[1]
except:
    print "ERROR"
    sys.exit(1)

#dataService = "Credito"
#dataState = "CDMX"

cursor = mongooDB.get_data_tweet()

creditArray = ["#Dinero", "#NecesitoVacaciones", "#PorquePobre", "#Desempleado", "#QuieroCasa", "#Debo", "#NecesitoDinero"]
carInsuranceArray = ["#Accidente","#SiTomasNoManejes","#SinLlantas","#RoboAutoPartes"]
healthInsuranceArray = ["#MalditaAlergia","#EnElHospital","#Inseguridad","#MeCai","#QueDolor"]
ar = []
jsonData = []

for tweet in cursor:
    print tweet['userLocation']
    if tweet['userLocation'].find(dataState+",") != -1 or tweet['userLocation'].find(dataState) != -1:
        if dataService == "Credito":
            print tweet['userLocation']," ",tweet['hashTag']
            if tweet['hashTag'] in creditArray:
                ar.append({"Hashtag":tweet['hashTag']})
        elif dataService == "Auto":
            print tweet['userLocation']," ",tweet['hashTag']
            if tweet['hashTag'] in carInsuranceArray:
                ar.append({"Hashtag":tweet['hashTag']})
        else:
            print tweet['userLocation']," ",tweet['hashTag']
            if tweet['hashTag'] in healthInsuranceArray:
                ar.append({"Hashtag":tweet['hashTag']})

signs = Counter(k['Hashtag'] for k in ar if k.get('Hashtag'))
for sign, count in signs.most_common():
    print(sign, count)
    jsonData.append({"Hashtag":sign, "tweets":count})

    result = {
        "dato1":dataService,
        "dato2":dataState
    }

# Send it to stdout (to PHP)
print json.dumps(jsonData)