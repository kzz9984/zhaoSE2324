'''
Name: Kevin Zhao
File: zhaoBossLevel.py
Date: 04/22/2024

Purpose: Create a boss level for the game

'''

import sys
import pygame
from zhaoPlayer import HumanPlayer
from zhaoScreen import Screen
from zhaoGame import Game, HardGame, BossGame
from zhaoMain import play_game

if __name__ == "__main__":
	pygame.init()

	screen = Screen(width=1000, height=1000)		# Enlarged screen
	player = HumanPlayer(screen.width/2, screen.height-100)
	game = BossGame()

	play_game(screen, player, game)