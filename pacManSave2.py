import pygame, sys, random
from pygame.locals import *

# set up pygame
pygame.init()
mainClock = pygame.time.Clock()

#set up the window
WINDOWWIDTH = 550
WINDOWHEIGHT = 510
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Pac-Man')

# set up the colors
BLACK = (0, 0, 0)
YELLOW = (255, 200, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# set up movement variables
moveLeft = False
moveRight = False
moveUp = False
moveDown = False
x = 0
y = 0
MOVESPEED = 2


#class to hold a wall rect
class Wall(object):

    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 22, 22)

walls = []

level = [
    "WWWWWWWWWWWWWWWWWWWWWWWWW",
    "W           W           W",
    "W WWW WWWWW W WWWWW WWW W",
    "W WWW WWWWW W WWWWW WWW W",
    "W                       W",
    "W WWW W WWWWWWWWW W WWW W",
    "W     W     W     W     W",
    "WWWWW WWWWW W WWWWW WWWWW",
    "    W W           W W    ",
    "    W W WWW   WWW W W    ",
    "    W   W       W   W    ",
    "    W W W       W W W    ",
    "    W W WWWWWWWWW W W    ",
    "    W W           W W    ",
    "WWWWW W WWWWWWWWW W WWWWW",
    "W           W           W",
    "W WWW WWWWW W WWWWW WWW W",
    "W   W               W   W",
    "WWW W W WWWWWWWWW W W WWW",
    "W     W     W     W     W",
    "W WWWWWWWWW W WWWWWWWWW W",
    "W                       W",
    "WWWWWWWWWWWWWWWWWWWWWWWWW",
    ]

#parse the level string above
a = b = 0
for row in level:
    for col in row:
        if col == "W":
            Wall((a, b))
        a += 22
    b += 22
    a = 0


# draw the player onto the surface
player = pygame.Rect(23, 23, 18, 18)


# run the game loop
while True:
    # check for events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    key = pygame.key.get_pressed()

    if key[pygame.K_LEFT]:
            x = -1
            y = 0
            
    if key[pygame.K_RIGHT]:
            x = 1.5
            y = 0
        
    if key[pygame.K_UP]:
            x = 0
            y = -1

    if key[pygame.K_DOWN]:
            x = 0
            y = 1.5
            
    if x != 0:
        player.x += x
        player.y += y
        for wall in walls:
            if player.colliderect(wall.rect):
                if x > 0:
                    player.right = wall.rect.left
                if x < 0:
                    player.left = wall.rect.right 

    if y != 0:
        player.x += x
        player.y += y
        for wall in walls:
            if player.colliderect(wall.rect): 
                if y < 0:
                    player.top = wall.rect.bottom
                if y > 0:
                    player.bottom = wall.rect.top
    
                
    # draw the black background onto the surface
    windowSurface.fill(BLACK)

    pygame.draw.rect(windowSurface, YELLOW, player)
    
    # draw the window onto the screen
    for wall in walls:
        pygame.draw.rect(windowSurface, (0, 0, 255), wall.rect)
        
    pygame.display.update()
    mainClock.tick(40)

