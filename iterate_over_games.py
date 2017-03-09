import json
import pandas as pd
import urllib.request

fp = urllib.request.urlopen("https://trackobot.com/profile/history.json?username=still-gnoll-6604&token=ekojyJx_c68FJpkVfavn")
mybytes = fp.read()

mystr = mybytes.decode("utf8")
fp.close()


#print(config)

#Read in file
#data = open('Data/pg4.json').read()

#Decode json
config = json.loads(mystr)

#game = config['history'][0]['card_history']
#game = pd.DataFrame(game)

counter = 0
for i in range(len(config['history'])):
    if i == 0:
        game = config['history'][counter]['card_history']
        #gamerank = config['history'][counter]['rank']
        gameresult = config['history'][counter]['result']
        gamemode = config['history'][counter]['mode']
        gameid = config['history'][counter]['id']
        gamecoin = config['history'][counter]['coin']
        gameduration = config['history'][counter]['duration']
        gameopponent = config['history'][counter]['opponent']
        gamehero = config['history'][counter]['hero']
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
        game['opponent'] = gameopponent
        game['hero'] = gamehero

       # game['rank'] = gamerank

        counter = counter + 1
    elif not config['history'][counter]['card_history']:
                counter = counter + 1

    else:
        game1 = config['history'][counter]['card_history']
       # gamerank = config['history'][counter]['rank']
        gameresult = config['history'][counter]['result']
        gamemode = config['history'][counter]['mode']
        gameid = config['history'][counter]['id']
        gamecoin = config['history'][counter]['coin']
        gameduration = config['history'][counter]['duration']
        gameopponent = config['history'][counter]['opponent']
        gamehero = config['history'][counter]['hero']
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
        game['opponent'] = gameopponent
        game['hero'] = gamehero
       # game1['rank'] = gamerank

        counter = counter + 1
        game = game.append(game1)

print(game)
game['name'] = game['name'].str.replace(',', '')
game.to_csv('Data/hs_alytic_v2.csv', sep='\t', encoding='utf-8')
#bigdata = game1df.append(game2df, ignore_index=True)
