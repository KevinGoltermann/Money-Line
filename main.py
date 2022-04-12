import requests
import pandas as pd
import numpy as np



URL = "https://www.baseball-reference.com/leagues/majors/2022.shtml"
page = requests.get(URL)


df = pd.read_html(URL, attrs = {'id': 'teams_standard_batting'})


df=df[0].drop(df[0].index[-3: ])


df['G'] = pd.to_numeric(df['G'])
df['H'] = pd.to_numeric(df['H'])

df['Add'] = df.G + df.H


print(df)







