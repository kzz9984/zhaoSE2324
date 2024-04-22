'''
Name: Kevin Zhao
File: zhaoScreen.py
Date: 04/21/2024

Purpose: Create a class to handle all the visual components of the game

'''

from zhaoColor import Color
import pygame

# Class containing all visual functions
class Screen:
	def __init__(self, width=800, height=600, background_color=Color.BACKGROUND_COLOR, font_type="monospace", font_size=35, clock_tick=30):
		
		# Define screen and its dimensions
		self.width = width								
		self.height = height
		self.screen = pygame.display.set_mode((width, height))

		# Define background color and font	
		self.background_color = background_color
		self.font = pygame.font.SysFont(font_type, font_size)

		# Define clock and frame rate
		self.clock = pygame.time.Clock()				
		self.clock_tick = clock_tick

	# Reset screen 
	def refresh_background(self):
		self.screen.fill(self.background_color)

	# Draw enemies on screen
	def draw_enemies(self, enemy_list):
		for enemy in enemy_list:
			enemy.draw(self.screen)

	# Draw player on screen
	def draw_player(self, player):
		player.draw(self.screen)

	# Draw score label on screen
	def draw_score_label(self, score, color=Color.YELLOW):
		text = f"Score: {score}"
		label = self.font.render(text, 1, color)
		self.screen.blit(label, (self.width-200, self.height-40))

	# Update screen
	def update_screen(self, enemy_list, player, score):
	
		# Reset screen every update
		self.refresh_background()						
		
		# Draw all components on screen
		self.draw_enemies(enemy_list)
		self.draw_player(player)
		self.draw_score_label(score)

		# Update display based on frame rate
		self.clock.tick(self.clock_tick)
		pygame.display.update()					