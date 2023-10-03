import pandas as pd

airports = pd.read_csv("airports.csv")
airports = airports.drop(['ICAO', 'Altitude', 'Timezone', 'DST', 'Timezone.1'], axis=1)
routes = pd.read_csv("routes.csv")
routes = routes.drop(routes[routes.Stops > 0].index)
routes = routes.drop(['Source Airport ID', 'Destination Airport ID', 'Codeshare', 'Equipment', 'Stops'], axis=1)
print(airports.sample(10))
print(routes.sample(10))