import pandas as pd
import numpy as np

def initialize_data():
    #reads in airports and drops unneccessary columns
    airports = pd.read_csv("airports.csv")
    airports = airports.drop(['ICAO', 'Altitude', 'Timezone', 'DST', 'Timezone.1'], axis=1)
    #Gets rid of rows with garbage IATA dodes
    airports = airports.replace('\\N', np.nan)
    airports = airports.dropna()
    #reads in routes and drops unneccessary columns
    routes = pd.read_csv("routes.csv")
    routes = routes.drop(routes[routes.Stops > 0].index)
    routes = routes.drop(['Source Airport ID', 'Destination Airport ID', 'Codeshare', 'Equipment', 'Stops'], axis=1)
    #Gets rid of rows with garbage IATA codes
    routes = routes.replace('\\N', np.nan)
    routes = routes.dropna()

    #Returns cleaned data sets
    return airports, routes
