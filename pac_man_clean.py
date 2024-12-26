import pygame, sys, random
from pygame.locals import *
from collections import defaultdict


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
RED = (255, 0, 0)
GREEN = (0, 255, 0)
ORANGE = (255, 215, 0)

win = False
x = 0
y = 0
value = 0
score = 0
x2 = 0
y2 = 0
xC = 0
yC = 0



lives = 3

#flag variables - boolean
gameOver = False
dead1 = False
dead2 = False
dead3 = False
p1stat = False
p2stat = False
p3stat = False
p4stat = False
eatenB = False
eatenC = False

frightened = False



#pac mans images
playerImage = pygame.image.load('myPacMan.png')
playerImageLeft = pygame.image.load('myPacManLeft.png')
playerImageRight = pygame.image.load('myPacManRight.png')
playerImageUp = pygame.image.load('myPacManUp.png')
playerImageDown = pygame.image.load('myPacManDown.png')
blinkyImageChase = pygame.image.load('blinky4.png')
clydeImageChase = pygame.image.load('clyde.png')
frightenedGhost = pygame.image.load('frightenedGhost.png')
ghostEyes = pygame.image.load('ghostEyes.png')

#pac mans images correctly sized
playerStretchedImage = pygame.transform.scale(playerImage, (16, 16))
playerStretchedLeft = pygame.transform.scale(playerImageLeft, (16, 16))
playerStretchedRight = pygame.transform.scale(playerImageRight, (16, 16))
playerStretchedUp = pygame.transform.scale(playerImageUp, (16, 16))
playerStretchedDown = pygame.transform.scale(playerImageDown, (16, 16))
blinkyStretchedChase = pygame.transform.scale(blinkyImageChase, (15, 15))
clydeStretchedChase = pygame.transform.scale(clydeImageChase, (15, 15))
pelletStretched = pygame.transform.scale(playerImage, (12, 12))
frightenedStretch = pygame.transform.scale(frightenedGhost, (15, 15))
eyesStretched = pygame.transform.scale(ghostEyes, (15, 15))

#list to hold the pac man sized images
image_sprite = [playerStretchedLeft, playerStretchedRight, playerStretchedUp, playerStretchedDown, playerStretchedImage]

mouthToggle = pygame.USEREVENT + 0
pygame.time.set_timer(mouthToggle, 300)


#cookie variables
cookieCount = 0
cookies = []
cookiesEaten = []
FOODSIZE = 5

# y coordinate for starting point of both sets of cookies
j = 34
k = 314


# first set of cookies for the top half of the map
while (j <= 135):
    for i in range(24):
        cookies.append(pygame.Rect((i*20) + 33, j, FOODSIZE, FOODSIZE))
    j = j + 20

# second set of cookies for the bottom half of the map
while (k <= 435):
    for i in range(24):
        cookies.append(pygame.Rect((i*20) + 33, k, FOODSIZE, FOODSIZE))
    k = k + 20

# these two for loops are for the cookies I couldn't reach with the two while loops above
for i in range(8):
    cookies.append(pygame.Rect(114, (i*20) + 150, FOODSIZE, FOODSIZE))
for i in range(8):
    cookies.append(pygame.Rect(394, (i*20)+150, FOODSIZE, FOODSIZE))

#giving the nodes, characters and life spaces coordinates and size
ghost = pygame.Rect(230, 208, 15, 15)
ghostC = pygame.Rect(200, 208, 15, 15)
player = pygame.Rect(270, 310, 15, 15)



life1 = (pygame.Rect(30, 490, 16, 16))
life2 = (pygame.Rect(55, 490, 16, 16))
life3 = (pygame.Rect(80, 490, 16, 16))

n1 = pygame.Rect(30, 30, 10, 10) 
n2 = pygame.Rect(110, 30, 10, 10)
n3 = pygame.Rect(230, 30, 10, 10)
n4 = pygame.Rect(270, 30, 10, 10) 
n5 = pygame.Rect(390, 30, 10, 10)
n6 = pygame.Rect(470, 30, 10, 10)


n7 = pygame.Rect(30, 90, 10, 10)
n8 = pygame.Rect(110, 90, 10, 10)
n9 = pygame.Rect(150, 90, 10, 10)
n10 = pygame.Rect(230, 90, 10, 10)
n11 = pygame.Rect(270, 90, 10, 10)
n12 = pygame.Rect(350, 90, 10, 10)
n13 = pygame.Rect(390, 90, 10, 10)
n14 = pygame.Rect(470, 90, 10, 10)

n15 = pygame.Rect(30, 130, 10, 10)
n16 = pygame.Rect(110, 130, 10, 10)
n17 = pygame.Rect(150, 130, 10, 10)
n18 = pygame.Rect(230, 130, 10, 10)
n19 = pygame.Rect(270, 130, 10, 10)
n20 = pygame.Rect(350, 130, 10, 10)
n21 = pygame.Rect(390, 130, 10, 10)
n22 = pygame.Rect(470, 130, 10, 10)

n23 = pygame.Rect(150, 170, 10, 10)
n24 = pygame.Rect(230, 170, 10, 10)
n25 = pygame.Rect(270, 170, 10, 10)
n26 = pygame.Rect(350, 170, 10, 10)

n27 = pygame.Rect(110, 210, 10, 10)
n28 = pygame.Rect(150, 210, 10, 10)
n29 = pygame.Rect(350, 210, 10, 10)
n30 = pygame.Rect(390, 210, 10, 10)

n31 = pygame.Rect(150, 270, 10, 10)
n32 = pygame.Rect(350, 270, 10, 10)

n33 = pygame.Rect(30, 310, 10, 10)
n34 = pygame.Rect(110, 310, 10, 10)
n35 = pygame.Rect(150, 310, 10, 10)
n36 = pygame.Rect(230, 310, 10, 10)
n37 = pygame.Rect(270, 310, 10, 10)
n38 = pygame.Rect(350, 310, 10, 10)
n39 = pygame.Rect(390, 310, 10, 10)
n40 = pygame.Rect(470, 310, 10, 10)

n41 = pygame.Rect(30, 350, 10, 10)
n42 = pygame.Rect(70, 350, 10, 10)
n43 = pygame.Rect(110, 350, 10, 10)
n44 = pygame.Rect(150, 350, 10, 10)
n63 = pygame.Rect(230, 350, 10, 10)
n64 = pygame.Rect( 270, 350, 10, 10)
n45 = pygame.Rect(350, 350, 10, 10)
n46 = pygame.Rect(390, 350, 10, 10)
n47 = pygame.Rect(430, 350, 10, 10)
n48 = pygame.Rect(470, 350, 10, 10)

n49 = pygame.Rect(30, 390, 10, 10)
n50 = pygame.Rect(70, 390, 10, 10)
n51 = pygame.Rect(110, 390, 10, 10)
n52 = pygame.Rect(150, 390, 10, 10)
n53 = pygame.Rect(230, 390, 10, 10)
n54 = pygame.Rect(270, 390, 10, 10)
n55 = pygame.Rect(350, 390, 10, 10)
n56 = pygame.Rect(390, 390, 10, 10)
n57 = pygame.Rect(430, 390, 10, 10)
n58 = pygame.Rect(470, 390, 10, 10)

n59 = pygame.Rect(30, 430, 10, 10)
n60 = pygame.Rect(230, 430, 10, 10)
n61 = pygame.Rect(270, 430, 10, 10)
n62 = pygame.Rect(470, 430, 10, 10)

nc = pygame.Rect(200, 210, 10, 10)
nb = pygame.Rect(230, 210, 10, 10)
ni = pygame.Rect(270, 210, 10, 10)
np = pygame.Rect(300, 210, 10, 10)

p1 = pygame.Rect(29, 29, 12, 12)
p2 = pygame.Rect(469, 29, 12, 12)
p3 = pygame.Rect(29, 348, 12, 12)
p4 = pygame.Rect(469, 348, 12, 12)


#some variables for character positions
randomPos = 'n18'
next_spotC = nc
ghostCPos = "nc"
closeToPlayer = False


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



a = b = 5 #variables for (x, y) wall coordinates

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
    a = 5


one = False
playerPos = 'n37'

#class to build weighted graph from edges
class Graph():
    def __init__(self):
        """
        self.edges is a dict of all possible next nodes
        e.g. {'X': ['A', 'B', 'C', 'E'], ...}
        self.weights has all the weights between two nodes,
        with the two nodes as a tuple as the key
        e.g. {('X', 'A'): 7, ('X', 'B'): 2, ...}
        """
        self.edges = defaultdict(list)
        self.weights = {}
    
    def add_edge(self, from_node, to_node, weight):
        # Note: assumes edges are bi-directional
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.weights[(from_node, to_node)] = weight
        self.weights[(to_node, from_node)] = weight

#dictionary for nodes, made node checks easier to code
nodes = {
    'n1': n1, 'n2':n2, 'n3':n3, 'n4':n4, 'n5':n5, 'n6':n6,
    'n7':n7, 'n8':n8, 'n9':n9, 'n10':n10, 'n11':n11,
    'n12': n12, 'n13':n13, 'n14':n14, 'n15':n15, 'n16':n16,
    'n17':n17, 'n18':n18, 'n19':n19, 'n20':n20, 'n21':n21,
    'n22':n22, 'n23':n23, 'n24':n24, 'n25':n25, 'n26':n26,
    'n27':n27, 'n28':n28, 'n29':n29, 'n30':n30, 'n31':n31,
    'n32':n32, 'n33':n33, 'n34':n34, 'n35':n35, 'n36':n36,
    'n37':n37, 'n38':n38, 'n39':n39, 'n40':n40, 'n41':n41,
    'n42':n42, 'n43':n43, 'n44':n44, 'n45':n45, 'n46':n46,
    'n47':n47, 'n48':n48, 'n49':n49, 'n50':n50, 'n51':n51,
    'n52':n52, 'n53':n53, 'n54':n54, 'n55':n55, 'n56':n56,
    'n57':n57, 'n58':n58, 'n59':n59, 'n60':n60, 'n61':n61,
    'n62':n62, 'n63':n63, 'n64':n64, 'nc':nc, 'nb':nb, 'ni':ni, 'np':np,
    }

#variables for the graph and the paths we'll get from dijsktra
randomN = nc
graph = Graph()
path = []
pathb= []
pathc = []
pathToPlayer = []

#edges to be used for the weighted graph. Weight represents distance from points
edges = [
    #e1
    ('n1', 'n2', 80),
    ('n2', 'n3', 120),
    ('n4', 'n5', 120),
    ('n5', 'n6', 80),
    ('n1', 'n7', 60),
    ('n2', 'n8', 60),
    ('n3', 'n10', 60),
    ('n4', 'n11', 60),
    ('n5', 'n13', 60),
    #e10
    ('n6', 'n14', 60),
    ('n7', 'n8', 80),
    ('n8', 'n9', 40),
    ('n9', 'n10', 80),
    ('n10', 'n11', 40),
    ('n11', 'n12', 80),
    ('n12', 'n13', 40),
    ('n13', 'n14', 80),
    ('n7', 'n15', 40),
    ('n8', 'n16', 40),
    #e20
    ('n9', 'n17', 40),
    ('n12', 'n20', 40),
    ('n13', 'n21', 40),
    ('n14', 'n22', 40),
    ('n15', 'n16', 80),
    ('n17', 'n18', 80),
    ('n19', 'n20', 80),
    ('n21', 'n22', 80),
    ('n16', 'n27', 80),
    ('n18', 'n24', 40),
    #e30
    ('n19', 'n25', 40),
    ('n21', 'n30', 80),
    ('n23', 'n28', 40),
    ('n23', 'n24', 80),
    ('n24', 'n25', 40),
    ('n25', 'n26', 80),
    ('n26', 'n29', 40),
    ('n27', 'n28', 40),
    ('n29', 'n30', 40),
    ('n27', 'n34', 100),
    #e40
    ('n28', 'n31', 60),
    ('n29', 'n32', 60),
    ('n30', 'n39', 100),
    ('n31', 'n32', 200),
    ('n31', 'n35', 40),
    ('n32', 'n38', 40),
    ('n33', 'n34', 80),
    ('n34', 'n35', 40),
    ('n35', 'n36', 80),
    ('n37', 'n38', 80),
    #e50
    ('n38', 'n39', 40),
    ('n39', 'n40', 80),
    ('n33', 'n41', 40),
    ('n34', 'n43', 40),
    ('n36', 'n63', 40),
    ('n37', 'n64', 40),
    ('n39', 'n46', 40),
    ('n40', 'n48', 40),
    ('n41', 'n42', 40),
    ('n43', 'n44', 40),
    #e60
    ('n44', 'n63', 80),
    ('n63', 'n64', 40),
    ('n64', 'n45', 80),
    ('n45', 'n55', 40),
    ('n45', 'n46', 40),
    ('n47', 'n48', 40),
    ('n42', 'n50', 40),
    ('n43', 'n51', 40),
    ('n44', 'n52', 40),
    ('n46', 'n56', 40),
    #e70
    ('n47', 'n57', 40),
    ('n49', 'n50', 40),
    ('n50', 'n51', 40),
    ('n52', 'n53', 80),
    ('n54', 'n55', 80),
    ('n56', 'n57', 40),
    ('n57', 'n58', 40),
    ('n59', 'n60', 200),
    ('n53', 'n60', 40),
    ('n60', 'n61', 40),
    #e80
    ('n54', 'n61', 40),
    ('n61', 'n62', 200),
    ('n49', 'n59', 40),
    ('n58', 'n62', 40),
    #gh
    ('n24', 'nb', 40),
    ('n25', 'ni', 40),
    ('nc', 'nb', 30),
    ('nb', 'ni', 40),
    ('ni', 'np', 30),
    
]

#adds edges to graph
for edge in edges:
    graph.add_edge(*edge)

#gets the shortest path between two points based on our graphs weighted edges
def dijsktra(graph, initial, end, path):
    # shortest paths is a dict of nodes
    # whose value is a tuple of (previous node, weight)
    
    shortest_paths = {initial: (None, 0)}
    current_node = initial
    visited = set()
    
    while current_node != end:
        visited.add(current_node)
        destinations = graph.edges[current_node]
        weight_to_current_node = shortest_paths[current_node][1]

        for next_node in destinations:
            weight = graph.weights[(current_node, next_node)] + weight_to_current_node
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)
        
        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_destinations:
            return "Route Not Possible"
        # next node is the destination with the lowest weight
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])
    
    # Work back through destinations in shortest path
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        current_node = next_node
    # Reverse path
    path = path[::-1]
    #print(current_node)

    return path
    
playerChange = 0

font = pygame.font.SysFont(None, 48)


#method for drawing text on our window
def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, YELLOW)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

toggle = 0
vulnerable = 0
next_spot = n8


#beginning of game loop
while True:

    #check for events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        #this is to  move pac mans mouth 
        if event.type == mouthToggle:
            toggle = (toggle + 1) % 2

    #moves ghost to the next spot on the path if destination hasn't been reached
    for i in range(len(pathc)):
        if i >= 1:
            if ghostC.x != next_spotC.x:
                if ghostC.x > next_spotC.x:
                    xC = -1
                    yC = 0
                if ghostC.x < next_spotC.x:
                    xC = 1.5
                    yC = 0
        
            if ghostC.y != next_spotC.y:
                if ghostC.y > next_spotC.y:
                    yC = -1
                    xC = 0
                if ghostC.y < next_spotC.y:
                    yC = 1.5
                    xC = 0

    #same as above but for blinky
    for i in range(len(pathb)):
        if i >= 1:
            if ghost.x != next_spot.x:
                if ghost.x > next_spot.x:
                    x = -1
                    y = 0
                if ghost.x < next_spot.x:
                    x = 1.5
                    y = 0
        
            if ghost.y != next_spot.y:
                if ghost.y > next_spot.y:
                    y = -1
                    x = 0
                if ghost.y < next_spot.y:
                    y = 1.5
                    x = 0
        #this is for chasing pac man between two nodes when path is empty
        if i < 1:
            if ghostPos == playerPos:
                if ghost.x > player.x:
                    x = -1
                    y = 0
                if ghost.x < player.x:
                    x = 1.5
                    y = 0
                if ghost.y > player.y:
                    y = -1
                    x = 0
                if ghost.y < player.y:
                    y = 1.5
                    x = 0
                    
    #moves ghosts 
    if gameOver == False:
        ghost.x += x
        ghost.y += y
        ghostC.x += xC
        ghostC.y += yC

    #what clyde should do if not eaten
    if eatenC == False:
        for i in nodes:
            #what clyde should do if not eaten or frightened
            if frightened == False:
                if ghostC.contains(nodes[i]):
                    #if clyde is not close to player he will chase player
                    if closeToPlayer == False:
                        ghostCPos= ''+i+''
                        key_list = list(nodes.keys())
                        value_list = list(nodes.values())
                        path = []
                        pathc = []
                        
                        dijsktra(graph, playerPos, ghostCPos, path)
                        pathc = path
                        if len(pathc) > 1:
                            next_spotC = nodes.get(pathc[1])
                        if len(pathc) < 3:
                            closeToPlayer = True
                        #if clyde gets to players position, which shouldn't happen
                        else:
                            if ghostCPos == playerPos:
                                if ghostC.x > player.x:
                                    xC = -1
                                    yC = 0
                                if ghostC.x < player.x:
                                    xC = 1.5
                                    yC = 0
                                if ghostC.y > player.y:
                                    yC = -1
                                    xC = 0
                                if ghostC.y < player.y:
                                    yC = 1.5
                                    xC = 0
                    # if clyde gets too close to player his target will change to random
                    else:
                        ghostCPos = ''+i+''
                        tempPos = randomPos
                        randomN = random.randint(1, 63)
                        key_list = list(nodes.keys())
                        value_list = list(nodes.values())
                        path = []
                        pathc = []
                    
                        dijsktra(graph, tempPos, ghostCPos, path)
                        pathc = path
                        if len(pathc) > 1:
                            next_spotC = nodes.get(pathc[1])
                        else:
                            closeToPlayer = False
            #frightened clyde will go to random nodes
            else:
                for i in nodes:
                    if ghostC.contains(nodes[i]):
                        ghostCPos = ''+i+''
                        tempPos = randomPos
                        randomN = random.randint(1, 63)
                        key_list = list(nodes.keys())
                        value_list = list(nodes.values())
                        path = []
                        pathc = []
                        dijsktra(graph, tempPos, ghostCPos, path)
                        pathc = path
                    
                        if len(pathc) < 2:
                            randomPos = ''+key_list[randomN]+''
                            dijsktra(graph, randomPos, ghostCPos, path)
                        next_spotC = nodes.get(pathc[1])

    #code for blinky if he is not eaten                    
    if eatenB == False:
        for i in nodes:
            #blinky will go to random node if frightened
            if frightened == True:
                if ghost.contains(nodes[i]):
                    ghostPos = ''+i+''
                    tempPos2 = randomPos
                    randomN = random.randint(1, 63)
                    key_list = list(nodes.keys())
                    value_list = list(nodes.values())
                    path = []
                    pathb = []
                    dijsktra(graph, tempPos2, ghostPos, path)
                    pathb = path
        
                    if len(pathb) < 2:
                        randomPos = ''+key_list[randomN]+''
                        dijsktra(graph, randomPos, ghostPos, path)
                    next_spot = nodes.get(pathb[1])

                #this is basically a timer for frightened mode
                if playerChange >= 50:
                    frightened = False
           

            #if blinky is not frightened or eaten he will just chase player
            else:
                for j in nodes:
                    if ghost.contains(nodes[j]):
                        ghostPos= ''+j+''
                        key_list = list(nodes.keys())
                        value_list = list(nodes.values())
                        path = []
                        pathb = []
                        dijsktra(graph, playerPos, ghostPos, path)
                        pathb = path
                        if len(pathb) > 1:
                            next_spot = nodes.get(pathb[1])


                
            
    #print(next_spot)
            
    #timer for frightened mode
    for i in nodes:
        if ghost.contains(nodes[i]):
            playerChange = playerChange + 1
            
    #this gives player position whenever they collide with a node
    for i in nodes:
        if player.contains(nodes[i]):
            playerPos = ''+i+''


    #value determines which pacman sprite to show and is based on pressed key
    if value >= len(image_sprite):
        value = 0

    if toggle == 0:
        image = image_sprite[value]
    if toggle == 1:
        image = playerStretchedImage

    #variable to hold specific key pressed
    key = pygame.key.get_pressed()

    #pac man movement from pressed keys
    if gameOver == False:
        if key[pygame.K_LEFT]:
                x2 = -1.3
                y2 = 0
                value = 0
            
        if key[pygame.K_RIGHT]:
                x2 = 2
                y2 = 0
                value = 1
        
        if key[pygame.K_UP]:
                x2 = 0
                y2 = -1.3
                value = 2

        if key[pygame.K_DOWN]:
                x2 = 0
                y2 = 2
                value = 3

    #movement - adjusts players coordinates based on pressed key
    player.x += x2
    player.y += y2

    #checks players direction and prevents them from going through a wall
    for wall in walls:
        if player.colliderect(wall.rect):
            if x2 > 0:
                player.right = wall.rect.left
            if x2 < 0:
                player.left = wall.rect.right
            if y2 < 0:
                player.top = wall.rect.bottom
            if y2 > 0:
                player.bottom = wall.rect.top
                
        #wall collision for blinky
        if ghost.colliderect(wall.rect):
            if x > 0:
                ghost.right = wall.rect.left
                ghost.x = ghost.x - 1
                path = []
                dijsktra(graph, playerPos, ghostPos, path)
            if x < 0:
                ghost.left = wall.rect.right
                ghost.x = ghost.x + 1
                path = []
                dijsktra(graph, playerPos, ghostPos, path)
            if y < 0:
                ghost.top = wall.rect.bottom
                ghost.x = ghost.x - 1
                path = []
                dijsktra(graph, playerPos, ghostPos, path)
            if y > 0:
                ghost.bottom = wall.rect.top
                ghost.x = ghost.x + 1
                path = []
                dijsktra(graph, playerPos, ghostPos, path)
                
        #wall collision for clyde
        if ghostC.colliderect(wall.rect):
            if x > 0:
                ghostC.right = wall.rect.left
                path = []
                dijsktra(graph, tempPos, ghostCPos, path)
            if x < 0:
                ghostC.left = wall.rect.right
                path = []
                dijsktra(graph, tempPos, ghostCPos, path)
            if y < 0:
                ghostC.top = wall.rect.bottom
                path = []
                dijsktra(graph, tempPos, ghostCPos, path)
            if y > 0:
                ghostC.bottom = wall.rect.top
                path = []
                dijsktra(graph, tempPos, ghostCPos, path)
                
    #map exits for player warps them to other side
    if player.x <= 0:
        player.x = 488

    if player.x >= 490:
        player.x = 2

    #draw the rects for nodes
    for i in nodes:
        pygame.draw.rect(windowSurface, WHITE, nodes.get(i))


    windowSurface.fill(BLACK)


    # if player collides with cookies: delete cookie, increase score and cookieCount
    for cookie in cookies[:]:
        if player.colliderect(cookie):
            cookies.remove(cookie)
            score = score + 10
            cookieCount = cookieCount + 1

    #draw the cookies
    for i in range(len(cookies)):
        pygame.draw.rect(windowSurface, WHITE, cookies[i])

    #draws the power pellets
    windowSurface.blit(pelletStretched, p1)
    windowSurface.blit(pelletStretched, p2)
    windowSurface.blit(pelletStretched, p3)
    windowSurface.blit(pelletStretched, p4)

    #This section is for pac man eating a power pellet
    if player.colliderect(p1) and p1stat == False:
        playerChange = 0
        frightened = True
        p1stat = True
    if p1stat == True:
        pygame.draw.rect(windowSurface, BLACK, p1)

    if player.colliderect(p2) and p2stat == False:
        playerChange = 0
        frightened = True
        p2stat = True
    if p2stat == True:
        pygame.draw.rect(windowSurface, BLACK, p2)

    if player.colliderect(p3) and p3stat == False:
        playerChange = 0
        frightened = True
        p3stat = True
    if p3stat == True:
        pygame.draw.rect(windowSurface, BLACK, p3)

    if player.colliderect(p4) and p4stat == False:
        playerChange = 0
        frightened = True
        p4stat = True
    if p4stat == True:
        pygame.draw.rect(windowSurface, BLACK, p4)
        
    

    #build maze from list
    for wall in walls:
        pygame.draw.rect(windowSurface, (0, 0, 255), wall.rect)
    
    windowSurface.blit(image, player)
    windowSurface.blit(blinkyStretchedChase, ghost)
    windowSurface.blit(clydeStretchedChase, ghostC)
    
    windowSurface.blit(playerStretchedImage, life1)
    windowSurface.blit(playerStretchedImage, life2)
    windowSurface.blit(playerStretchedImage, life3)

    #draw the text for the scoreboard using the drawText method
    drawText('Score: %s' % (score), font, windowSurface, 20, 520)

    #message displayed after eating all of the cookies
    if cookieCount >= 201:
        win = True
        gameOver = True

    #if ghosts catch pac man
    if frightened == False:
        if ghost.colliderect(player) or ghostC.colliderect(player):
            if lives == 0:
                win = False
                gameOver = True
            else:
                if lives == 3:
                    dead3 = True
                    
                if lives == 2:
                    dead2 = True
                    
                if lives == 1:
                    dead1 = True

                ghost.x = 230
                ghost.y = 208
                player.x = 270
                player.y = 310
                ghostC.x = 200
                ghostC.y = 210
                path = []
                next_spotC = nb
                    
            lives = lives - 1

    #frightened mode
    if frightened == True:
        windowSurface.blit(frightenedStretch, ghost)
        windowSurface.blit(frightenedStretch, ghostC)
        if ghost.colliderect(player):
            eatenB = True
        if ghostC.colliderect(player):
            eatenC = True

    #what happens if pac man eats ghosts
    if eatenB == True:
        windowSurface.blit(eyesStretched, ghost)
        for j in nodes:
            if ghost.contains(nodes[j]):
                ghostPos = ''+j+''
                key_list = list(nodes.keys())
                value_list = list(nodes.values())
                path = []
                pathb = []
                dijsktra(graph, 'nb', ghostPos, path)
                pathb = path
                if len(pathb) > 1:
                    next_spot = nodes.get(pathb[1])
                else:
                    eatenB = False

    if eatenC == True:
        windowSurface.blit(eyesStretched, ghostC)
        for i in nodes:
            if ghostC.contains(nodes[i]):
                ghostCPos = ''+i+''
                key_list = list(nodes.keys())
                value_list = list(nodes.values())
                path = []
                pathc = []
                dijsktra(graph, 'nc', ghostCPos, path)
                pathc = path
                if len(pathc) > 1:
                    next_spotC = nodes.get(pathc[1])
                else:
                    eatenC = False   


    if dead3 == True:
        pygame.draw.rect(windowSurface, BLACK, life3)
    if dead2 == True:
        pygame.draw.rect(windowSurface, BLACK, life2)
    if dead1 == True:
        pygame.draw.rect(windowSurface, BLACK, life1)
            
    if gameOver == True:
        x = 0
        y = 0
        x2 = 0
        y2 = 0
        xC = 0
        yC = 0
        if win == False:
            drawText('Game Over!', font, windowSurface, 300, 520)
        if win == True:
            drawText('You Win!', font, windowSurface, 300, 520)


    pygame.display.update()
    mainClock.tick(40)
