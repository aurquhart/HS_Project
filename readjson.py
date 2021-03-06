import json
import pandas as pd
#from flatten_json import flatten


#Read in file
data = open('Data/hs24022017.json').read()
#print (data)

#Decode json
config = json.loads(data)

x = 0

for i in range(len(sequence)):
    # work with index i

#Create a list from the json of game1 only
game1 = config['history'][0]['card_history']
game1rank = config['history'][0]['rank']
game1result = config['history'][0]['result']
game1mode = config['history'][0]['mode']
game1id = config['history'][0]['id']
game1coin = config['history'][0]['coin']
game1duration = config['history'][0]['duration']

#convert list to dataframe
game1df = pd.DataFrame(game1)

#break out the dict that is one of the fields in the dataframe
game1df = pd.concat([game1df, game1df['card'].apply(pd.Series)], axis=1)
#delete the original dict field
del game1df['card']

game1df['duration'] = game1duration
game1df['coin'] = game1coin
game1df['gameid'] = game1id
game1df['mode'] = game1mode
game1df['result'] = game1result
game1df['rank'] = game1rank


print(game1df)

#game1df2 = pd.DataFrame([game1df]['card'], columns=['id', 'cost', 'name'])

#print(game1df2)

#game1turn1 = game1[0]
#cardsgame1turn1 = game1turn1['card']
#print(type(cardsgame1turn1))


#print(game1df)

#game1andmoreturn1 = game1[0]



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