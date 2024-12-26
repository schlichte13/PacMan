import pygame, sys, random, time
from pygame.locals import *

# set up pygame
pygame.init()
mainClock = pygame.time.Clock()

#set up the window
WINDOWWIDTH = 550
WINDOWHEIGHT = 600
FOODSIZE = 5
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Pac-Man')


# set up the colors
BLACK = (0, 0, 0)
YELLOW = (255, 200, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
TEXTCOLOR = (255, 200, 0)

# set up movement variables
x = 0
y = 0
cookieCount = 0
score = 0


# pac man image
playerImage = pygame.image.load('myPacMan.png')
playerImageLeft = pygame.image.load('myPacManLeft.png')
playerImageRight = pygame.image.load('myPacManRight.png')
playerImageUp = pygame.image.load('myPacManUp.png')
playerImageDown = pygame.image.load('myPacManDown.png')
                                     
playerStretchedImage = pygame.transform.scale(playerImage, (18, 18))
playerStretchedLeft = pygame.transform.scale(playerImageLeft, (18, 18))
playerStretchedRight = pygame.transform.scale(playerImageRight, (18, 18))
playerStretchedUp = pygame.transform.scale(playerImageUp, (18, 18))
playerStretchedDown = pygame.transform.scale(playerImageDown, (18, 18))


image_sprite = [playerStretchedLeft, playerStretchedRight, playerStretchedUp, playerStretchedDown, playerStretchedImage]

    
newClock = pygame.time.Clock()

value = 0

                                
direction = playerStretchedImage

# cookies
cookies = []
cookiesEaten = []
j = 31
k = 340


while (j <= 141):
    for i in range(23):
        cookies.append(pygame.Rect((i*22) + 31, j, FOODSIZE, FOODSIZE))
    j = j + 22

while (k <= 490):
    for i in range(23):
        cookies.append(pygame.Rect((i*22) + 31, k, FOODSIZE, FOODSIZE))
    k = k + 22

for i in range(8):
    cookies.append(pygame.Rect(119, (i*22) + 163, FOODSIZE, FOODSIZE))
for i in range(8):
    cookies.append(pygame.Rect(427, (i*22)+163, FOODSIZE, FOODSIZE))






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

#parse the level into the wall array
a = b = 0
for row in level:
    for col in row:
        if col == "W":
            Wall((a, b))
        a += 22
    b += 22
    a = 0


# draw the player onto the surface
player = pygame.Rect(156, 177, 18, 18)

font = pygame.font.SysFont(None, 48)

text = 'Score: '
#pygame.display.update()

def drawText(text, font, surface, x, y):
    #render creates a surface object for the text to be on
    textobj = font.render(text, 1, TEXTCOLOR)
    #gets size and location of surface object
    textrect = textobj.get_rect()
    #where to start drawing the text
    textrect.topleft = (x, y)
    #blit draws an image onto another (text on surface object)
    surface.blit(textobj, textrect)



# run the game loop
while True:
    # check for events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #newClock.tick(1)
    if value >= len(image_sprite):
        value = 0

    image = image_sprite[value]

            
    # handles the keyboard input
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
            

    #checks if player collides with wall then redirects
    if x != 0:
        player.x += x
        player.y += y
        if x > 0:
            direction = playerStretchedRight
        if x < 0:
            direction = playerStretchedLeft
        
        for wall in walls:
            if player.colliderect(wall.rect):
                if x > 0:
                    player.right = wall.rect.left
                if x < 0:
                    player.left = wall.rect.right 

    if y != 0:
        player.x += x
        player.y += y
        if y < 0:
            direction = playerStretchedUp
        if y > 0:
            direction = playerStretchedDown
        
        for wall in walls:
            if player.colliderect(wall.rect): 
                if y < 0:
                    player.top = wall.rect.bottom
                if y > 0:
                    player.bottom = wall.rect.top
    
                
    # draw the black background onto the surface
    windowSurface.fill(BLACK)


    # collision with cookies
    for cookie in cookies[:]:
        if player.colliderect(cookie):
            cookies.remove(cookie)
            score = score + 10
            cookieCount = cookieCount + 1

    #if player.rect.colliderect(cookie_rect):
        

    # draw the cookies
    for i in range(len(cookies)):
        pygame.draw.rect(windowSurface, WHITE, cookies[i])
   
    
    # draw the wall from the array
    for wall in walls:
        pygame.draw.rect(windowSurface, (0, 0, 255), wall.rect)
        

    windowSurface.blit(image, player)
    #windowSurface.blit(playerStretchedImage, player)
    #pygame.display.update()
    #direction = playerStretchedImage

    
    #pygame.draw.rect(windowSurface, YELLOW, player)
    drawText('Score: %s' % (score), font, windowSurface, 20, 520)
    
    # draw the wall from the array
    for wall in walls:
        pygame.draw.rect(windowSurface, (0, 0, 255), wall.rect)

    #if cookieCount >= 201:
    if cookieCount >= 201:
        drawText('You Win!', font, windowSurface, 400, 520)
        
    pygame.display.update()
    mainClock.tick(40)


