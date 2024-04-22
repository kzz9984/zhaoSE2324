'''
Name: Kevin Zhao
File: zhaoGame.py
Date: 04/21/2024

Purpose: Create a class to handle all the game logic

'''

import random
from zhaoPlayer import Enemy, LargeEnemy, KeithEnemy

# Normal game mode
class Game:

	# Set to normal enemy
	Enemy = Enemy	

	# Initialize game stats and settings
	def __init__(self, speed=10, score=0, max_enemies=10, delay=0.1):
		self.speed = speed
		self.score = score
		self.max_enemies = max_enemies
		self.delay = delay				# Lower delay = more staggered enemies

		self.enemy_list = []

    # Drop enemies into game
	def drop_enemies(self, screen_width):
		
        # Define random psuedo-delay
		delay = random.random()
		
        # Generate enemy based on delay if below maximum
		if len(self.enemy_list) < self.max_enemies and delay < self.delay:
			random_x = random.randint(0, screen_width)
			y_pos = 0
			enemy = self.Enemy(random_x, y_pos)
			self.enemy_list.append(enemy)

	# Update falling enemy positions
	def update_enemy_positions(self, screen_height):
		new_enemy_list = []
		for enemy in self.enemy_list:

			# Have enemy fall when on screen
			if enemy.y >= 0 and enemy.y < screen_height:
				enemy.y += self.speed
				new_enemy_list.append(enemy)
			
			# Increment score when enemy exits screen
			else:
				self.score += 1
		self.enemy_list = new_enemy_list

	# Set speed to increase in increments based on score
	def set_level(self):
		if self.score < 20:
			self.speed = 5
		elif self.score < 40:
			self.speed = 8
		elif self.score < 60:
			self.speed = 12
		else:
			self.speed = 15

	# Check collisions with player for all enemies
	def collision_check(self, player):
		for enemy in self.enemy_list:
			if enemy.detect_collision(player):
				return True
		return False

# Hard game mode
class HardGame(Game):

	# Set to large enemy
	Enemy = LargeEnemy

	# Set speed to increase proportionally to score
	def set_level(self):
		self.speed = self.score/5 + 1

# Boss game mode
class BossGame(Game):

	Enemy = KeithEnemy