import json
from flatten_json import flatten


data = open('Data/hs24022017.json').read()
#print (data)


config = json.loads(data)

#access my first game
print(config['history'][0])

list_for_table = []

#access my first game result
#print(config['history'][0]['id'])

#for element in config['history']:
#    print (element)

for element in config['history']:
    list_for_table.append(element)

print(list_for_table)

#'meta' in config
#print(config)
#print(config['meta'])
#print(config['history'])