import os
os.environ['PROJ_LIB'] = r'C:\Users\Isaac\anaconda3\pkgs\proj4-5.2.0-hc56fc5f_1\Library\share'
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

fig, ax = plt.subplots(figsize=(12,15))
m = Basemap(width=12000000,height=9000000,projection='lcc',
            resolution=None,lat_1=45.,lat_2=55,lat_0=50,lon_0=-107.)
m.bluemarble()
plt.show()