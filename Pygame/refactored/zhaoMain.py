'''
Name: Kevin Zhao
File: zhaoMain.py
Date: 04/21/2024

Purpose: Create the main runner file for a game in which the player
		 must dodge falling blocks that become faster over time

'''

import sys
import pygame
from zhaoPlayer import HumanPlayer
from zhaoScreen import Screen
from zhaoGame import Game

def play_game(screen, player, game):
	
	game_over = False
	
    # Run game until game over
	while not game_over:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:           # Track quit event
				sys.exit()

			if event.type == pygame.KEYDOWN:        # Track keyboard event
				
                # Move player left and right with arrow keys (must stay on screen)
				if event.key == pygame.K_LEFT and player.x > 0:
					player.x -= player.size
				elif event.key == pygame.K_RIGHT and player.x < (screen.width - player.size):
					player.x += player.size

        # Drop falling enemies and update score and speed
		game.drop_enemies(screen.width)
		game.update_enemy_positions(screen.height)
		game.set_level()

		# Update screen
		screen.update_screen(game.enemy_list, player, game.score)

        # End game and exit loop upon collision
		if game.collision_check(player):
			game_over = True
			break

if __name__ == "__main__":
	
    # Initialize Pygame
	pygame.init()

	# Initialize necessary classes
	screen = Screen()
	player = HumanPlayer(screen.width/2, screen.height-100)
	game = Game()

	play_game(screen, player, game)