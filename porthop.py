import os
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import pandas as pd
from math import sin, cos, acos, radians
from algo import astar, airport_to_path
from initialize_data import initialize_data


class Porthop:
    def __init__(self, airports, routes, start, dest):
        self.airports = airports    # DataFrame containing all airport data
        self.routes = routes        # DataFrame containing all route data
        self.start = start          # Start airport IATA
        self.dest = dest            # Destination airport IATA

    # Returns a list of all outgoing routes from airport passed as arg
    def successors(self, start_port):
        pos_routes = self.routes[self.routes["Source Airport"] == start_port]
        return pos_routes['Destination Airport']
        
    # Finds the euclidean distance between airport passed as arg and
    # destination airport using coordinates
    def heuristic(self, src):
        # Get rows containing desired airports
        src_row = (airports[airports['IATA'] == src])
        end_row = (airports[airports['IATA'] == self.dest])

        # Get coords of each airport
        start_lat = src_row["Latitude"].iloc[0]
        start_lon = src_row["Longitude"].iloc[0]
        end_lat = end_row["Latitude"].iloc[0]
        end_lon = end_row["Longitude"].iloc[0]

        # Calculate Euclidean distance using Spherical Law of Cosines formula
        start_lat, start_lon, end_lat, end_lon = \
            map(radians, [start_lat, start_lon, end_lat, end_lon])
        return acos(sin(start_lat) * sin(end_lat) + cos(start_lat) *
                    cos(end_lat) * cos(end_lon - start_lon)) * 3958.756

    def cost(self, src, end):
        # Get rows containing desired airports
        src_row = (airports[airports['IATA'] == src])
        end_row = (airports[airports['IATA'] == end])

        # Get coords of each airport
        start_lat = src_row["Latitude"].iloc[0]
        start_lon = src_row["Longitude"].iloc[0]
        end_lat = end_row["Latitude"].iloc[0]
        end_lon = end_row["Longitude"].iloc[0]

        # Calculate Euclidean distance using Spherical Law of Cosines formula
        start_lat, start_lon, end_lat, end_lon = \
            map(radians, [start_lat, start_lon, end_lat, end_lon])
        return acos(sin(start_lat) * sin(end_lat) + cos(start_lat) *
                    cos(end_lat) * cos(end_lon - start_lon)) * 3958.756

    # Check if airport passed as arg is the destination
    def goal_test(self, test_port):
        return test_port == self.dest


# Get DataFrames from cleaned csv files
airports, routes = initialize_data()


# Finds coords for entire DataFrame (unused)
def find_coords(col, lat_or_lon):
    new_col = []
    for i, row in col.iteritems():
        cols = (airports[airports['IATA'] == row])
        val = cols[lat_or_lon].iloc[0]
        new_col.append(val)
    return new_col


#Given an IATA code for a starting port and a destination port, returns the most efficient path between them distance-wise
def port_search(start_port, dest_port):

    # finds all outgoing routes from starting airport
    pos_routes = routes[routes["Source Airport"] == start_port]

    # gives you the source and end airport IATA ID
    # src and end are for point A-B routes, dest is info for the goal destination
    src = pos_routes['Source Airport']

    port_search = Porthop(airports, routes, src, dest_port)

    route = astar(start_port, port_search.goal_test, port_search.successors,
                  port_search.heuristic, port_search.cost)
    path = airport_to_path(route)

    return path

#Given a list of IATA codes, plots a path between them on a map
def plot_path(path):
    longitudes = airports["Longitude"].tolist()
    latitudes = airports["Latitude"].tolist()

    latitudes.pop(0)
    longitudes.pop(0)

    fig, ax = plt.subplots(figsize=(20, 15))
    plt.title("Airports Around the World")

    lats = []
    lons = []
    for stop in path:
        cols = (airports[airports['IATA'] == stop])
        lat = cols["Latitude"].iloc[0]
        lon = cols["Longitude"].iloc[0]
        lats.append(lat)
        lons.append(lon)

    plt.scatter(longitudes, latitudes, s=1)
    plt.plot(lons, lats, color="orange", marker='o')
    plt.show()


#given list of IATA codes, returns list of airport names
def list_full_names(path):
    full_names = []
    for port in path:
        full_names.append(airports.loc[airports['IATA'] == port].iloc[0]['Name'])
    return full_names


# # Initial method used to test algorithm
# # Establishes necessary data from dataset, plots airports on globe,
# # and calls astar
# def start(start_port, dest_port):
#
#     # finds all outgoing routes from starting airport
#     pos_routes = routes[routes["Source Airport"] == start_port]
#
#     # gives you the source and end airport IATA ID
#     # src and end are for point A-B routes, dest is info for the goal destination
#     src = pos_routes['Source Airport']
#
#     port_search = Porthop(airports, routes, src, dest_port)
#
#     longitudes = airports["Longitude"].tolist()
#     latitudes = airports["Latitude"].tolist()
#
#     latitudes.pop(0)
#     longitudes.pop(0)
#
#     fig, ax = plt.subplots(figsize=(20, 15))
#     plt.title("Airports Around the World")
#
#     route = astar(start_port, port_search.goal_test, port_search.successors,
#                   port_search.heuristic, port_search.cost)
#     path = airport_to_path(route)
#
#     lats = []
#     lons = []
#     for stop in path:
#         cols = (airports[airports['IATA'] == stop])
#         lat = cols["Latitude"].iloc[0]
#         lon = cols["Longitude"].iloc[0]
#         lats.append(lat)
#         lons.append(lon)
#
#     plt.scatter(longitudes, latitudes, s=1)
#     plt.plot(lons, lats, color = "orange", marker='o')
#     plt.show()
#     return path
#
#
# if __name__ == "__main__":
#     start("BTV", "LNZ")
