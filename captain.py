#imports
import requests
import pandas as pd
import numpy as np

url = 'https://fantasy.premierleague.com/api/entry/511906/event/1/picks/'

r = requests.get(url)
json = r.json()
json.keys()
captain_df = pd.DataFrame(json['keyname'])

slim_captain_df = captain_df[['entry','event','points','total_points','bank',
                                'points_on_bench','active_chip','overall_rank',
                                'event_transfers','event_transfers_cost', 'element', 'is_captain']]

#will need to join with list of players data set to get players name
#get unique player list left join onto captain_df on playerid one to many: player name field
#get data for one particular user hard coded

#get data for one week hardcoded


#get data from multiple users in a list and append into one data set


#get data from mutilple users and all gameweek s(1-38) and appedn to one data table


#apply filter to filter by gameweek or by playerid
