import requests
from bs4 import BeautifulSoup as bs

game_links = []
for current_year in range(2016,2022):
    url = f"https://www.baseball-reference.com/leagues/MLB/{current_year}-schedule.shtml"
    resp = requests.get(url)
    soup=bs(resp.text)
    games = soup.findAll('a',text='Boxscore')
    game_links.extend([x['href'] for x in games])
print("Number of games to download: ", len(game_links))
print(game_links[0])