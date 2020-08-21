import math

#function to get distance between coordinates
def distBetweenCoords(lat1, lon1, lat2, lon2):
    earthsRadiusKm= 6371.0

    dLat=(lat2-lat1)
    dLon= (lon2-lon1)
    
    lat1 = math.radians(lat1)
    lat2 = math.radians(lat2)

    a = math.sin(dLat/2) * math.sin(dLat/2) + math.sin(dLon/2) * math.sin(dLon/2) * math.cos(lat1) * math.cos(lat2); 
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a)); 

    return (earthsRadiusKm * c)/1.852

print(distBetweenCoords(51.5, 0, 38.8, -77.1))
