import os
os.environ['PROJ_LIB'] = r'C:\Users\Isaac\anaconda3\pkgs\proj4-5.2.0-hc56fc5f_1\Library\share'
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import pandas as pd

airports = pd.read_csv("airports.csv",
                names=["ID", "Name", "City", "Country", "IATA", "ICAO",
                "Latitude", "Longitude", "Altitude", "Timezone", "DST",
                "Tz",  "Type", "Source"])
routes = pd.read_csv("routes.csv",
                names=["Airline ID", "Source airport", "Source airport ID",
                "Destination airport",  "Destination airport ID", "Codeshare",
                "Stops", "Equipment"])
longitudes = airports["Longitude"].tolist()
latitudes = airports["Latitude"].tolist()
fig, ax = plt.subplots(figsize=(15,20))
plt.title("Airports Around the World")
m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80,
            llcrnrlon=-180, urcrnrlon=180)

routes_sfo = routes[routes["Source airport"]=="SFO"]
src = routes_sfo['Source airport']
end = routes_sfo['Destination airport']

def find_coords(col, lat_or_lon):
    newCol = []
    for i, row in col.iteritems():
        cols = (airports[airports['IATA']==row])
        val = cols[lat_or_lon].iloc[0]
        newCol.append(val)
    return newCol
# routes_sfo.loc[:,'src_lat'] = find_coords(src, "Latitude")
# routes_sfo.loc[:,'src_lon'] = find_coords(src, "Longitude")
# routes_sfo.loc[:,'end_lat'] = find_coords(end, "Latitude")
# routes_sfo.loc[:,'end_lon'] = find_coords(end, "Longitude")

lat = find_coords(src, "Latitude"), find_coords(end, "Latitude")
lon = find_coords(src, "Longitude"), find_coords(end, "Longitude")

#print(source[0],dest[0])

# print("thing1")
# print (longitudes)
# print("\n\n\n")
# print("thing2")
# print (source)

#x, y = m(longitudes, latitudes)
x, y = m(lon[1], lat[1])

start_x, end_x = lon

#print(end_x)

plt.scatter(longitudes, latitudes,s=1)
plt.scatter(lon[1], lat[1],s=1,)
for route in enumerate(lon[0]):
    plt.plot((lon[0][0], lon[1][route[0]]), (lat[0][0], lat[1][route[0]]))
#m.drawcoastlines()
plt.show()