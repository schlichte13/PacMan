import pygame, sys, random
from pygame.locals import *

#from itertools import cycle
#sys.path.append(".")
#from Wall import Wall


#setup
pygame.init()
mainClock = pygame.time.Clock()

#window setup
WINDOWWIDTH = 550
WINDOWHEIGHT = 600
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Pac-Man')

#colors
BLACK = (0, 0, 0)
YELLOW = (255, 200, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

#variables
x = 0
y = 0
score = 0
value = 0

vectors = []

vectors.append(pygame.Rect(110, 30, 1, 1))
vectors.append(pygame.Rect(390, 30, 1, 1))
vectors.append(pygame.Rect(30, 90, 1, 1))
vectors.append(pygame.Rect(110, 90, 1, 1))
vectors.append(pygame.Rect(150, 90, 1, 1))
vectors.append(pygame.Rect(230, 90, 1, 1))
vectors.append(pygame.Rect(270, 90, 1, 1))
vectors.append(pygame.Rect(350, 90, 1, 1))
vectors.append(pygame.Rect(390, 90, 1, 1))
vectors.append(pygame.Rect(110, 130, 1, 1))
vectors.append(pygame.Rect(390, 130, 1, 1))
vectors.append(pygame.Rect(230, 170, 1, 1))
vectors.append(pygame.Rect(270, 170, 1, 1))
vectors.append(pygame.Rect(110, 210, 1, 1))
vectors.append(pygame.Rect(150, 210, 1, 1))
vectors.append(pygame.Rect(350, 210, 1, 1))
vectors.append(pygame.Rect(390, 210, 1, 1))
vectors.append(pygame.Rect(150, 270, 1, 1))
vectors.append(pygame.Rect(350, 270, 1, 1))
vectors.append(pygame.Rect(110, 310, 1, 1))
vectors.append(pygame.Rect(150, 310, 1, 1))
vectors.append(pygame.Rect(350, 310, 1, 1))
vectors.append(pygame.Rect(390, 310, 1, 1))
vectors.append(pygame.Rect(110, 350, 1, 1))
vectors.append(pygame.Rect(150, 350, 1, 1))
vectors.append(pygame.Rect(230, 350, 1, 1))
vectors.append(pygame.Rect(270, 350, 1, 1))
vectors.append(pygame.Rect(350, 350, 1, 1))
vectors.append(pygame.Rect(390, 350, 1, 1))
vectors.append(pygame.Rect(70, 390, 1, 1))
vectors.append(pygame.Rect(430, 390, 1, 1))
vectors.append(pygame.Rect(230, 430, 1, 1))
vectors.append(pygame.Rect(270, 430, 1, 1))
vectors.append(pygame.Rect(470, 90, 1, 1))



#class that adds block position to walls[]
class Wall(object):

    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 20, 20)
        

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
    "WWWWW W WWW   WWW W WWWWW",
    "        W       W        ",
    "      W W       W W      ",
    "WWWWW W WWWWWWWWW W WWWWW",
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



a = b = 0 #variables for (x, y) wall coordinates

#get the coordinates from level[] for the blocks needed for the wall
for row in level:
    for col in row:
        if col == "W":
            #send coordinates to the wall class if spot contains "W"
            Wall((a, b))
        #increase x coordinate for next spot in levels column
        a += 20
    #increase y coordinate for next row in levels, reset x 
    b += 20
    a = 0


#create players coordinates and size
player = pygame.Rect(240, 260, 20, 20)

#setting up the text to be displayed for the scoreboard
font = pygame.font.SysFont(None, 48)
text = 'Score: '

#method for drawing text on our window
def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, YELLOW)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

toggle = 0

#run the game loop
while True:

    #check for events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
   

    #checks players direction and prevents them from going through a wall
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

    #build maze from list
    for wall in walls:
        pygame.draw.rect(windowSurface, (0, 0, 255), wall.rect)

    for i in range(0, 520, 20):
        pygame.draw.line(windowSurface, WHITE, (i, 0), (i, 460))

    for i in range(0, 480, 20):
        pygame.draw.line(windowSurface, WHITE, (0, i), (500, i))

    #draw vectors
    for i in range(len(vectors)):
        pygame.draw.rect(windowSurface, WHITE, vectors[i])
    
    pygame.draw.rect(windowSurface, YELLOW, player)

    drawText('PlayerPos: x = %d' % (player.x), font, windowSurface, 20, 550)
    drawText('y = %d' % (player.y), font, windowSurface, 400, 550)


    pygame.display.update()
    mainClock.tick(40)
