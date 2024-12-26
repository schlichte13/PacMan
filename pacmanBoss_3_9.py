import pygame 
import sys
#import menuWork.py
  
  
# initializing the constructor 
pygame.init() 
  
# screen resolution 
res = (720,720) 


width = 550
height = 600
# opens up a window 
screen = pygame.display.set_mode((width, height))
  
# white color 
white = (255,255,255)
yellow = (255, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
orange = (255, 130, 0)
red = (255, 0, 0)


playerImage = pygame.image.load('myPacMan.png')
playerImageRight = pygame.image.load('myPacManRight.png')
playerImageLeft = pygame.image.load('myPacManLeft.png')
blinkyImageChase = pygame.image.load('blinky4.png')
frightenedGhost = pygame.image.load('frightenedGhost.png')

pygame.mixer.music.load('game_start.wav')
pygame.mixer.music.play(-1)


playerStretchedImage = pygame.transform.scale(playerImage, (50, 50))
playerStretchedRight = pygame.transform.scale(playerImageRight, (50, 50))
blinkyStretchedChase = pygame.transform.scale(blinkyImageChase, (35, 35))
playerStretchedLeft = pygame.transform.scale(playerImageLeft, (50, 50))
frightenedStretch = pygame.transform.scale(frightenedGhost, (35, 35))

pacMan = pygame.Rect(185, 180, 50, 50)
ghost = pygame.Rect(285, 185, 35, 35)

mouthToggle = pygame.USEREVENT + 0
pygame.time.set_timer(mouthToggle, 300)

ghostToggle = pygame.USEREVENT + 1
pygame.time.set_timer(ghostToggle, 2000)

toggle = 0
toggle2 = 0

  
# light shade of the button 
color_light = (170,170,170) 
  
# dark shade of the button 
color_dark = (100,100,100) 
  
  
# defining a font 
smallfont = pygame.font.SysFont('Corbel',35)
font = pygame.font.SysFont('Corbel', 70)
  
# rendering a text written in 
# this font 
textQ = smallfont.render('exit' , True , white)
textS = smallfont.render('easy', True , white)
textH = smallfont.render('hard', True , white)
#textR = smallfont.render('restart', True, color)
textTitle = font.render('Pac - Man', True, yellow)
  
while True: 
      
    for ev in pygame.event.get(): 
          
        if ev.type == pygame.QUIT: 
            pygame.quit()


        if ev.type == mouthToggle:
            toggle = (toggle + 1) % 2

        if ev.type == ghostToggle:
            toggle2 = (toggle2 + 1) % 2


        if toggle2 == 0:
            ghostImage = blinkyStretchedChase
            rightLeft = playerStretchedLeft

        if toggle2 == 1:
            ghostImage = frightenedStretch
            rightLeft = playerStretchedRight


        if toggle == 0:
            image = rightLeft

        if toggle == 1:
            image = playerStretchedImage
              
        #checks if a mouse is clicked 
        if ev.type == pygame.MOUSEBUTTONDOWN: 
              
            #if the mouse is clicked on the 
            # button the game is terminated 
            if 185 <= mouse[0] <= 325 and 460 <= mouse[1] <= 500: 
                pygame.quit()

            if 185 <= mouse[0] <= 325 and 360 <= mouse[1] <= 400:
                import bossLevel.py

            if 185 <= mouse[0] <= 325 and 260 <= mouse[1] <= 300:
                import pinkyPath.py
                  
    # fills the screen with a color 
    screen.fill(black) 
      
    # stores the (x,y) coordinates into 
    # the variable as a tuple 
    mouse = pygame.mouse.get_pos() 
      
    # if mouse is hovered on a button it 
    # changes to lighter shade 
    if 185 <= mouse[0] <= 325 and 440 <= mouse[1] <= 480: 
        pygame.draw.rect(screen,color_light,[185,440,140,40]) 
          
    else: 
        pygame.draw.rect(screen,blue,[185,440,140,40])


    if 185 <= mouse[0] <= 325 and 360 <= mouse[1] <= 400:
        pygame.draw.rect(screen,color_light, [185,360,140,40])

    else:
        pygame.draw.rect(screen,red,[185,360,140,40])

    if 185 <= mouse[0] <= 325 and 280 <= mouse[1] <= 320:
        pygame.draw.rect(screen, color_light,[185,280,140,40])
        

    else:
        pygame.draw.rect(screen,blue,[185,280,140,40])
      
    # superimposing the text onto our button
    screen.blit(textTitle, (135, 100))
    screen.blit(textQ , (230,440))
    screen.blit(textS, (230,280))
    screen.blit(textH, (230,360))

    screen.blit(image, pacMan)
    screen.blit(ghostImage, ghost)
    
      
    # updates the frames of the game 
    pygame.display.update()
