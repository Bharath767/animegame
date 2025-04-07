import pygame
import time
import math
import random

pygame.init()
#pygame.font.init()


screen = pygame.display.set_mode((512,448))
# game caption
pygame.display.set_caption('zoro hunt')
# game icon
icon = pygame.image.load('zoro logo.png')
pygame.display.set_icon(icon)
# background image
bgimage =pygame.image.load('bg_image.jpg') 
#zoro image
zoroimage =pygame.image.load('bat1.png')
#zoro position
zorox = 150
zoroy = 150
#direction
direction = "right"
#kill score
score = -1
#mihack image
mihackimage =pygame.image.load('ball_image.png')
#mihack position 
mihawkx = 110
mihawky= 110

#score
scorefont = pygame.font.SysFont('freesansbold.tff',40)
# game over font
gameoverfont = pygame.font.SysFont('freesansbold',80)
#bg music
pygame.mixer.init()
pygame.mixer.music.load('bg_music.mp3')


pygame.mixer.music.play(-1)
gameover = False
while not gameover:
   
    screen.blit(bgimage, (0,0))
    screen.blit(zoroimage,(zorox,zoroy))
    screen.blit(mihackimage,(mihawkx,mihawky))
    
    distance = math.dist ((zorox,zoroy),(mihawkx,mihawky))  
    if distance <= 60:
        pygame.mixer.Sound('mixkit-samurai-sword-impact-2789.wav').play()
        # pygame.mixer.Sound('run_music.mp3').play()
        mihawkx = random.randint(1,500-50)   
        mihawky = random.randint(50,500-62)    
        score = score + 1   
       
    scoresurface = scorefont.render(f"RUNS_SCORED : {score}", True, (5,5,5))
    screen.blit(scoresurface, (200,20))
                    
   
        
    for event in pygame.event.get( ):
        if event.type == pygame.QUIT:
            gameover = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:    
                direction = "right"
            if event.key == pygame.K_LEFT:
                direction = "left" 
            if event.key == pygame.K_UP:
                direction = "up"          
            if event.key == pygame.K_DOWN:
                direction = "down"    
    if direction =="right":
       zorox = zorox + 2
    if direction =="left":
       zorox = zorox - 2
    if direction =="up":
       zoroy -= 2
    if direction =="down":
       zoroy += 2
    
    if zorox <= 0 or zorox >= 462 or zoroy <=0 or zoroy>= 450:
        gameover = True
   
    if gameover:
        gameoversurface = gameoverfont.render("GAME OVER ",True,(255,255,0))
        screen.blit(gameoversurface,(110,200))
        pygame.display.update()
        pygame.mixer.music.stop()
        pygame.mixer.Sound('nani_Pmxf5n3.mp3').play()
        time.sleep(4)     
    pygame.display.update()
    
    time.sleep(0.02)

    