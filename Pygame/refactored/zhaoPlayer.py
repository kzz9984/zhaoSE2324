'''
Name: Kevin Zhao
File: zhaoPlayer.py
Date: 04/21/2024

Purpose: Create classes to define the properties of all game entities

'''

from zhaoColor import Color
import pygame

# Parent class for all entities
class Player:
	def __init__(self, x, y, size, color=Color.RED):
		self.x = x
		self.y = y
		self.size = size
		self.color = color

	# Draw player rectangle
	def draw(self, screen):
		pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))

	# Detect when another entity collides with player
	def detect_collision(self, other):

		# Check for overlap on x-axis
		if (other.x >= self.x and other.x < (self.x + self.size)) or (self.x >= other.x and self.x < (other.x + other.size)):
			# Check for overlap on y-axis
			if (other.y >= self.y and other.y < (self.y + self.size)) or (self.y >= other.y and self.y < (other.y + self.size)):
				return True

		return False

# Class for normal enemy
class Enemy(Player):
	def __init__(self, x, y):
		super().__init__(x, y, size=50, color=Color.BLUE)

# Class for large enemy
class LargeEnemy(Player):
	def __init__(self, x, y):
		super().__init__(x, y, size=100, color=Color.BLUE)

# Class for boss enemy
class KeithEnemy(Player):

	# Get image using absolute path
	img = pygame.image.load(r"C:\Users\kevin\OneDrive\Desktop\Software Engineering\zhaoSE2324\Pygame\refactored\assets\selfie.jpg")
	
	def __init__(self, x, y):
		super().__init__(x, y, size=75, color=Color.BLUE)

	# Draw boss enemy rectangle and apply Keith image
	def draw(self, screen):
		rect = pygame.Rect(self.x, self.y, self.size,self.size)
		scaled_img = pygame.transform.scale(self.img, rect.size)
		scaled_img = scaled_img.convert()
		screen.blit(scaled_img, rect)

# Class for user-controlled player
class HumanPlayer(Player):
	def __init__(self, x, y):
		super().__init__(x, y, size=50, color=Color.RED)