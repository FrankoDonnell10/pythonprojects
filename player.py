import requests
import pandas as pd
from tqdm.auto import tqdm
tqdm.pandas()

url = "https://fantasy.premierleague.com/api/bootstrap-static/"
base_url = "https://fantasy.premierleague.com/api/"


#def get_season_history(player_id):
#    season = requests.get(
#        base_url + 'element-summary/' + str(player_id) + '/'
#    ).json()
#
#    # extract 'history' data from response into dataframe
#    df2 = pd.json_normalize(season['history'])
#    return df2
#
#get_season_history(1)[
#    [
#        'round',
#        'total_points',
#        'minutes',
#        'goals_scored',
#        'assists'
#    ]
#].head(10)


r = requests.get(url)
json = r.json()
json.keys()
#retireving data
players = pd.DataFrame(json['elements'])
teams = pd.DataFrame(json['teams'])
types = pd.DataFrame(json['element_types'])
events = pd.DataFrame(json['events'])

players1 = players[['id', 'first_name', 'second_name', 'web_name', 'team',
     'element_type']]

players1 = players1.merge(
    teams[['id', 'name']],
    left_on='team',
    right_on='id',
    suffixes=['_player', None]
).drop(['team', 'id'], axis=1)

players1 = players1.merge(
    types[['id', 'singular_name_short']],
    left_on='element_type',
    right_on='id'
).drop(['element_type', 'id'], axis=1)

players1.head()

#test after deadline make sure api is active
points = players['id_player'].progress_apply(get_gameweek_history)

# combine results into single dataframe
points = pd.concat(df for df in points)

# join web_name
points = players[['id_player', 'web_name']].merge(
    points,
    left_on='id_player',
    right_on='element'
)

print(players1)





####Alternative Solutions to joining keys######
#combining data from above together
#df = pd.merge(
#    left=players,
#    right=teams,
#    left_on='team',
#    right_on='id'
#)
#
## show joined result
##df = df[['first_name', 'second_name', 'name']].head()
#
#df = df.merge(
#    types,
#    left_on='element_type',
#    right_on='id'
#)
#
## rename columns
#df = df.rename(
#    columns={'name':'team_name', 'singular_name':'position_name'}
#)
#
## show result
#df = df[
#    ['first_name', 'second_name', 'team_name', 'position_name', "id"]
#].head()
