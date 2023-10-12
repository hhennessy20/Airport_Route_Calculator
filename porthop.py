import os
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import pandas as pd
from math import sin, cos, acos, radians
from algo import astar, airport_to_path


class Porthop:
    def __init__(self, airports, routes, start, dest):
        self.airports = airports
        self.routes = routes
        self.start = start
        self.dest = dest

    def successors(self, start_port):
        pos_routes = self.routes[self.routes["Source airport"] == start_port]
        return pos_routes['Destination airport']

    def dest_check(self, start_port, dest_port):
        pos_routes = self.routes[self.routes["Source airport"] == start_port]
        end = pos_routes['Destination airport']
        for i, row in end.iteritems():
            if row == dest_port:
                return True
        return False

    def heuristic(self, src):
        scr_routes = self.routes[self.routes["Source airport"] == src]
        scr_routes = scr_routes["Source airport"]

        start_lat = find_coords(scr_routes, "Latitude")
        start_lon = find_coords(scr_routes, "Longitude")
        end_lat = find_coords(self.dest, "Latitude")
        end_lon = find_coords(self.dest, "Longitude")

        start_lat, start_lon, end_lat, end_lon = float(start_lat[0]), \
            float(start_lon[0]), float(end_lat[0]), float(end_lon[0])
        start_lat, start_lon, end_lat, end_lon = \
            map(radians, [start_lat, start_lon, end_lat, end_lon])
        return acos(sin(start_lat) * sin(end_lat) + cos(start_lat) *
                    cos(end_lat) * cos(end_lon - start_lon)) * 3958.756

    def cost(self, src, end):
        # Theres gotta be a more efficient way to do this
        # the IATA IDs are passed as args, so can you just lookup the
        # corresponding lat/longs?
        src_routes = self.routes[self.routes["Source airport"] == src]
        end_routes = self.routes[self.routes["Source airport"] == end]
        src_routes = src_routes["Source airport"]
        end_routes = end_routes["Source airport"]

        start_lat = find_coords(src_routes, "Latitude")
        start_lon = find_coords(src_routes, "Longitude")
        end_lat = find_coords(end_routes, "Latitude")
        end_lon = find_coords(end_routes, "Longitude")

        start_lat, start_lon, end_lat, end_lon = float(start_lat[0]), \
            float(start_lon[0]), float(end_lat[0]), float(end_lon[0])
        start_lat, start_lon, end_lat, end_lon = \
            map(radians, [start_lat, start_lon, end_lat, end_lon])
        return acos(sin(start_lat) * sin(end_lat) + cos(start_lat) *
                    cos(end_lat) * cos(end_lon - start_lon)) * 3958.756

    def goal_test(self, test_port):
        return test_port == self.dest[0]


# stores the contents of the csv files into these vars
airports = pd.read_csv("airports_old.csv",
                names=["ID", "Name", "City", "Country", "IATA", "ICAO",
                "Latitude", "Longitude", "Altitude", "Timezone", "DST",
                "Tz",  "Type", "Source"])
routes = pd.read_csv("routes.csv",
                     names=["Airline"
                            "Airline ID", "Source airport",
                            "Source airport ID",
                            "Destination airport",
                            "Destination airport ID", "Codeshare",
                            "Stops", "Equipment"])


def find_coords(col, lat_or_lon):
    new_col = []
    for i, row in col.iteritems():
        cols = (airports[airports['IATA'] == row])
        val = cols[lat_or_lon].iloc[0]
        new_col.append(val)
    return new_col


# generic function that just holds important code to get basic things working
# this code should and probably will be moved to other functions later on
def start():
    # Rewrite for user input
    start_port = "BTV"
    dest_port = "JFK"

    # finds all outgoing routes from starting airport
    pos_routes = routes[routes["Source airport"] == start_port]
    dest_grab = routes[routes["Source airport"] == dest_port]

    # gives you the source and end airport IATA ID
    # src and end are for point A-B routes, dest is info for the goal destination
    src = pos_routes['Source airport']
    end = pos_routes['Destination airport']
    dest = dest_grab['Source airport']


    port_search = Porthop(airports, routes, src, dest)

    #print(port_search.successors(start_port))
    #print(port_search.dest_check(start_port, dest_port))
    #print(port_search.heuristic(start_port))
    #print(port_search.cost("BTV", "ATL"))

    longitudes = airports["Longitude"].tolist()
    latitudes = airports["Latitude"].tolist()

    latitudes.pop(0)
    longitudes.pop(0)

    fig, ax = plt.subplots(figsize=(20, 15))
    plt.title("Airports Around the World")

    #print(longitudes)

    route = astar(start_port, port_search.goal_test, port_search.successors,
                  port_search.heuristic, port_search.cost)
    path = airport_to_path(route)


    lats = []
    lons = []
    for stop in path:
        cols = (airports[airports['IATA'] == stop])
        lat = cols["Latitude"].iloc[0]
        lon = cols["Longitude"].iloc[0]
        lats.append(lat)
        lons.append(lon)

    print(lats)
    print(lons)

    plt.scatter(longitudes, latitudes, s=1)
    plt.plot(lons, lats, color = "orange")
    plt.show()


if __name__ == "__main__":
    start()
