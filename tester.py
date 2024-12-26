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

#pac mans images
playerImage = pygame.image.load('myPacMan.png')
playerImageLeft = pygame.image.load('myPacManLeft.png')
playerImageRight = pygame.image.load('myPacManRight.png')
playerImageUp = pygame.image.load('myPacManUp.png')
playerImageDown = pygame.image.load('myPacManDown.png')

#pac mans images correctly sized
playerStretchedImage = pygame.transform.scale(playerImage, (18, 18))
playerStretchedLeft = pygame.transform.scale(playerImageLeft, (18, 18))
playerStretchedRight = pygame.transform.scale(playerImageRight, (18, 18))
playerStretchedUp = pygame.transform.scale(playerImageUp, (18, 18))
playerStretchedDown = pygame.transform.scale(playerImageDown, (18, 18))

#list to hold the pac man sized images
image_sprite = [playerStretchedLeft, playerStretchedRight, playerStretchedUp, playerStretchedDown, playerStretchedImage]

mouthToggle = pygame.USEREVENT + 0
pygame.time.set_timer(mouthToggle, 300)

#cookie variables
cookieCount = 0
cookies = []
cookiesEaten = []
FOODSIZE = 5

# j = y, k = x for crosshair
kX = 150
jY = 90


# first set of cookies for the top half of the map
#while (j <= 141):
    #for i in range(23):
        #cookies.append(pygame.Rect((i*22) + 31, j, FOODSIZE, FOODSIZE))
    #j = j + 22

# second set of cookies for the bottom half of the map
#while (k <= 490):
    #for i in range(23):
        #cookies.append(pygame.Rect((i*22) + 31, k, FOODSIZE, FOODSIZE))
    #k = k + 22

# these two for loops are for the cookies I couldn't reach with the two while loops above
#for i in range(8):
    #cookies.append(pygame.Rect(119, (i*22) + 163, FOODSIZE, FOODSIZE))
#for i in range(8):
    #cookies.append(pygame.Rect(427, (i*22)+163, FOODSIZE, FOODSIZE))

#crosshairs
for i in range(550):
    cookies.append(pygame.Rect(i, jY, 1, 1))

for i in range(600):
    cookies.append(pygame.Rect(kX, i, 1, 1))



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
player = pygame.Rect(265, 287, 18, 18)
tester = pygame.Rect(121, 30, 1, 1)

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
        if event.type == mouthToggle:
            toggle = (toggle + 1) % 2
            

    #value determines which pacman sprite to show and is based on pressed key
    if value >= len(image_sprite):
        value = 0

    #image = image_sprite[value]

    if toggle == 0:
        image = image_sprite[value]
    if toggle == 1:
        image = playerStretchedImage
            
    #variable to hold specific key pressed
    key = pygame.key.get_pressed()

    if key[pygame.K_LEFT]:
            x = -1.5
            y = 0
            value = 0
            
    if key[pygame.K_RIGHT]:
            x = 2
            y = 0
            value = 1
        
    if key[pygame.K_UP]:
            x = 0
            y = -1.5
            value = 2

    if key[pygame.K_DOWN]:
            x = 0
            y = 2
            value = 3

    #movement - adjusts players coordinates based on pressed key
    player.x += x
    player.y += y


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


    if player.x <= 0:
        player.x = 530

    if player.x >= 532:
        player.x = 2
    
    
    #black background
    windowSurface.fill(BLACK)

    # if player collides with cookies: delete cookie, increase score and cookieCount
    #for cookie in cookies[:]:
        #if player.colliderect(cookie):
            #cookies.remove(cookie)
            #score = score + 10
            #cookieCount = cookieCount + 1

    #draw the cookies
    for i in range(len(cookies)):
        pygame.draw.rect(windowSurface, WHITE, cookies[i])

    #draw the player with the images
    windowSurface.blit(image, player)
    pygame.draw.rect(windowSurface, YELLOW, tester)
    

    #draw the text for the scoreboard using the drawText method
    drawText('Score: %s' % (score), font, windowSurface, 20, 520)
    drawText('PlayerPos: x = %d' % (player.x), font, windowSurface, 20, 550)
    drawText('y = %d' % (player.y), font, windowSurface, 400, 550)

    #build maze from list
    for wall in walls:
        pygame.draw.rect(windowSurface, (0, 0, 255), wall.rect)

    #message displayed after eating all of the cookies
    #if cookieCount >= 201:
        #drawText('You Win!', font, windowSurface, 400, 520)


    pygame.display.update()
    mainClock.tick(40)
