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

gameOver = False


#pac mans images
playerImage = pygame.image.load('myPacMan.png')
playerImageLeft = pygame.image.load('myPacManLeft.png')
playerImageRight = pygame.image.load('myPacManRight.png')
playerImageUp = pygame.image.load('myPacManUp.png')
playerImageDown = pygame.image.load('myPacManDown.png')
blinkyImageChase = pygame.image.load('blinky4.png')

#pac mans images correctly sized
playerStretchedImage = pygame.transform.scale(playerImage, (16, 16))
playerStretchedLeft = pygame.transform.scale(playerImageLeft, (16, 16))
playerStretchedRight = pygame.transform.scale(playerImageRight, (16, 16))
playerStretchedUp = pygame.transform.scale(playerImageUp, (16, 16))
playerStretchedDown = pygame.transform.scale(playerImageDown, (16, 16))
blinkyStretchedChase = pygame.transform.scale(blinkyImageChase, (15, 15))

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


ghost = pygame.Rect(30, 30, 12, 12)
player = pygame.Rect(270, 310, 16, 16)


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
ghostPos = 'n1'
#var = A

#playerPos

#ghostPos

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


graph = Graph()
path = []
#next_node = B
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
    
]


for edge in edges:
    graph.add_edge(*edge)


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
    #path = []
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        current_node = next_node
    # Reverse path
    path = path[::-1]
    #print(current_node)

    return path
    


font = pygame.font.SysFont(None, 48)


#method for drawing text on our window
def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, YELLOW)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

toggle = 0
next_spot = n8

while True:

    #check for events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == mouthToggle:
            toggle = (toggle + 1) % 2
    
    for i in range(len(path)):
        if i >= 1:
            if path[1] == 'n1':
                next_spot = n1
            if path[1] == 'n2':
                next_spot = n2
            if path[1] == 'n3':
                next_spot = n3
            if path[1] == 'n4':
                next_spot = n4
            if path[1] == 'n5':
                next_spot = n5
            if path[1] == 'n6':
                next_spot = n6
            if path[1] == 'n7':
                next_spot = n7
            if path[1] == 'n8':
                next_spot = n8
            if path[1] == 'n9':
                next_spot = n9
            if path[1] == 'n10':
                next_spot = n10
            if path[1] == 'n11':
                next_spot = n11
            if path[1] == 'n12':
                next_spot = n12
            if path[1] == 'n13':
                next_spot = n13
            if path[1] == 'n14':
                next_spot = n14
            if path[1] == 'n15':
                next_spot = n15
            if path[1] == 'n16':
                next_spot = n16
            if path[1] == 'n17':
                next_spot = n17
            if path[1] == 'n18':
                next_spot = n18
            if path[1] == 'n19':
                next_spot = n19
            if path[1] == 'n20':
                next_spot = n20
            if path[1] == 'n21':
                next_spot = n21
            if path[1] == 'n22':
                next_spot = n22
            if path[1] == 'n23':
                next_spot = n23
            if path[1] == 'n24':
                next_spot = n24
            if path[1] == 'n25':
                next_spot = n25
            if path[1] == 'n26':
                next_spot = n26
            if path[1] == 'n27':
                next_spot = n27
            if path[1] == 'n28':
                next_spot = n28
            if path[1] == 'n29':
                next_spot = n29
            if path[1] == 'n30':
                next_spot = n30
            if path[1] == 'n31':
                next_spot = n31
            if path[1] == 'n32':
                next_spot = n32
            if path[1] == 'n33':
                next_spot = n33
            if path[1] == 'n34':
                next_spot = n34
            if path[1] == 'n35':
                next_spot = n35
            if path[1] == 'n36':
                next_spot = n36
            if path[1] == 'n37':
                next_spot = n37
            if path[1] == 'n38':
                next_spot = n38
            if path[1] == 'n39':
                next_spot = n39
            if path[1] == 'n40':
                next_spot = n40
            if path[1] == 'n41':
                next_spot = n41
            if path[1] == 'n42':
                next_spot = n42
            if path[1] == 'n43':
                next_spot = n43
            if path[1] == 'n44':
                next_spot = n44
            if path[1] == 'n45':
                next_spot = n45
            if path[1] == 'n46':
                next_spot = n46
            if path[1] == 'n47':
                next_spot = n47
            if path[1] == 'n48':
                next_spot = n48
            if path[1] == 'n49':
                next_spot = n49
            if path[1] == 'n50':
                next_spot = n50
            if path[1] == 'n51':
                next_spot = n51
            if path[1] == 'n52':
                next_spot = n52
            if path[1] == 'n53':
                next_spot = n53
            if path[1] == 'n54':
                next_spot = n54
            if path[1] == 'n55':
                next_spot = n55
            if path[1] == 'n56':
                next_spot = n56
            if path[1] == 'n57':
                next_spot = n57
            if path[1] == 'n58':
                next_spot = n58
            if path[1] == 'n59':
                next_spot = n59
            if path[1] == 'n60':
                next_spot = n60
            if path[1] == 'n61':
                next_spot = n61
            if path[1] == 'n62':
                next_spot = n62
            if path[1] == 'n63':
                next_spot = n63
            if path[i] == 'n64':
                next_spot = n64
            
        
            if ghost.x != next_spot.x:
                if ghost.x > next_spot.x:
                    x = -1
                    y = 0
                if ghost.x < next_spot.x:
                    x = 1
                    y = 0
        
            if ghost.y != next_spot.y:
                if ghost.y > next_spot.y:
                    y = -1
                    x = 0
                if ghost.y < next_spot.y:
                    y = 1
                    x = 0
            
        if i < 1:
            if ghostPos == playerPos:
                if ghost.x > player.x:
                    x = -1
                    y = 0
                if ghost.x < player.x:
                    x = 1
                    y = 0
                if ghost.y > player.y:
                    y = -1
                    x = 0
                if ghost.y < player.y:
                    y = 1
                    x = 0

    if gameOver == False:
        ghost.x += x
        ghost.y += y
    

    if ghost.contains(n1):
        path = []
        ghostPos = 'n1'
        dijsktra(graph, playerPos, ghostPos, path)

    if ghost.contains(n2):
        path = []
        ghostPos = 'n2'
        dijsktra(graph, playerPos, ghostPos, path)
        
    if ghost.contains(n3):
        path = []
        ghostPos = 'n3'
        dijsktra(graph, playerPos, ghostPos, path)
        
    if ghost.contains(n4):
        path = []
        ghostPos = 'n4'
        dijsktra(graph, playerPos, ghostPos, path)

    if ghost.contains(n5):
        path = []
        ghostPos = 'n5'
        dijsktra(graph, playerPos, ghostPos, path)
        
    if ghost.contains(n6):
        path = []
        ghostPos = 'n6'
        dijsktra(graph, playerPos, ghostPos, path)
        
    if ghost.contains(n7):
        path = []
        ghostPos = 'n7'
        dijsktra(graph, playerPos, ghostPos, path)
        
    if ghost.contains(n8):
        path = []
        ghostPos = 'n8'
        dijsktra(graph, playerPos, ghostPos, path)

    if ghost.contains(n9):
        path = []
        ghostPos = 'n9'
        dijsktra(graph, playerPos, ghostPos, path)

    if ghost.contains(n10):
        path = []
        ghostPos = 'n10'
        dijsktra(graph, playerPos, ghostPos, path)

    if ghost.contains(n11):
        path = []
        ghostPos = 'n11'
        dijsktra(graph, playerPos, ghostPos, path)

    if ghost.contains(n12):
        path = []
        ghostPos = 'n12'
        dijsktra(graph, playerPos, ghostPos, path)
        
    if ghost.contains(n13):
        path = []
        ghostPos = 'n13'
        dijsktra(graph, playerPos, ghostPos, path)
        
    if ghost.contains(n14):
        path = []
        ghostPos = 'n14'
        dijsktra(graph, playerPos, ghostPos, path)

    if ghost.contains(n15):
        path = []
        ghostPos = 'n15'
        dijsktra(graph, playerPos, ghostPos, path)
        
    if ghost.contains(n16):
        path = []
        ghostPos = 'n16'
        dijsktra(graph, playerPos, ghostPos, path)
        
    if ghost.contains(n17):
        path = []
        ghostPos = 'n17'
        dijsktra(graph, playerPos, ghostPos, path)
        
    if ghost.contains(n18):
        path = []
        ghostPos = 'n18'
        dijsktra(graph, playerPos, ghostPos, path)

    if ghost.contains(n19):
        path = []
        ghostPos = 'n19'
        dijsktra(graph, playerPos, ghostPos, path)

    if ghost.contains(n20):
        path = []
        ghostPos = 'n20'
        dijsktra(graph, playerPos, ghostPos, path)

    if ghost.contains(n21):
        path = []
        ghostPos = 'n21'
        dijsktra(graph, playerPos, ghostPos, path)

    if ghost.contains(n22):
        path = []
        ghostPos = 'n22'
        dijsktra(graph, playerPos, ghostPos, path)
        
    if ghost.contains(n23):
        path = []
        ghostPos = 'n23'
        dijsktra(graph, playerPos, ghostPos, path)
        
    if ghost.contains(n24):
        path = []
        ghostPos = 'n24'
        dijsktra(graph, playerPos, ghostPos, path)

    if ghost.contains(n25):
        path = []
        ghostPos = 'n25'
        dijsktra(graph, playerPos, ghostPos, path)
        
    if ghost.contains(n26):
        path = []
        ghostPos = 'n26'
        dijsktra(graph, playerPos, ghostPos, path)
        
    if ghost.contains(n27):
        path = []
        ghostPos = 'n27'
        dijsktra(graph, playerPos, ghostPos, path)
        
    if ghost.contains(n28):
        path = []
        ghostPos = 'n28'
        dijsktra(graph, playerPos, ghostPos, path)

    if ghost.contains(n29):
        path = []
        ghostPos = 'n29'
        dijsktra(graph, playerPos, ghostPos, path)

    if ghost.contains(n30):
        path = []
        ghostPos = 'n30'
        dijsktra(graph, playerPos, ghostPos, path)

    if ghost.contains(n31):
        path = []
        ghostPos = 'n31'
        dijsktra(graph, playerPos, ghostPos, path)

    if ghost.contains(n32):
        path = []
        ghostPos = 'n32'
        dijsktra(graph, playerPos, ghostPos, path)
        
    if ghost.contains(n33):
        path = []
        ghostPos = 'n33'
        dijsktra(graph, playerPos, ghostPos, path)
        
    if ghost.contains(n34):
        path = []
        ghostPos = 'n34'
        dijsktra(graph, playerPos, ghostPos, path)

    if ghost.contains(n35):
        path = []
        ghostPos = 'n35'
        dijsktra(graph, playerPos, ghostPos, path)
        
    if ghost.contains(n36):
        path = []
        ghostPos = 'n36'
        dijsktra(graph, playerPos, ghostPos, path)
        
    if ghost.contains(n37):
        path = []
        ghostPos = 'n37'
        dijsktra(graph, playerPos, ghostPos, path)
        
    if ghost.contains(n38):
        path = []
        ghostPos = 'n38'
        dijsktra(graph, playerPos, ghostPos, path)

    if ghost.contains(n39):
        path = []
        ghostPos = 'n39'
        dijsktra(graph, playerPos, ghostPos, path)

    if ghost.contains(n40):
        path = []
        ghostPos = 'n40'
        dijsktra(graph, playerPos, ghostPos, path)

    if ghost.contains(n41):
        path = []
        ghostPos = 'n41'
        dijsktra(graph, playerPos, ghostPos, path)

    if ghost.contains(n42):
        path = []
        ghostPos = 'n42'
        dijsktra(graph, playerPos, ghostPos, path)
        
    if ghost.contains(n43):
        path = []
        ghostPos = 'n43'
        dijsktra(graph, playerPos, ghostPos, path)
        
    if ghost.contains(n44):
        path = []
        ghostPos = 'n44'
        dijsktra(graph, playerPos, ghostPos, path)

    if ghost.contains(n45):
        path = []
        ghostPos = 'n45'
        dijsktra(graph, playerPos, ghostPos, path)
        
    if ghost.contains(n46):
        path = []
        ghostPos = 'n46'
        dijsktra(graph, playerPos, ghostPos, path)
        
    if ghost.contains(n47):
        path = []
        ghostPos = 'n47'
        dijsktra(graph, playerPos, ghostPos, path)
        
    if ghost.contains(n48):
        path = []
        ghostPos = 'n48'
        dijsktra(graph, playerPos, ghostPos, path)

    if ghost.contains(n49):
        path = []
        ghostPos = 'n49'
        dijsktra(graph, playerPos, ghostPos, path)

    if ghost.contains(n50):
        path = []
        ghostPos = 'n50'
        dijsktra(graph, playerPos, ghostPos, path)

    if ghost.contains(n51):
        path = []
        ghostPos = 'n51'
        dijsktra(graph, playerPos, ghostPos, path)

    if ghost.contains(n52):
        path = []
        ghostPos = 'n52'
        dijsktra(graph, playerPos, ghostPos, path)
        
    if ghost.contains(n53):
        path = []
        ghostPos = 'n53'
        dijsktra(graph, playerPos, ghostPos, path)
        
    if ghost.contains(n54):
        path = []
        ghostPos = 'n54'
        dijsktra(graph, playerPos, ghostPos, path)

    if ghost.contains(n55):
        path = []
        ghostPos = 'n55'
        dijsktra(graph, playerPos, ghostPos, path)
        
    if ghost.contains(n56):
        path = []
        ghostPos = 'n56'
        dijsktra(graph, playerPos, ghostPos, path)
        
    if ghost.contains(n57):
        path = []
        ghostPos = 'n57'
        dijsktra(graph, playerPos, ghostPos, path)
        
    if ghost.contains(n58):
        path = []
        ghostPos = 'n58'
        dijsktra(graph, playerPos, ghostPos, path)

    if ghost.contains(n59):
        path = []
        ghostPos = 'n59'
        dijsktra(graph, playerPos, ghostPos, path)

    if ghost.contains(n60):
        path = []
        ghostPos = 'n60'
        dijsktra(graph, playerPos, ghostPos, path)

    if ghost.contains(n61):
        path = []
        ghostPos = 'n61'
        dijsktra(graph, playerPos, ghostPos, path)

    if ghost.contains(n62):
        path = []
        ghostPos = 'n62'
        dijsktra(graph, playerPos, ghostPos, path)

    if ghost.contains(n63):
        path = []
        ghostPos = 'n63'
        dijsktra(graph, playerPos, ghostPos, path)

    if ghost.contains(n64):
        path = []
        ghostPos = 'n64'
        dijsktra(graph, playerPos, ghostPos, path)


    if player.colliderect(n1):
        playerPos = 'n1'

    if player.colliderect(n2):
        playerPos = 'n2'
        
    if player.colliderect(n3):
        playerPos = 'n3'
        
    if player.colliderect(n4):
        playerPos = 'n4'
        
    if player.colliderect(n5):
        playerPos = 'n5'
        
    if player.colliderect(n6):
        playerPos = 'n6'
        
    if player.colliderect(n7):
        playerPos = 'n7'
        
    if player.colliderect(n8):
        playerPos = 'n8'

    if player.colliderect(n9):
        playerPos = 'n9'

    if player.colliderect(n10):
        playerPos = 'n10'

    if player.colliderect(n11):
        playerPos = 'n11'

    if player.colliderect(n12):
        playerPos = 'n12'
        
    if player.colliderect(n13):
        playerPos = 'n13'
        
    if player.colliderect(n14):
        playerPos = 'n14'
        
    if player.colliderect(n15):
        playerPos = 'n15'
        
    if player.colliderect(n16):
        playerPos = 'n16'
        
    if player.colliderect(n17):
        playerPos = 'n17'
        
    if player.colliderect(n18):
        playerPos = 'n18'

    if player.colliderect(n19):
        playerPos = 'n19'

    if player.colliderect(n20):
        playerPos = 'n20'

    if player.colliderect(n21):
        playerPos = 'n21'

    if player.colliderect(n22):
        playerPos = 'n22'
        
    if player.colliderect(n23):
        playerPos = 'n23'
        
    if player.colliderect(n24):
        playerPos = 'n24'
        
    if player.colliderect(n25):
        playerPos = 'n25'
        
    if player.colliderect(n26):
        playerPos = 'n26'
        
    if player.colliderect(n27):
        playerPos = 'n27'
        
    if player.colliderect(n28):
        playerPos = 'n28'

    if player.colliderect(n29):
        playerPos = 'n29'

    if player.colliderect(n30):
        playerPos = 'n30'

    if player.colliderect(n31):
        playerPos = 'n31'

    if player.colliderect(n32):
        playerPos = 'n32'
        
    if player.colliderect(n33):
        playerPos = 'n33'
        
    if player.colliderect(n34):
        playerPos = 'n34'
        
    if player.colliderect(n35):
        playerPos = 'n35'
        
    if player.colliderect(n36):
        playerPos = 'n36'
        
    if player.colliderect(n37):
        playerPos = 'n37'
        
    if player.colliderect(n38):
        playerPos = 'n38'

    if player.colliderect(n39):
        playerPos = 'n39'

    if player.colliderect(n40):
        playerPos = 'n40'

    if player.colliderect(n41):
        playerPos = 'n41'

    if player.colliderect(n42):
        playerPos = 'n42'
        
    if player.colliderect(n43):
        playerPos = 'n43'
        
    if player.colliderect(n44):
        playerPos = 'n44'
        
    if player.colliderect(n45):
        playerPos = 'n45'
        
    if player.colliderect(n46):
        playerPos = 'n46'
        
    if player.colliderect(n47):
        playerPos = 'n47'
        
    if player.colliderect(n48):
        playerPos = 'n48'

    if player.colliderect(n49):
        playerPos = 'n49'

    if player.colliderect(n50):
        playerPos = 'n50'

    if player.colliderect(n51):
        playerPos = 'n51'

    if player.colliderect(n52):
        playerPos = 'n52'
        
    if player.colliderect(n53):
        playerPos = 'n53'
        
    if player.colliderect(n54):
        playerPos = 'n54'
        
    if player.colliderect(n55):
        playerPos = 'n55'
        
    if player.colliderect(n56):
        playerPos = 'n56'
        
    if player.colliderect(n57):
        playerPos = 'n57'
        
    if player.colliderect(n58):
        playerPos = 'n58'

    if player.colliderect(n59):
        playerPos = 'n59'

    if player.colliderect(n60):
        playerPos = 'n60'

    if player.colliderect(n61):
        playerPos = 'n61'

    if player.colliderect(n62):
        playerPos = 'n62'

    if player.colliderect(n63):
        playerPos = 'n63'

    if player.colliderect(n64):
        playerPos = 'n64'


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

    if gameOver == False:
        if key[pygame.K_LEFT]:
                x2 = -1.5
                y2 = 0
                value = 0
            
        if key[pygame.K_RIGHT]:
                x2 = 2
                y2 = 0
                value = 1
        
        if key[pygame.K_UP]:
                x2 = 0
                y2 = -1.5
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

        if ghost.colliderect(wall.rect):
            if x > 0:
                ghost.right = wall.rect.left
                path = []
                dijsktra(graph, playerPos, ghostPos, path)
            if x < 0:
                ghost.left = wall.rect.right
                path = []
                dijsktra(graph, playerPos, ghostPos, path)
            if y < 0:
                ghost.top = wall.rect.bottom
                path = []
                dijsktra(graph, playerPos, ghostPos, path)
            if y > 0:
                ghost.bottom = wall.rect.top
                path = []
                dijsktra(graph, playerPos, ghostPos, path)
                

    if player.x <= 0:
        player.x = 488

    if player.x >= 490:
        player.x = 2


    pygame.draw.rect(windowSurface, WHITE, n1)
    pygame.draw.rect(windowSurface, WHITE, n2)
    pygame.draw.rect(windowSurface, WHITE, n3)
    pygame.draw.rect(windowSurface, WHITE, n4)
    pygame.draw.rect(windowSurface, WHITE, n5)
    pygame.draw.rect(windowSurface, WHITE, n6)
    pygame.draw.rect(windowSurface, WHITE, n7)
    pygame.draw.rect(windowSurface, WHITE, n8)
    pygame.draw.rect(windowSurface, WHITE, n9)
    pygame.draw.rect(windowSurface, WHITE, n10)
    pygame.draw.rect(windowSurface, WHITE, n11)
    pygame.draw.rect(windowSurface, WHITE, n12)
    pygame.draw.rect(windowSurface, WHITE, n13)
    pygame.draw.rect(windowSurface, WHITE, n14)
    pygame.draw.rect(windowSurface, WHITE, n15)
    pygame.draw.rect(windowSurface, WHITE, n16)
    pygame.draw.rect(windowSurface, WHITE, n17)
    pygame.draw.rect(windowSurface, WHITE, n18)
    pygame.draw.rect(windowSurface, WHITE, n19)
    pygame.draw.rect(windowSurface, WHITE, n20)
    pygame.draw.rect(windowSurface, WHITE, n21)
    pygame.draw.rect(windowSurface, WHITE, n22)
    pygame.draw.rect(windowSurface, WHITE, n23)
    pygame.draw.rect(windowSurface, WHITE, n24)
    pygame.draw.rect(windowSurface, WHITE, n25)
    pygame.draw.rect(windowSurface, WHITE, n26)
    pygame.draw.rect(windowSurface, WHITE, n27)
    pygame.draw.rect(windowSurface, WHITE, n28)
    pygame.draw.rect(windowSurface, WHITE, n29)
    pygame.draw.rect(windowSurface, WHITE, n30)
    pygame.draw.rect(windowSurface, WHITE, n31)
    pygame.draw.rect(windowSurface, WHITE, n32)
    pygame.draw.rect(windowSurface, WHITE, n33)
    pygame.draw.rect(windowSurface, WHITE, n34)
    pygame.draw.rect(windowSurface, WHITE, n35)
    pygame.draw.rect(windowSurface, WHITE, n36)
    pygame.draw.rect(windowSurface, WHITE, n37)
    pygame.draw.rect(windowSurface, WHITE, n38)
    pygame.draw.rect(windowSurface, WHITE, n39)
    pygame.draw.rect(windowSurface, WHITE, n40)
    pygame.draw.rect(windowSurface, WHITE, n41)
    pygame.draw.rect(windowSurface, WHITE, n42)
    pygame.draw.rect(windowSurface, WHITE, n43)
    pygame.draw.rect(windowSurface, WHITE, n44)
    pygame.draw.rect(windowSurface, WHITE, n45)
    pygame.draw.rect(windowSurface, WHITE, n46)
    pygame.draw.rect(windowSurface, WHITE, n47)
    pygame.draw.rect(windowSurface, WHITE, n48)
    pygame.draw.rect(windowSurface, WHITE, n49)
    pygame.draw.rect(windowSurface, WHITE, n50)
    pygame.draw.rect(windowSurface, WHITE, n51)
    pygame.draw.rect(windowSurface, WHITE, n52)
    pygame.draw.rect(windowSurface, WHITE, n53)
    pygame.draw.rect(windowSurface, WHITE, n54)
    pygame.draw.rect(windowSurface, WHITE, n55)
    pygame.draw.rect(windowSurface, WHITE, n56)
    pygame.draw.rect(windowSurface, WHITE, n57)
    pygame.draw.rect(windowSurface, WHITE, n58)
    pygame.draw.rect(windowSurface, WHITE, n59)
    pygame.draw.rect(windowSurface, WHITE, n60)
    pygame.draw.rect(windowSurface, WHITE, n61)
    pygame.draw.rect(windowSurface, WHITE, n62)
    pygame.draw.rect(windowSurface, WHITE, n63)
    pygame.draw.rect(windowSurface, WHITE, n64)




        

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
    

    #build maze from list
    for wall in walls:
        pygame.draw.rect(windowSurface, (0, 0, 255), wall.rect)
    
    windowSurface.blit(image, player)
    windowSurface.blit(blinkyStretchedChase, ghost)
    #pygame.draw.rect(windowSurface, RED, ghost)

    #draw the text for the scoreboard using the drawText method
    drawText('Score: %s' % (score), font, windowSurface, 20, 520)

    #message displayed after eating all of the cookies
    if cookieCount >= 201:
        win = True
        gameOver = True


    if ghost.colliderect(player):
        win = False
        gameOver = True
        #pygame.time.wait(2000)
            
    if gameOver == True:
        x = 0
        y = 0
        x2 = 0
        y2 = 0
        if win == False:
            drawText('Game Over!', font, windowSurface, 300, 520)
        if win == True:
            drawText('You Win!', font, windowSurface, 300, 520)
    
    #pygame.draw.rect(windowSurface, YELLOW, player)

    pygame.display.update()
    mainClock.tick(40)
