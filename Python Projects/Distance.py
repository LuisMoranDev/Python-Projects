import math
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="distance")



while True:
	try:
		start = geolocator.geocode(input("What is the name of the first city? "))
	except ValueError:
		print("Need to put in a city name")
	else:
		if hasattr(start,'latitude'):
			break
		else:
			print("Please enter proper name of city")

while True:
	try:
		end = geolocator.geocode(input("What is the name of the second city? "))

	except ValueError:
		print("Need to put in a city name")
	else:
		if hasattr(end,'latitude'):
			break
		else:
			print("Please enter proper name of city ")


rad = 6371
lat1 = start.latitude * math.pi / 180.0
lat2 = end.latitude * math.pi / 180.0
dlat = (lat2 - lat1) * math.pi / 180.0
dlon = (end.longitude - start.longitude) * math.pi / 180.0

a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2) * math.sin(dlon/2)

c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

d = round(rad * c)

miles = round(d / 1.609)

print(f"The distance between the two cities is : {miles} Miles")


# print((location.latitude, location.longitude))