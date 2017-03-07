# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 10:34:56 2017

@author: angusurquhart
"""

import json
import pandas as pd

#Read in file
data = open('Data/pg4.json').read()

#Decode json
config = json.loads(data)
counter = 0
game = config['history'][counter]['card_history']

#if game.empty():
#    print ('Empty')
#else:
#    print (game)



#if not game:
#  print("List is empty")
#else: 
#    print (game)