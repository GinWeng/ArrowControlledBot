
import pygame
import numpy as np


# initialize the pygame environment
pygame.init()

# screen height and width
height = 600
width = 800
screen = pygame.display.set_mode((width, height))

# Title and Icon
pygame.display.set_caption("Robot in tic tac toe")
icon =  pygame.image.load('winnieXi.png')
pygame.display.set_icon(icon)


# Player 
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
moveSpeed = 0.2
(playerSizeX,playerSizeY) = playerImg.get_size()
playerX_change = 0
playerY_change = 0

def playerArrowControl(x,y):
    screen.blit(playerImg, (x, y)) # drawing the screen frame

def playerNumControl(number):
    pass

# Game Loop
running = True
while running:

    # RGB value in the fill
    screen.fill((255,255,255)) #background color RGB
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
       
    # if keystroke is pressed, check whether if it is arrow keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("left arrow pressed")
                playerX_change = -moveSpeed
            if event.key == pygame.K_RIGHT:
                print("right arrow pressed")
                playerX_change = moveSpeed
            if event.key == pygame.K_UP:
                print("up arrow pressed")
                playerY_change = -moveSpeed
            if event.key == pygame.K_DOWN:
                print("down arrow pressed")
                playerY_change = moveSpeed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print("keystroke is released")
                playerX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                print("keystroke is released")
                playerY_change = 0

    if playerX >= (width-playerSizeX) and playerX_change >0 :
        playerX = width-playerSizeX
    elif playerX <= 0 and playerX_change <0:
        playerX = 0
    else:
        playerX += playerX_change

    if playerY >= (height-playerSizeY) and playerY_change >0 :
        playerY = height-playerSizeY
    elif playerY <= 0 and playerY_change <0:
        playerY = 0
    else:
        playerY += playerY_change
    playerArrowControl(playerX,playerY) # to avoid player being covered by the background


    # Two movement options: 
    ## Option 1 - movement by arrow keys

    ## Option 2 - teleport by the number keys (1-9)
    pygame.display.update()