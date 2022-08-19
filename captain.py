#imports
import requests
import pandas as pd
import numpy as np
#playeridlist = ['251256', '5225028']
url = 'https://fantasy.premierleague.com/api/entry/251256/event/1/picks/'

#currently works with a hardcoded id, trying to iterate through multiple ids 
#Function to generate url endpoint for api potentially)
#def GetEndpoints():
#    apis = []
#    baseEndpoint = "'https://fantasy.premierleague.com/api/entry/"
#    for i in list['251256', '5225028']:
#        if i == 1 :
#          #print(baseEndpoint)
#          apis.append(baseEndpoint)
#        else:
#            apiEndpoint = baseEndpoint + str(i) + "/event/1/"
#            #print(apiEndpoint)
#            apis.append(apiEndpoint)
#    return apis
#
r = requests.get(url)
json = r.json()
json.keys()
captain_df = pd.DataFrame(json['entry_history'], index=[0])

slim_captain_df = captain_df[['event','points','total_points','bank',
                                'points_on_bench','overall_rank',
                                'event_transfers','event_transfers_cost','value','bank']]

slim_captain_df['playerid'] = 251256
#will need to join with list of players data set to get players name
#get unique player list left join onto captain_df on playerid one to many: player name field
#get data for one particular user hard coded

#get data for one week hardcoded


#get data from multiple users in a list and append into one data set


#get data from mutilple users and all gameweek s(1-38) and appedn to one data table


#apply filter to filter by gameweek or by playerid


print(slim_captain_df)
