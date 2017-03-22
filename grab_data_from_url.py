



import json
import urllib.request
import pandas as pd
from collections import defaultdict

import trackopy
user = {"password":'e479deb2e1', 'username':'still-gnoll-6604'}
trackobot = trackopy.Trackobot(user['username'], user['password'])

d1 = trackobot.history(page=1)
d2 = trackobot.history(page=2)

#print (config)




#z = {**config1, **config2}

dd = defaultdict(list)

for d in (d1, d2): # you can list as many input dicts as you want here
    for key, value in d.items():
        dd[key].append(value)

#print(d1)
print(type(d1))
#gameid = dd['history'][10]['id']
#print (gameid)




#user = trackopy.Trackobot.create_user()
#Out[29]: {'password': '92c18bde03', 'username': 'solitary-murloc-scout-1758'}
#KeyError: 'solitary-murloc-scout-1758'


#d = {"password":'e479deb2e1', 'username':'still-gnoll-6604'}

#trackobot = trackopy.Trackobot(d['still-gnoll-6604'], d['e479deb2e1'])
#history = trackobot.history()
#user = trackopy.Trackobot.create_user()
#trackobot = trackopy.Trackobot(user['snowy-gruul-4722'], user['bb24b42b26'])

#fp = urllib.request.urlopen("https://trackobot.com/profile.json?username=still-gnoll-6604&token=ekojyJx_c68FJpkVfavn")

#mybytes = fp.read()
#mystr = mybytes.decode("utf8")
#fp.close()
#print (mystr)

#config = json.loads(mystr)
#print(type(config))
#print(config)


#gameid = config['history'][10]['id']
#print (gameid)


#counter = 1
#game = config['history'][counter]['card_history']
#game = pd.DataFrame(game)
#print(game)



