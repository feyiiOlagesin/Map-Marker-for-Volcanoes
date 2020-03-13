# importing the various packages/libraries needed for the program
import folium as fl
import pandas as pd

#read the volcanoe data from the txt file using pandas
volcanoes_data = pd.read_csv("Volcanoes-USA.txt")

#create an object of the Map
map = fl.Map(location = [48.082, -121.6233], zoom_start = 4, tiles = 'Stamen Terrain')


#loop through and assign the values in the data set to the object of map and assign markers
for latitude,longitude,name in zip(volcanoes_data["LAT"], volcanoes_data["LON"], volcanoes_data["NAME"]):
    map.add_child(fl.Marker(location=[latitude, longitude], popup=name, color = "red"))




map.save(outfile = 'test.html')