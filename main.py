import requests
import pandas as pd
import numpy as np

## Setting URL to MLB stats site

URL = "https://www.baseball-reference.com/leagues/majors/2022.shtml"
page = requests.get(URL)

## Parsing site for 'Team Standard Batting' table and dropping averages row
df_batting = pd.read_html(URL, attrs = {'id': 'teams_standard_batting'})
df_batting=df_batting[0].drop(df_batting[0].index[-3: ])











