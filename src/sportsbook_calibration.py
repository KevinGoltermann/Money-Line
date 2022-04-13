from sklearn.metrics import accuracy_score
import pickle


with open("./data/covers_data.pkl", "rb") as f:
    game_data = pickle.load(f)

# the actual outcome of the game, true if the the home team won
outcomes = []
# predictions derived from moneyline odds. True if the home team was the favorite
predictions = []
# probability the home team will win, derived from moneyline odds
probabilities = []

for d in game_data:
    try:
        moneyline = int(d['home_moneyline'])
        home_score = int(d['home_score'])
        away_score = int(d['away_score'])
    except:
        #incomplete data
        continue
    if moneyline==100:
        # it's rare to have a tossup since covers is averaging the odds from several sports books
        # but we'll exclude them from our calculations
        continue

    # convert moneyline odds ot their implied probabilities
    if moneyline<0:
        probabilities.append(-moneyline/(-moneyline + 100))
    elif moneyline>100:
        probabilities.append(100/(moneyline + 100))

    outcomes.append(home_score>away_score)
    predictions.append(moneyline<0)


pickle.dump((outcomes,predictions, probabilities), open('./data/baseline.pkl','wb'))