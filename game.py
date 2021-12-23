import pygame
import sys
import time
from pygame.locals import *
import random
pygame.init()
 
# Colours
BACKGROUND = (255, 255, 255)
 
# Game Setup
WINDOW_WIDTH = 700
WINDOW_HEIGHT = 600
 
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Snakey Snake') 
colors = [(60,19,97),(82, 48, 124),(102, 58, 130),(124, 82, 149), (180, 145, 200),(188, 160, 220)]
blue = (0,0,255)
red = (255,0,0)
black = (0,0,0)



clock = pygame.time.Clock()
snake_speed=30
 
font_style = pygame.font.SysFont(None, 30)
score_font = pygame.font.SysFont("comicsansms", 35)

def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, blue)
    WINDOW.blit(value, [0, 0])

def make10(number):
    while number%10 != 0:
        number+= 1
    return number

def message(msg,color):
    mesg = font_style.render(msg, True, color)
    WINDOW.blit(mesg, [WINDOW_WIDTH/4, WINDOW_HEIGHT/2])
snake_block = 10

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(WINDOW, colors[snake_list.index(x)%len(colors)], [int(x[0]),int(x[1]), snake_block,snake_block])

def updateFood(list):
    foodx = make10(round(random.randrange(0,WINDOW_WIDTH - snake_block)))
    foody = make10(round(random.randrange(0,WINDOW_HEIGHT - snake_block)))
    for item in list:
        if foodx == item[0] and foody == item[1]:
            return 0
    return [foodx,foody]
# The main game loop
def runIt():
    x1 = WINDOW_WIDTH/2
    y1 = WINDOW_HEIGHT/2

    deltaY = 0
    deltaX = 0


    snake_List = []
    length = 1
    lastDir = 0
    Game_Over = False
    Game_close = False

    exo = updateFood([[1000,1000]])

    while not Game_Over:
        # Get inputs
        while Game_close == True:
            WINDOW.fill(black)
            message("You bitch. Press Q to quit, or C to continue", red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        Game_Over = True
                        Game_close = False
                    if event.key == pygame.K_c:
                        runIt()
        justNow = False
        for event in pygame.event.get():
            if event.type == QUIT :
                Game_Over = True
            if event.type == pygame.KEYDOWN:
                justNow = True
                if event.key == pygame.K_LEFT and lastDir != 2:
                    deltaX = -10
                    deltaY = 0
                    lastDir = 1
                elif event.key == pygame.K_RIGHT and lastDir != 1:
                    deltaX = 10
                    deltaY = 0
                    lastDir = 2
                elif event.key == pygame.K_UP and lastDir != 4:
                    deltaY = -10
                    deltaX = 0
                    lastDir = 3
                elif event.key == pygame.K_DOWN and lastDir != 3:
                    deltaY = 10
                    deltaX = 0
                    lastDir = 4

                x1 += deltaX
                y1 += deltaY
            pygame.display.update()    

        if x1 < 0 or x1 >= WINDOW_WIDTH or y1 < 0 or y1 >= WINDOW_HEIGHT:
            Game_close = True
        if not justNow:
            x1 += deltaX
            y1 += deltaY


        WINDOW.fill(BACKGROUND)
        pygame.draw.rect(WINDOW, blue, [exo[0], exo[1], snake_block, snake_block]) 

        snake_head = []
        snoot = x1
        sneet = y1
        for bang in range(10):
            snake_head.append(snoot)
            snake_head.append(sneet)
            snoot +=10
            sneet += 10

        snake_List.append(snake_head)
    
        if len(snake_List) > length:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_head:
                Game_close = True
        our_snake(snake_block, snake_List)
        Your_score(length-1)
        if x1 == exo[0] and y1 == exo[1]:
            exo = updateFood(snake_List)
            while exo == 0:
                exo = updateFood(snake_List)
            length += 10
        pygame.display.update()    
        # Render elements of the game
        clock.tick(snake_speed)
    message("Fuck You", red)
    pygame.display.update()
    time.sleep(1)
    pygame.quit()
    quit()
runIt()