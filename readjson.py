import json
import pandas as pd
#from flatten_json import flatten


#Read in file
data = open('Data/hs24022017.json').read()
#print (data)

#Decode json
config = json.loads(data)

#Create a table of game 1
game1 = config['history'][0]['card_history']
game1turn1 = game1[0]
cardsgame1turn1 = game1turn1['card']
#print(type(cardsgame1turn1))

pd.DataFrame(cardsgame1turn1.items(), columns=['id', 'mana', 'name'])

#pd.DataFrame(game1turn1['card'].items(), columns=['id', 'mana'])


#access my first game
#print(config['history'][0])

#list_for_table = []

#access my first game result
#print(config['history'][0]['id'])

#for element in config['history']:
#    print (element)

#for element in config['history']:

#    list_for_table.append(element)
#print(list_for_table)

#'meta' in config
#print(config)
#print(config['meta'])
#print(config['history'])