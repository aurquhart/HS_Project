# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 07:05:30 2017

@author: angusurquhart
"""

#Figure out how to loop through urls
from collections import defaultdict

import trackopy
import pandas as pd
user = {"password":'e479deb2e1', 'username':'still-gnoll-6604'}
trackobot = trackopy.Trackobot(user['username'], user['password'])

#d1 = trackobot.history(page=1)
#d2 = trackobot.history(page=2)

#Create list of urls
yourdict = {}
list_of_game_dicts = []

for x in range(1,8):

     yourdict[1] = trackobot.history(page=x)
     list_of_game_dicts.append(yourdict.copy())

page_counter = 0
counter = 0

page = list_of_game_dicts[0]
game = game1[1]['history'][counter]['card_history']
game = pd.DataFrame(game)
# break out the dict that is one of the fields in the dataframe
game = pd.concat([game, game['card'].apply(pd.Series)], axis=1)
# delete the original dict field
del game['card']



#These can be used to explore structure of json
#game1.keys()
#game1[1].keys()
#game1[1]['meta']
#game1[1]['history']


print(game)
