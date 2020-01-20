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


#ITERATION TO EXPLORE TEST SCENERIOS GOES HERE
# ATTEMPT TO CHANGE: In any situation where defaultDict fails to initilize, then supply would tecninically be added as below
# Expected Results: This should bug out the program and only display what is passed
# ACTUAL RESULT: The game only display what was passed through the dictionary via the supply2 Parameter.

supply2 = {}
supply2["Copper"]=[Dominion.Copper()]*(60-len(player_names)*7)
supply2["Silver"]=[Dominion.Silver()]*40
supply2["Gold"]=[Dominion.Gold()]*30
supply2["Estate"]=[Dominion.Estate()]*nV
supply2["Duchy"]=[Dominion.Duchy()]*nV
supply2["Province"]=[Dominion.Province()]*nV
supply2["Curse"]=[Dominion.Curse()]*nC

#Play the game
#NOTE TO SELF*** we submited another parameter as supply2 not supply. 
testUtility.playGame(supply_order, supply2, players, trash)
