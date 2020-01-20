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
# ATTEMPT TO CHANGE: We redefined the dictionary so that it will act as a Dominion Curse Card; we also reset the card quanity to one
# Expected Results: The Province should change into a curse card and should be counted as a (-1)VP
# ACTUAL RESULT: The Game shows a province card at one, but will not register that there is a province card when the user buys the game. This prevents the players from 
# winning and completing the game once province is bought.
supply["Province"]=[Dominion.Curse()]*1

#Play the game
testUtility.playGame(supply_order, supply, players, trash)
