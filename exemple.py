import json
import math
def test_lecture(file:str):
    with open(file, 'r') as f:
        contenu = f.read()
    return len(json.loads(contenu)['elements'])

print(test_lecture("/home/adminetu/Documents/TP_SAE502/osm.json"))

def fonction_add(file:str, id):
    with open(file, 'r') as f:
        contenu = json.loads(f.read())

    for dico in contenu['elements'] :
        if dico["id"] == id:
            return dico
        
print(fonction_add("/home/adminetu/Documents/TP_SAE502/osm.json", 1993724795))

from math import radians, cos, sin, asin, sqrt

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance in kilometers between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles. Determines return value units.
    return c * r

def voisins(donnees, id, dist):
# — un paramètre donnees qui correspondra aux données OSM ;
# — un paramètre id correspondant à un identifiant de boulangerie ;
# — un paramètre dist correspondant à une distance.
    contenu = json.loads(donnees)
    ensemble = set()
    for dico in contenu['elements']:
        if dico["id"] == id : 
            latitude1 = dico["lat"]
            longitude1 = dico["lon"]

    for dico2 in contenu["elements"]:
        if dico2["type"] == "node":
            if haversine(longitude1, latitude1, dico2["lon"], dico2["lat"]) <= dist :
                try: 
                    ensemble.add((dico2["id"], dico2["tags"]["name"]))
                except:
                    ensemble.add((dico2["id"], None))

    return ensemble

with open("/home/adminetu/Documents/TP_SAE502/osm.json", 'r') as f:
    contenu1 = f.read()

print(voisins(contenu1, 1993724795, 55))
