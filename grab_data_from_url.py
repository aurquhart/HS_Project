



import json
import urllib.request
import pandas as pd

fp = urllib.request.urlopen("https://trackobot.com/profile.json?username=still-gnoll-6604&token=ekojyJx_c68FJpkVfavn")
mybytes = fp.read()

mystr = mybytes.decode("utf8")
fp.close()
#print (mystr)

config = json.loads(mystr)
#print(type(config))
#print(config)


gameid = config['history'][10]['id']
print (gameid)


#counter = 1
#game = config['history'][counter]['card_history']
#game = pd.DataFrame(game)
#print(game)



