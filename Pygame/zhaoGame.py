'''
Name: Kevin Zhao
File: zhaoGame.py
Date: 04/17/2024

Purpose: Create a game in which the player must dodge falling blocks
         that become faster over time

'''

import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Define screen dimensions
WIDTH = 800
HEIGHT = 600                                        

# Define game colors
RED = (255,0,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
BACKGROUND_COLOR = (0,0,0)

# Define player size and position
player_size = 50
player_pos = [WIDTH/2, HEIGHT-2*player_size]

# Define enemy size and random position
enemy_size = 50
enemy_pos = [random.randint(0,WIDTH-enemy_size), 0]

# Define enemy list (starts with one enemy)
enemy_list = [enemy_pos]

# Define enemy falling speed
SPEED = 10

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Define game over state
game_over = False

# Define score
score = 0

# Define clock to set frame rate
clock = pygame.time.Clock()

# Define font for score display
myFont = pygame.font.SysFont("monospace", 35)


# Set speed to increase based on score
def set_level(score, SPEED):
	if score < 20:
		SPEED = 5
	elif score < 40:
		SPEED = 8
	elif score < 60:
		SPEED = 12
	else:
		SPEED = 15
	return SPEED
	# SPEED = score/5 + 1                       # Speed proportional to score


# Drop enemies into game
def drop_enemies(enemy_list):

    # Define random psuedo-delay
	delay = random.random()
	
    # Generate enemy 1 in 10 times (maximum of 10 enemies at a time)
	if len(enemy_list) < 10 and delay < 0.1: 
		x_pos = random.randint(0,WIDTH-enemy_size)
		y_pos = 0
		enemy_list.append([x_pos, y_pos])


# Draw enemy rectangles
def draw_enemies(enemy_list):
	for enemy_pos in enemy_list:
		pygame.draw.rect(screen, BLUE, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))


# Update falling enemy positions
def update_enemy_positions(enemy_list, score):

	for idx, enemy_pos in enumerate(enemy_list):

		# Have enemy fall when on screen
		if enemy_pos[1] >= 0 and enemy_pos[1] < HEIGHT:
			enemy_pos[1] += SPEED

        # Remove enemy and increment score when it exits screen
		else:
			enemy_list.pop(idx)
			score += 1

	return score


# Check collisions for all enemies
def collision_check(enemy_list, player_pos):
	for enemy_pos in enemy_list:
		if detect_collision(enemy_pos, player_pos):
			return True
	return False


# Detect when enemy collides with player
def detect_collision(player_pos, enemy_pos):
	
    # Get current player and enemy positions
	p_x = player_pos[0]
	p_y = player_pos[1]
	e_x = enemy_pos[0]
	e_y = enemy_pos[1]

    # Check for overlap on x-axis
	if (e_x >= p_x and e_x < (p_x + player_size)) or (p_x >= e_x and p_x < (e_x+enemy_size)):
		# Check for overlap on y-axis
		if (e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= e_y and p_y < (e_y+enemy_size)):
			return True
	return False


while not game_over:                                # Run game until game over

	for event in pygame.event.get():
		if event.type == pygame.QUIT:               # Track quit event
			sys.exit()

		if event.type == pygame.KEYDOWN:            # Track keyboard event
            
			x = player_pos[0]                       # Get current player position
			y = player_pos[1]

			if event.key == pygame.K_LEFT:          # Track left arrow key
				x -= player_size                    # Move player left
			elif event.key == pygame.K_RIGHT:       # Track right arrow key
				x += player_size                    # Move player right

			player_pos = [x,y]                      # Update player position

	screen.fill(BACKGROUND_COLOR)                   # Reset screen every update

    # Drop falling enemies and update score and speed
	drop_enemies(enemy_list)
	score = update_enemy_positions(enemy_list, score)
	SPEED = set_level(score, SPEED)

    # Display score on screen
	text = "Score:" + str(score)
	label = myFont.render(text, 1, YELLOW)
	screen.blit(label, (WIDTH-200, HEIGHT-40))

    # Check for collisions
	if collision_check(enemy_list, player_pos):
		game_over = True                            # Game over upon collision
		break                                       # Exit loop upon collision
    
    # Draw enemy rectangles
	draw_enemies(enemy_list)

    # Draw player rectangle
	pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], player_size, player_size))

	clock.tick(30)                                  # Set frame rate of 30 fps

	pygame.display.update()                         # Update display