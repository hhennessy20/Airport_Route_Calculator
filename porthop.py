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
        

    def heuristic(self, src):
        src_row = (airports[airports['IATA'] == src])
        end_row = (airports[airports['IATA'] == self.dest])
        if src_row.empty or end_row.empty:
            # print("Heuristic")
            # print(src)
            # print(src_row, end_row)
            print("Found empty data frame")
        start_lat = src_row["Latitude"].iloc[0]
        start_lon = src_row["Longitude"].iloc[0]
        end_lat = end_row["Latitude"].iloc[0]
        end_lon = end_row["Longitude"].iloc[0]

        start_lat, start_lon, end_lat, end_lon = float(start_lat), \
            float(start_lon), float(end_lat), float(end_lon)
        start_lat, start_lon, end_lat, end_lon = \
            map(radians, [start_lat, start_lon, end_lat, end_lon])
        return acos(sin(start_lat) * sin(end_lat) + cos(start_lat) *
                    cos(end_lat) * cos(end_lon - start_lon)) * 3958.756

    def cost(self, src, end):
        src_row = (airports[airports['IATA'] == src])
        end_row = (airports[airports['IATA'] == end])
        if src_row.empty or end_row.empty:
            # print("src: " + src, "end: " + end)
            # print("src_row: ", src_row, "end_row: ", end_row)
            print("Found empty data frame")
        start_lat = src_row["Latitude"].iloc[0]
        start_lon = src_row["Longitude"].iloc[0]
        end_lat = end_row["Latitude"].iloc[0]
        end_lon = end_row["Longitude"].iloc[0]

        start_lat, start_lon, end_lat, end_lon = float(start_lat), \
            float(start_lon), float(end_lat), float(end_lon)
        start_lat, start_lon, end_lat, end_lon = \
            map(radians, [start_lat, start_lon, end_lat, end_lon])
        return acos(sin(start_lat) * sin(end_lat) + cos(start_lat) *
                    cos(end_lat) * cos(end_lon - start_lon)) * 3958.756

    
    def goal_test(self, test_port):
        return test_port == self.dest


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


    port_search = Porthop(airports, routes, src, dest_port)

    #print(port_search.successors(start_port))
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
