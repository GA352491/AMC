import pandas as pd

#
# df = pd.read_excel('/Users/anishganga/Desktop/amc.xlsx')
from functools import partial
from geopy.geocoders import Nominatim
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="amc", timeout=10)
geocode = partial(geolocator.geocode)

# coordinates = []
# for num in range(0, len(df)):
#     a = dict(df)
#     location = geolocator.geocode(
#         query={'street': a['ADDRESS'][num], 'postalcode': a['ZIPCODE'][num]},
#         addressdetails=True)
#
#     if location is None:
#         b = coordinates.append('false')
#     else:
#         b = (location.latitude, location.longitude)
#         c = coordinates.append(b)
# print(coordinates)
#


df = pd.read_excel('/Users/anishganga/Downloads/archive/Bangalore_venues.xls')
# print(df['address'])
lat = []
long = []
# for address in df['address']:
#     location = geolocator.geocode(
#         query={'street': address},
#         addressdetails=True)
#     if location is None:
#
#         lat.append('False')
#         long.append('False')
#     else:
#         lat.append(location.latitude)
#         long.append(location.longitude)
# df['latitude'] = lat
# df['longitude'] = long
# df.to_excel('/Users/anishganga/PycharmProjects/amc/media/download/download.xlsx')
#
# df['location'] = df['address'].apply(lambda x: geolocator.geocode(x) if x else None)
# print(df['location'])
df = pd.read_excel(open('media/uploaded_files/Bangalore_venues.xls','rb'))
print(df)
