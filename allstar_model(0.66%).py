# @title importing
import requests
import pandas as pd
import sklearn
season_id = '2023-24'
per_mode = 'Totals'
player_info_url = 'https://stats.nba.com/stats/leaguedashplayerstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&ISTRound=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode='+per_mode+'&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season='+season_id+'&SeasonSegment=&SeasonType=Regular%20Season&ShotClockRange=&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight='
headers  = {
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/plain, */*',
    'x-nba-stats-token': 'true',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    'x-nba-stats-origin': 'stats',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Referer': 'https://stats.nba.com/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
}
response = requests.get(url=player_info_url, headers=headers).json()
player_info = response['resultSets'][0]['rowSet']

columns_list = [
        #season_id=season_id
        'player_id',
        'player_name',
        'nickname',
        'team_id',
        'team_abbreviation',
        'age',
        'gp',
        'w',
        'l',
        'w_pct',
        'min',
        'fgm',
        'fga',
        'fg_pct',
        'fg3m',
        'fg3a',
        'fg3_pct',
        'ftm',
        'fta',
        'ft_pct',
        'oreb',
        'dreb',
        'reb',
        'ast',
        'tov',
        'stl',
        'blk',
        'blka',
        'pf',
        'pfd',
        'pts',
        'plus_minus',
        'nba_fantasy_pts',
        'dd2',
        'td3',
        'gp_rank',
        'w_rank',
        'l_rank',
        'w_pct_rank',
        'min_rank',
        'fgm_rank',
        'fga_rank',
        'fg_pct_rank',
        'fg3m_rank',
        'fg3a_rank',
        'fg3_pct_rank',
        'ftm_rank',
        'fta_rank',
        'ft_pct_rank',
        'oreb_rank',
        'dreb_rank',
        'reb_rank',
        'ast_rank',
        'tov_rank',
        'stl_rank',
        'blk_rank',
        'blka_rank',
        'pf_rank',
        'pfd_rank',
        'pts_rank',
        'plus_minus_rank',
        'nba_fantasy_pts_rank',
        'dd2_rank',
        'td3_rank',
        'cfid',
        'cfparams',
]
nba_df = pd.DataFrame(player_info, columns = columns_list)

nba_df.sample(10)

nba_df.to_csv('player_general_traditional_2023-24.csv', index=False)



# @title 2023-24 csv generation
new = pd.read_csv('player_general_traditional_2023-24.csv', usecols=lambda x: x not in ["player_name", "nickname", "team_id", "team_abbreviation"])
new['allstar'] = 0

allstar_ids = [2544, 1629029, 201142, 1628983, 203999, 1626164, 201939, 203076, 1630162, 202331, 202695, 1626157,
               1628389, 203507, 1630169, 203081, 1628369, 1631094, 1627759, 1628973, 1630178, 1628378, 203944, 203954]
for player_id in allstar_ids:
  new.loc[new['player_id'] == player_id, 'allstar'] = 1

new = new.drop("player_id", axis='columns')



# @title Logistic Regression Model
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# LOGISTIC REGRESSION

X = new.drop(['allstar'], axis=1)
y = new['allstar']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression(max_iter = 1000)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
#print("Accuracy:", accuracy)

# accuracy around 99%

# @title 2022-23 Season CSV Generation
season_id = '2022-23'
per_mode = 'Totals'
player_info_url = 'https://stats.nba.com/stats/leaguedashplayerstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&ISTRound=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode='+per_mode+'&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season='+season_id+'&SeasonSegment=&SeasonType=Regular%20Season&ShotClockRange=&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight='
headers  = {
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/plain, */*',
    'x-nba-stats-token': 'true',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    'x-nba-stats-origin': 'stats',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Referer': 'https://stats.nba.com/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
}
response = requests.get(url=player_info_url, headers=headers).json()
player_info = response['resultSets'][0]['rowSet']

columns_list = [
        #season_id=season_id
        'player_id',
        'player_name',
        'nickname',
        'team_id',
        'team_abbreviation',
        'age',
        'gp',
        'w',
        'l',
        'w_pct',
        'min',
        'fgm',
        'fga',
        'fg_pct',
        'fg3m',
        'fg3a',
        'fg3_pct',
        'ftm',
        'fta',
        'ft_pct',
        'oreb',
        'dreb',
        'reb',
        'ast',
        'tov',
        'stl',
        'blk',
        'blka',
        'pf',
        'pfd',
        'pts',
        'plus_minus',
        'nba_fantasy_pts',
        'dd2',
        'td3',
        'gp_rank',
        'w_rank',
        'l_rank',
        'w_pct_rank',
        'min_rank',
        'fgm_rank',
        'fga_rank',
        'fg_pct_rank',
        'fg3m_rank',
        'fg3a_rank',
        'fg3_pct_rank',
        'ftm_rank',
        'fta_rank',
        'ft_pct_rank',
        'oreb_rank',
        'dreb_rank',
        'reb_rank',
        'ast_rank',
        'tov_rank',
        'stl_rank',
        'blk_rank',
        'blka_rank',
        'pf_rank',
        'pfd_rank',
        'pts_rank',
        'plus_minus_rank',
        'nba_fantasy_pts_rank',
        'dd2_rank',
        'td3_rank',
        'cfid',
        'cfparams',
]
nba_df = pd.DataFrame(player_info, columns = columns_list)

nba_df.sample(10)

nba_df.to_csv('player_general_traditional_2022-23.csv', index=False)
nba_df.sample(10)

# @title Testing My Model on 2022-23 Dataset
unseen_data = pd.read_csv('player_general_traditional_2022-23.csv', usecols=lambda x: x not in ["player_name", "nickname", "team_id", "team_abbreviation"])
unseen_data['allstar'] = 0

allstar_ids = [2544, 1629029, 203954, 202681, 203999, 1627759, 202331, 1630169, 1628991, 203944, 201939, 1629627,
               203507, 1628374, 1628378, 1629630, 1628369, 1628389, 1628983, 201942, 201950, 203081, 1627734, 201142]
for player_id in allstar_ids:
  unseen_data.loc[unseen_data['player_id'] == player_id, 'allstar'] = 1

unseen_data = unseen_data.drop("player_id", axis='columns')



X_unseen = unseen_data.drop(['allstar'], axis=1)  # Assuming 'player_id' is not a feature

y_pred_unseen = model.predict(X_unseen)

unseen_data['predicted_allstar'] = y_pred_unseen

pd.options.display.max_columns = None
pd.options.display.max_rows = None

differences = int((unseen_data['allstar'] != unseen_data['predicted_allstar']).sum() / 2)

print("Number of differences between 'allstar' and 'predicted_allstar':", differences, "\n")
differences_df = unseen_data[unseen_data['allstar'] != unseen_data['predicted_allstar']]

num_rows = differences_df.shape[0]
print("My accuracy of this specific run was: ", num_rows/(num_rows+differences))

#print("IDs of players where 'allstar' and 'predicted_allstar' values differ:")
#print(differences_df['player_id'])

#unseen_data.head(1000)

differences_df = unseen_data[unseen_data['allstar'] != unseen_data['predicted_allstar']]
same_df = unseen_data[(unseen_data['allstar'] == 1) & (unseen_data['predicted_allstar'] == 1)]


# Print the first few rows of the filtered DataFrame
print("Rows where 'allstar' and 'predicted_allstar' values are the same:")
#print(same_df.to_string(index=False, max_rows=100))  # Adjust max_rows as needed
print(same_df.head(100))

# @title Print Differences in Model

print("Rows where 'allstar' and 'predicted_allstar' values differ:")
print(differences_df.head(100))