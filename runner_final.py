import pygame
import random

pygame.init()

# game constants
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
orange= (255, 165, 0)
yellow = (255, 255, 0)
WIDTH = 600
HEIGHT = 600

# game variables
score1 = 0
score2 = 0
player1_x = 50
player1_y = 200
player2_x = 50
player2_y = 500
y1_change = 0
x1_change = 0
y2_change = 0
x2_change = 0
gravity = 1
obstacles1 = [450, 600, 750]
obstacles2 = [450, 600, 750]
powerLoc1 = 450
powerLoc2 = 600
powerLoc3 = 450
powerLoc4 = 600
obstacle_speed1 = 2 # also used in power-ups speed!
obstacle_speed2 = 2
speedResetCtr1 = 0
speedResetCtr2 = 0
active = False
player1_running = False
player2_running = False

screen = pygame.display.set_mode([WIDTH, HEIGHT])
#screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Runner Game')
background = black
fps = 60
font = pygame.font.Font('freesansbold.ttf', 16)
timer = pygame.time.Clock()

# game loop
running = True
while running:
    timer.tick(fps)
    screen.fill(background)
    if not active:
        instruction_text = font.render(f'Space Bar to Start', True, white, black)
        screen.blit(instruction_text, (150, 50))
        instruction_text2 = font.render(f'Player 1: Up Arrow Jumps, Left/Right', True, white, black)
        screen.blit(instruction_text2, (80, 90))
        instruction_text3 = font.render(f'Player 2: W Key Jumps, A=Left, D=Right', True, white, black)
        screen.blit(instruction_text3, (80, 300))
        if not player1_running and not player2_running and score1 > score2:
            win1_text = font.render(f'Player 1 Wins!', True, white, black)
            screen.blit(win1_text, (120, 350))
        if not player1_running and not player2_running and score2 > score1:
            win2_text = font.render(f'Player 2 Wins!', True, white, black)
            screen.blit(win2_text, (120, 350))

    score1_text = font.render(f'Score: {score1}', True, white, black)
    screen.blit(score1_text, (450, 40))
    score2_text = font.render(f'Score: {score2}', True, white, black)
    screen.blit(score2_text, (450, 260))

    floor1 = pygame.draw.rect(screen, white, [0, 220, WIDTH, 5])
    floor2 = pygame.draw.rect(screen, white, [0, 520, WIDTH, 5])
    player1 = pygame.draw.rect(screen, green, [player1_x, player1_y, 20, 20])
    player2 = pygame.draw.rect(screen, green, [player2_x, player2_y, 20, 20])
    # player 1 obstacles
    obstacle0 = pygame.draw.rect(screen, red, [obstacles1[0], 200, 20, 20])
    obstacle1 = pygame.draw.rect(screen, orange, [obstacles1[1], 200, 20, 20])
    obstacle2 = pygame.draw.rect(screen, yellow, [obstacles1[2], 200, 20, 20])
    # player 2 obstacles
    obstacle3 = pygame.draw.rect(screen, red, [obstacles2[0], 500, 20, 20])
    obstacle4 = pygame.draw.rect(screen, orange, [obstacles2[1], 500, 20, 20])
    obstacle5 = pygame.draw.rect(screen, yellow, [obstacles2[2], 500, 20, 20])
    # player 1 power-ups
    power1 = pygame.draw.circle(screen, green, [powerLoc1, 100], 10) # speed up opponent
    power2 = pygame.draw.circle(screen, yellow, [powerLoc2, 100], 10) # slow down yourself
    # player 2 power-ups
    power3 = pygame.draw.circle(screen, green, [powerLoc3, 400], 10) # speed up opponent
    power4 = pygame.draw.circle(screen, yellow, [powerLoc4, 400], 10) # slow down yourself

    # player 1 score counter
    if active:
        if player1_running:
            score1 += 1
        if player2_running:
            score2 += 1
        
    # Go non active when both crash, not just one
    if not player2_running and not player1_running:
        active = False
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # game start on space and resets on space
        if event.type == pygame.KEYDOWN and not active:
            if event.key == pygame.K_SPACE:
                obstacles1 = [450, 600, 750]
                obstacles2 = [450, 600, 750]
                player1_x = 50
                player2_x = 50
                player1_y = 200
                player2_y = 500
                powerLoc1 = 450
                powerLoc2 = 600
                powerLoc3 = 450
                powerLoc4 = 600
                score1 = 0
                score2 = 0
                active = True
                player1_running = True
                player2_running = True

        # speed counters to reset
        if speedResetCtr1 != 0:
            speedResetCtr1 -= 1
        else:
            obstacle_speed1 = 2
        
        if speedResetCtr2 != 0:
            speedResetCtr2 -= 1
        else:
            obstacle_speed2 = 2

    
        # player 1 movement
        if event.type == pygame.KEYDOWN and active and player1_running:
            # player 1 jump
            if event.key == pygame.K_UP and y1_change == 0:
                y1_change = 18
            # player 1 right press
            if event.key == pygame.K_RIGHT:
                x1_change = 2
            # player 1 left press
            if event.key == pygame.K_LEFT:
                x1_change = -2

        # player 1 stop moving
        if event.type == pygame.KEYUP:
            # player 1 right release 
            if event.key == pygame.K_RIGHT:
                x1_change = 0
            # player 1 left release
            if event.key == pygame.K_LEFT:
                x1_change = 0

        # player 2 movement
        if event.type == pygame.KEYDOWN and active and player2_running:
            # player 2 jump
            if event.key == pygame.K_w and y2_change == 0:
                y2_change = 18
            # player 2 d press
            if event.key == pygame.K_d:
                x2_change = 2
            # player 2 a press
            if event.key == pygame.K_a:
                x2_change = -2

        # player 2 stop moving
        if event.type == pygame.KEYUP:
            # player 2 d release
            if event.key == pygame.K_d:
                x2_change = 0
            # player 2 a release
            if event.key == pygame.K_a:
                x2_change = 0
            
    # obstacles movement player 1
    for i in range(len(obstacles1)):
        if active and player1_running:
            obstacles1[i] -= obstacle_speed1
            if obstacles1[i] < -20:
                obstacles1[i] = random.randint(620, 720)
            if player1.colliderect(obstacle0) or player1.colliderect(obstacle1) or player1.colliderect(obstacle2):
                player1_running = False
                x1_change = 0
                y1_change = 0
    
    # obstacles movement player 2
    for i in range(len(obstacles2)):
        if active and player2_running:
            obstacles2[i] -= obstacle_speed2
            if obstacles2[i] < -20:
                obstacles2[i] = random.randint(620, 720)
            if player2.colliderect(obstacle3) or player2.colliderect(obstacle4) or player2.colliderect(obstacle5):
                player2_running = False
                x2_change = 0
                y2_change = 0

    # powerups movement player 1 - speed up opp
    if active and player1_running:
        powerLoc1 -= obstacle_speed1
        powerLoc2 -= obstacle_speed1
        if powerLoc1 < -20:
            powerLoc1 = random.randint(620, 820)
        if powerLoc2 < -20:
            powerLoc2 = random.randint(620, 820)
        if player1.colliderect(power1):
            obstacle_speed2 = 3
            speedResetCtr2 = 10
    # slow down self
        if player1.colliderect(power2):
            obstacle_speed1 = 1
            speedResetCtr1 = 10

    # powerups movement player 2 - speed up opp
    if active and player2_running:
        powerLoc3 -= obstacle_speed2
        powerLoc4 -= obstacle_speed2
        if powerLoc3 < -20:
            powerLoc3 = random.randint(620, 720)
        if powerLoc4 < -20:
            powerLoc4 = random.randint(620, 720)
        if player2.colliderect(power3):
            obstacle_speed1 = 3
            speedResetCtr1 = 10
    # slow down self
        if player2.colliderect(power4):
            obstacle_speed2 = 1
            speedResetCtr2 = 10
    
    # movement logic player 1
    if 0 <= player1_x <= 580:
        player1_x += x1_change
    if player1_x < 0:
        player1_x = 0
    if player1_x > 580:
        player1_x = 580

    # movement logic player 2
    if 0 <= player2_x <= 580:
        player2_x += x2_change
    if player2_x < 0:
        player2_x = 0
    if player2_x > 580:
        player2_x = 580


    # jump logic player 1
    if y1_change > 0 or player1_y < 200:
        player1_y -= y1_change
        if player1_running:
            y1_change -= gravity
    if player1_y > 200:
        player1_y = 200
    if player1_y == 200 and y1_change < 0:
        y1_change = 0

    # jump logic player 2
    if y2_change > 0 or player2_y < 500:
        player2_y -= y2_change
        if player2_running:
            y2_change -= gravity
    if player2_y > 500:
        player2_y = 500
    if player2_y == 500 and y2_change < 0:
        y2_change = 0

    if not active: # reset these changing variables
        obstacle_speed2 = 2
        obstacle_speed1 = 2

    pygame.display.flip()
pygame.quit()