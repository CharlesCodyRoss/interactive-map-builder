# Interactive Map Builder

This package will allow you to integrate interactive webmaps within python documents with ease, simply follow the 
below steps and call functions to create and add data to interactive web maps hosted by folium.

By using the **create_folium_map()** function you can instantly create a fully interactive folium map that pins your current location.  By passing the argument **address="search-address"** a prompt will allow you to enter an address of your choosing for the map to center on when called.



## Steps

In order to initate use of these packages simply run the below steps in your python environment

    * In your command line, run the following command within the python evironment of your choosing.
      Creating a new virtual environment is stongly recommended before using the package.
        * *pip install -e .*

    * When in python, import the folium map intializer by calling
        * *from folium_functions.folium_init_map import create_folium_map*

    * Call the map by using 
        * *create_folium_map()

    * The function as it is will call the map with a pin located at the devices current location
    
    * To change the map location to an address of your choosing, use
        * *create_colium_map(address="search-address")
    
    * Other variables for the create_folium_map that are alterable are
        *tiles = "OpenStreetMap" 
        * zoom_start = 10, 
        * zoom_conrtol = True
        * scrollWheelZoom=True
        * width = "100%"
        * height = "100%" 
        * position = "relative"