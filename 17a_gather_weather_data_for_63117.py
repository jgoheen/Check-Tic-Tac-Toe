# use BeautifulSoup and requests libraries to gather weather data for st. louis
from bs4 import BeautifulSoup
import requests

r = requests.get('https://forecast.weather.gov/MapClick.php?lat=38.6278&lon=-90.1996')

soup = BeautifulSoup(r.text, features="html.parser")

for p in soup.find_all("p", class_="myforecast-current"):
  print("Sumary: ", p.string)

for p in soup.find_all("p", class_="myforecast-current-lrg"):
  print("Current temp (F): ", p.string)

for p in soup.find_all("p", class_="myforecast-current-sm"):
  print("Current temp (C): ", p.string)

row = 0
table = soup.find_all('table')[0] #grabs the first table
for row in table.find_all('tr'):
  count = 0
  column = 0
  columns = row.find_all('td')
  for column in columns:
    if count == 0:
      print(column.string + ': ', end='')
    else:
      print(column.string)
    count += 1   