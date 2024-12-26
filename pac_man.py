import pygame, sys, random
from pygame.locals import *

#setup
pygame.init()
mainClock = pygame.time.Clock()

#window setup
WINDOWWIDTH = 550
WINDOWHEIGHT = 510
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Pac-Man')

#colors
BLACK = (0, 0, 0)
YELLOW = (255, 200, 0)
BLUE = (0, 0, 255)

#variables
x = 0
y = 0




#class to hold wall block positions
class Wall(object):
    
    #constructor that adds individual block position to wall list based on level[]
    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 22, 22)




#stores the coordinates for blocks needed to build the maze
walls = []

#representation of the wall layout
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



#get the coordinates from level[] for the blocks needed for the walls

a = b = 0 #variables for (x, y) wall coordinates

for row in level:
    for col in row:
        if col == "W":
            #send coordinates to the wall class if spot contains "W"
            Wall((a, b))
        #increase x coordinate for next spot in levels column
        a += 22
    #increase y coordinate for next row in levels, reset x 
    b += 22
    a = 0


#create players coordinates and size
player = pygame.Rect(23, 23, 18, 18)


#run the game loop
while True:

    #check for events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    #variable to hold specific key pressed
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

    player.x += x
    player.y += y

    for wall in walls:
        if player.colliderect(wall.rect):
            if x > 0:
                player.right = wall.rect.left
            if x < 0:
                player.left = wall.rect.right
            if y < 0:
                player.top = wall.rect.bottom
            if y > 0:
                player.bottom = wall.rect.top
    
    

    #black background
    windowSurface.fill(BLACK)

    #draw player onto screen with coordinates, size, and color
    pygame.draw.rect(windowSurface, YELLOW, player)

    #build maze from list
    for wall in walls:
        pygame.draw.rect(windowSurface, (0, 0, 255), wall.rect)


    pygame.display.update()
    mainClock.tick(40)
