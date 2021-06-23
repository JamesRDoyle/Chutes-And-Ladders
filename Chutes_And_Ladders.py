# Jamie Doyle
# Week 5, Day 2 REEU
# Chutes & Ladders Game

# Dr. Krogmeier's Code:
# This needs to be included for the random drawing of numbers from
# 1 to 6 simulating the throw of a die.
import random
from random import Random

random.seed(a=None,version=2)

# This dictionary stores the chutes and ladders board.
CandLTable = {1:38, 4:14, 9:31, 16:6, 21:42, 28:84, 36:44, 47:26, 
              49:11, 51:67, 56:53, 63:19, 64:60, 71:91, 80:100, 
              87:24, 93:73, 95:75, 98:78}

# The function to make a move
def CandL_make_a_move(position,CandLTable):
    rand = Random(None)
    roll = rand.randint(1, 6)
    if position + roll > 100:
        return position
    position += roll
    position = CandLTable.get(position, position)
    return position



# My code:

# Method definition to play a single game between n number of players
def Play_a_game(num_players):
    player_has_won = False
    player_list = [0] * num_players  # each player starts at position 0

    while (player_has_won != True): # Play rounds for each player until a winner is found
        for p in range(num_players):
            player_list[p] = CandL_make_a_move(player_list[p], CandLTable) # Make a move
            
            if (player_list[p] == 100): 
                player_has_won = True
                return p+1 # End the function now that a player has won

# Method definition to play x number of games with y number of players
def Play_games(num_players, num_games):
    for x in range(1, 1+num_games): # Play a game and declare a winner each time
        winner = Play_a_game(num_players)
        print("Player " + str(winner) + " has won game " + str(x) + "!!")

# Variables collect user input to dictate how many games should be played with how many numbers
num_players = int(input("How many players are playing? "))
num_games = int(input("How many games will be played? "))

Play_games(num_players, num_games)







