# use BeautifulSoup and requests libraries to obtain a list of all 30 mlb baseball teams
from bs4 import BeautifulSoup
import requests

r = requests.get('https://www.lineups.com/mlb/rosters')

soup = BeautifulSoup(r.text, features="html.parser")

teams = []

for link_black in soup.find_all(class_="link-black-underline team-txt"):
    if link_black.text:
        teams.append(link_black.text.strip())
        print(link_black.text.strip())

print("\nNumber of MLB teams: " + str(len(teams)))