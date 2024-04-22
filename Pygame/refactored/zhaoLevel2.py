'''
Name: Kevin Zhao
File: zhaoLevel2.py
Date: 04/22/2024

Purpose: Create a harder second level for the game

'''

import sys
import pygame
from zhaoPlayer import HumanPlayer
from zhaoScreen import Screen
from zhaoGame import Game, HardGame
from zhaoMain import play_game

if __name__ == "__main__":
	pygame.init()

	screen = Screen()
	player = HumanPlayer(screen.width/2, screen.height-100)
	game = HardGame()

	play_game(screen, player, game)