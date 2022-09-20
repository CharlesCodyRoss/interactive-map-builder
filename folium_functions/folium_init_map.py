import folium

from folium_functions.location_latlng import location_search
from folium_functions.location_latlng import my_location



#Create the Initial Folium Map
def create_folium_map(address = "my-address", tiles = "OpenStreetMap", zoom_start = 10, zoom_conrtol = True, scrollWheelZoom=True, width = "100%", height = "100%", position = "relative"):
    """
    Creates an Initial Simple Folium Map and Zooms to Location, the map will display a pin based on the latitutde, longitude
    of a defined location.  A latitude and longitude must be passed in to the function for the map to work.  If latitude and
    longitude not passed in, the function will exit and ask you to enter location.
    
    Options for "address":
        * my-address (current device location)
        * search-address (search for an adress by city and state)
    """
    
    #Find the Latitude and Longitude for the map to center on
    if address == "my-address":
        location = my_location()
        
    if address == 'search-address':
        location = location_search()
    
    
    #Initialize the Map
    my_map = folium.Map(
                    location=location,
                    tiles=tiles, 
                    zoom_start=zoom_start, 
                    zoom_control= True,  
                    scrollWheelZoom=scrollWheelZoom,
                    width=width, 
                    height=height,
                    position = position)
    
    
    #Add the Pin to the Map
    folium.Marker(
    location=location).add_to(my_map)
    
    return my_map