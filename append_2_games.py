import json
import pandas as pd

#Read in file
data = open('Data/hs24022017.json').read()

#Decode json
config = json.loads(data)



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


#Create a list from the json of game2 only
game1 = config['history'][1]['card_history']
game1rank = config['history'][1]['rank']
game1result = config['history'][1]['result']
game1mode = config['history'][1]['mode']
game1id = config['history'][1]['id']
game1coin = config['history'][1]['coin']
game1duration = config['history'][1]['duration']

#convert list to dataframe
game2df = pd.DataFrame(game1)

#break out the dict that is one of the fields in the dataframe
game2df = pd.concat([game2df, game2df['card'].apply(pd.Series)], axis=1)
#delete the original dict field
del game2df['card']

game2df['duration'] = game1duration
game2df['coin'] = game1coin
game2df['gameid'] = game1id
game2df['mode'] = game1mode
game2df['result'] = game1result
game2df['rank'] = game1rank



#print(game1df.head(5))
#print(game2df.head(5))

bigdata = game1df.append(game2df, ignore_index=True)

print(bigdata)
