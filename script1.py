# importing the various packages/libraries needed for the program
import folium as fl
import pandas as pd


volcanoes_data = pd.read_csv("Volcanoes-USA.txt")

map = fl.Map(location = [48.082, -121.623 3], zoom_start = 4, tiles = 'Stamen Terrain')


for latitude,longitude,name in zip(volcanoes_data["LAT"], volcanoes_data["LON"], volcanoes_data["NAME"]):
    map.add_child(fl.Marker(location=[latitude, longitude], popup=name, color = "red"))




map.save(outfile = 'test.html')