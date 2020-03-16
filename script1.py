# importing the various packages/libraries needed for the program
import folium as fl
import pandas as pd

#read the volcanoe data from the txt file using pandas
volcanoes_data = pd.read_csv("Volcanoes-USA.txt")

#create an object of the Map
#This also signifies the starting position of the map when loaded
map = fl.Map(location = [48.082, -121.6233], zoom_start = 4, tiles = 'Stamen Terrain')

def colorFinder(elev):
    if elev in range(0, 1000):
        color = "green"
    elif elev in range(1000, 3000):
        color = "orange"
    else:
        color = "red"
    return color

#loop through and assign the values in the data set to the object of map and assign markers
for latitude,longitude,name,elevation in zip(volcanoes_data["LAT"], volcanoes_data["LON"], volcanoes_data["NAME"], volcanoes_data["ELEV"]):
    map.add_child(fl.Marker(location=[latitude, longitude], popup=name,color = colorFinder(elevation)))



#save and load the map object into the html file in the same directory
map.save(outfile = 'test.html')