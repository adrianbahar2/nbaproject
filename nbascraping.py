import requests
import pandas as pd
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

#nba_df.to_csv('player_general_traditional_2020-21.csv', index=False)

season_list = [
    '1996-97',
    '1997-98',
    '1998-99',
    '1999-00',
    '2000-01',
    '2001-02',
    '2002-03',
    '2003-04',
    '2004-05',
    '2005-06',
    '2006-07',
    '2007-08',
    '2008-09',
    '2009-10',
    '2010-11',
    '2011-12',
    '2012-13',
    '2013-14',
    '2014-15',
    '2015-16',
    '2016-17',
    '2017-18',
    '2018-19',
    '2019-20',
    '2020-21',
    '2021-22',
    '2022-23',
    '2023-24'
]

dfs = []

for season_id in season_list:
    player_info_url = 'https://stats.nba.com/stats/leaguedashplayerstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=' + per_mode +'&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=' + season_id + '&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&TwoWay=0&VsConference=&VsDivision=&Weight='
    # json response
    response = requests.get(url=player_info_url, headers=headers).json()
    # pulling just the data we want
    player_info = response['resultSets'][0]['rowSet']
    # looping over data to insert into table
    df = pd.DataFrame(player_info, columns = columns_list)
    df['season_id'] = season_id
    print(season_id)
    dfs.append(df)

final_df = pd.concat(dfs, sort=False)
final_df.count()

season_df = df.loc[df['season_id'] == '2013-14']
players_df = final_df[['player_id', 'player_name']]
players_df.sample(10)
#players_df.to_csv('player_id_player_name.csv', index=False)
