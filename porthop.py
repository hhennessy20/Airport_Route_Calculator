import os
#os.environ['PROJ_LIB'] = r'C:\Users\Isaac\anaconda3\pkgs\proj4-5.2.0-hc56fc5f_1\Library\share'
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import pandas as pd

# stores the contents of the csv files into these vars
airports = pd.read_csv("airports.csv",
                       names=["Name", "City", "Country", "IATA", "ICAO",
                              "Latitude", "Longitude", "Altitude", "Timezone",
                              "DST", "Timezone"])
routes = pd.read_csv("routes.csv",
                     names=["Airline ID", "Source airport",
                            "Source airport ID",
                            "Destination airport",
                            "Destination airport ID", "Codeshare",
                            "Stops", "Equipment"])

#give it a list of
def find_coords(col, lat_or_lon):
    newCol = []
    for i, row in col.iteritems():
        cols = (airports[airports['IATA']==row])
        val = cols[lat_or_lon].iloc[0]
        newCol.append(val)
    return newCol

# start port must be the airport IATA ID
# returns list of IATA ID that can be sent to find_coords function
def successors(start_port):
    pos_routes = routes[routes["Source airport"] == start_port]
    return (pos_routes['Destination airport'])

# checks to see if the destination airport is available to a given starting airport
def dest_check(start_port, dest_port):
    pos_routes = routes[routes["Source airport"] == start_port]
    end = pos_routes['Destination airport']
    for i, row in end.iteritems():
        if row == dest_port:
            return True
    return False

# generic function that just holds important code to get basic things working
# this code should and probably will be moved to other functions later on
def start():
    # Rewrite for user input
    start_port = "BTV"
    dest_port = "ATL"

    # finds all outgoing routes from starting airport
    pos_routes = routes[routes["Source airport"] == start_port]
    dest_grab = routes[routes["Source airport"] == dest_port]

    # gives you the source and end airport IATA ID
    # src and end are for point A-B routes, dest is info for the goal destination
    src = pos_routes['Source airport']
    end = pos_routes['Destination airport']
    dest = dest_grab['Source airport']


    lat = find_coords(src, "Latitude"), find_coords(end, "Latitude")
    lon = find_coords(src, "Longitude"), find_coords(end, "Longitude")

    # [0] gives you the source coords, [1] is end coords
    # becasue of how this works it will print the source coord for however many
    # routes there are so theres a lot of duplication, can be ignored with lat/lon[0][0]
    print(lat[1])
    print(lon[1])

    # coords of the final destination for the heuristic measurments
    end_lat = find_coords(dest, "Latitude")
    end_lon = find_coords(dest, "Longitude")

    print(end_lat[0])
    print(end_lon[0])

    print(successors(start_port))
    print(dest_check(start_port, dest_port))


if __name__ == "__main__":
    start()
