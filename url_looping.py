# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 07:05:30 2017

@author: angusurquhart
"""

#Figure out how to loop through urls
from collections import defaultdict

import trackopy
user = {"password":'e479deb2e1', 'username':'still-gnoll-6604'}
trackobot = trackopy.Trackobot(user['username'], user['password'])

#d1 = trackobot.history(page=1)
#d2 = trackobot.history(page=2)

#Create list of urls
yourdict = {}
yourlist = []

for x in range(1,8):
    
     yourdict[1] = trackobot.history(page=x)
     yourlist.append(yourdict.copy())
 
print (yourlist[6])


#for x in range (1,11):
#    print('page='+str(x))
    
