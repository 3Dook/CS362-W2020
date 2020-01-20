# -*- coding: utf-8 -*-
"""
Created on SUN JAN 19, 2020

@author: doandu
"""

#TODO: Unable to import from testUtility below to save space
#1. Unable to import Dominion - tried to .py and lowercase
import Dominion
import random
from collections import defaultdict
import testUtility


#Get player names
player_names = testUtility.getPlayerNames()

#number of curses and victory cards
nV = testUtility.getNumberVictory(player_names)
nC = testUtility.getNumberCurse(player_names)

#Define box
#note to self* passing nV for the victory cards for gardens
box = testUtility.getBoxes(nV)
#set up the layout of the cards
supply_order = testUtility.getSupplyOrder()

#randomize supply and add static cards
supply = testUtility.getSupply(box, player_names, nV, nC)

#initialize the trash
trash = []

#Costruct the Player objects
players = testUtility.getPlayers(player_names)

#Play the game
testUtility.playGame(supply_order, supply, players, trash)
