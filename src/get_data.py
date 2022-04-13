import requests
import re
import datetime as dt
from bs4 import BeautifulSoup as bs
import pickle


url = 'https://www.baseball-reference.com/leagues/MLB/2019-schedule.shtml'
resp = requests.get(url)
days = re.findall("<h3>(.*2019)</h3>", resp.text)
dates = [dt.datetime.strptime(d,"%A, %B %d, %Y") for d in days]


game_data = []
for d in dates:
    # get the web page with game data on it
    game_day = d.strftime('%Y-%m-%d')
    url = f'https://www.covers.com/Sports/MLB/Matchups?selectedDate={game_day}'
    resp = requests.get(url)

    # parse the games
    scraped_games = bs(resp.text).findAll('div',{'class':'cmg_matchup_game_box'})
    for g in scraped_games:
        game = {}
        game['home_moneyline'] = g['data-game-odd']
        game['date'] = g['data-game-date']
        try:
            game['home_score'] =g.find('div',{'class':'cmg_matchup_list_score_home'}).text.strip()
            game['away_score'] =g.find('div',{'class':'cmg_matchup_list_score_away'}).text.strip()
        except:
            game['home_score'] =''
            game['away_score'] =''

        game_data.append(game)
        if len(game_data) % 500==0:
            #show progress
            print(dt.datetime.now(), game_day, len(game_data))


pickle.dump(game_data, open('covers_data.pkl','wb'))