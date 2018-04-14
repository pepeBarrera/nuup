from pymongo import MongoClient

def MongoDB( url ):
    client = MongoClient(url)

    ## Referencia a la base de datos, si no exite la crea
    db = client['nuupedb']
    return db