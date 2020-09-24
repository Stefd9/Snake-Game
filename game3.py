import pygame
import random
import time


pygame.init()
clock = pygame.time.Clock()
 # Creating the game screen - X = (800) LEFT TO RIGHT. Y = (600) TOP TO BOTTOM
display_width = 600
display_height = 400
screen = pygame.display.set_mode((display_width, display_height))

# RGB colours
blackcolor = (0, 0, 0)
greencolor = (0, 255, 0)
bluecolor = (50, 153, 213)
orangecolor = (255, 123, 7)
redcolor = (255, 0, 0)


# Player/Snake
player_size = 10
snake_speed = 10
snake_list = []





def snake(player_size, snake_list ):
	for x in snake_list:
		pygame.draw.rect(screen, redcolor, [x[0], x[1], player_size, player_size])




# Game caption and Icon
pygame.display.set_caption("Stefs Game of snake")

def snakegame():

	game_end = False
	game_over = False

	# Snake co-ordinates

	playerX = display_width / 2
	playerY = display_height / 2

	# Records Snakes movement
	playerX_change = 0
	playerY_change = 0
	head_direction = "none"


	# Snake length
	snake_list = []
	length_of_snake = 1

	# Food co-ordinates
	foodx = round(random.randrange(0, display_width - player_size) / 10.0) * 10.0
	foody = round(random.randrange(0, display_height - player_size) / 10.0) * 10.0




	while not game_over:


		while game_end == True:

			# Play Again Function
			screen.fill(blackcolor)
			play_again_font = pygame.font.SysFont("comicsansms", 30)
			play_again_message = play_again_font.render("Play Again? Press P. Press Q to quit", True, orangecolor)
			screen.blit(play_again_message, [display_width / 9.5, display_height / 3])



			# Score Board+ 
			score = length_of_snake - 1
			score_font = pygame.font.SysFont("comicsansms", 35)
			value = score_font.render("Your Score: " + str(score), True, greencolor)
			screen.blit(value, [display_width / 3, display_height / 5])

			high_score_value = score
			current_high_score = high_score_value
			if score < high_score_value:
				high_score_value = current_high_score
			else:
				high_score_value = score
			high_score_font = pygame.font.SysFont("comicsansms", 25)
			high_score = high_score_font.render("High Score: " + str(high_score_value), True, redcolor)
			screen.blit(high_score, [display_width / 2.5, display_height / 8])
			pygame.display.update()



			# Quit Program Function
	  
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_p:
						snakegame()
					elif event.key == pygame.K_q:
						pygame.quit()
						quit()

				if event.type == pygame.QUIT:
					game_over = True
					game_end = False

		# Snake Movement
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game_over = True

			if event.type == pygame.KEYDOWN:

			#To stop the snake being able to go in the reverse direction, if it is going in one direction,
			#pressing the opposite key will not do anything except allow it to continue in that direction.
			

				if event.key == pygame.K_LEFT and head_direction != "right":
					playerY_change = 0
					playerX_change = -player_size #(It goes in the left direction.)
					head_direction = "left"
					

						


				elif event.key == pygame.K_RIGHT and head_direction != "left":
					playerY_change = 0
					playerX_change = player_size
					head_direction = "right"
					

					

				elif event.key == pygame.K_UP and head_direction != "down":
					playerX_change = 0
					playerY_change = -player_size
					head_direction = "up"
					

				elif event.key == pygame.K_DOWN and head_direction != "up":
					playerX_change = 0
					playerY_change = player_size
					head_direction = "down"

		if playerX >= display_width or playerX < 0 or playerY >= display_height or playerY < 0:
			game_end = True

		#Drawing (blit) the image of the player 
		playerX += playerX_change
		playerY += playerY_change

		screen.fill(blackcolor)

		pygame.draw.rect(screen,greencolor,[foodx,foody,player_size,player_size])
		snake_head = []
		snake_head.append(playerX)
		snake_head.append(playerY)
		snake_list.append(snake_head)

		# 

		if len(snake_list) > length_of_snake:
			del snake_list[0]

		for x in snake_list[:-1]:
			if x == snake_head:
				game_end = True 
		snake(player_size, snake_list)
		pygame.display.update()

		if playerX == foodx and playerY == foody:
			foodx = round(random.randrange(0, display_width - player_size) / 10.0) * 10.0
			foody = round(random.randrange(0, display_height - player_size) / 10.0) * 10.0
			length_of_snake += 1
		clock.tick(snake_speed)
	pygame.quit()
	quit()
snakegame()