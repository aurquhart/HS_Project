import json
import pandas as pd

#Read in file
data = open('Data/hs24022017.json').read()

#Decode json
config = json.loads(data)

#game = config['history'][0]['card_history']
#game = pd.DataFrame(game)

counter = 0
for i in range(len(config['history'])):
    if i == 0:
        game = config['history'][counter]['card_history']
        gamerank = config['history'][counter]['rank']
        gameresult = config['history'][counter]['result']
        gamemode = config['history'][counter]['mode']
        gameid = config['history'][counter]['id']
        gamecoin = config['history'][counter]['coin']
        gameduration = config['history'][counter]['duration']
        game = pd.DataFrame(game)

        # break out the dict that is one of the fields in the dataframe
        game = pd.concat([game, game['card'].apply(pd.Series)], axis=1)
        # delete the original dict field
        del game['card']

        game['duration'] = gameduration
        game['coin'] = gamecoin
        game['gameid'] = gameid
        game['mode'] = gamemode
        game['result'] = gameresult
        game['rank'] = gamerank

        counter = counter + 1
    else:
        game1 = config['history'][counter]['card_history']
        gamerank = config['history'][counter]['rank']
        gameresult = config['history'][counter]['result']
        gamemode = config['history'][counter]['mode']
        gameid = config['history'][counter]['id']
        gamecoin = config['history'][counter]['coin']
        gameduration = config['history'][counter]['duration']
        game1 = pd.DataFrame(game1)
        # break out the dict that is one of the fields in the dataframe
        game1 = pd.concat([game1, game1['card'].apply(pd.Series)], axis=1)
        # delete the original dict field
        del game1['card']

        game1['duration'] = gameduration
        game1['coin'] = gamecoin
        game1['gameid'] = gameid
        game1['mode'] = gamemode
        game1['result'] = gameresult
        game1['rank'] = gamerank

        counter = counter + 1
        game = game.append(game1)

#print(game)
game['name'] = game['name'].str.replace(',', '')
game.to_csv('Data/hs_alytic.csv', sep='\t', encoding='utf-8')
#bigdata = game1df.append(game2df, ignore_index=True)
