# -*- coding: utf-8 -*-
"""
Created on 20 Dec 2017

@author: angusurquhart
Pull down data from trackobot into json files
"""

#Import packages
import trackopy


#Setup trackobot
user = {"password":'e479deb2e1', 'username':'still-gnoll-6604'}
trackobot = trackopy.Trackobot(user['username'], user['password'])




#count number of pages of data I have
pagecount = trackobot.history(page=1)['meta']['total_pages']+1
pagecount