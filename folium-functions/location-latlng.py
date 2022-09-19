import geocoder
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="geoapiExercises")


#Grab Lat and Long Based on Entry
def location_search():
    
    location = input("Enter City and State")
    
    try:
        city, latlng = geolocator.geocode(location)
        
        lat = latlng[0]
        lng = latlng[1]
        
        return [lat, lng]
        
        
    except:
        
        """
        Location Not Found!
        
        Please Try Entering Your Location Information Again
        
        """
    