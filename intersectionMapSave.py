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

x = 0
y = 0

x2 = 0
y2 = 0


ghost = pygame.Rect(30, 30, 10, 10)
player = pygame.Rect(110, 90, 10, 10)


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

playerPos = 'F'
ghostPos = 'A'
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

next_spot = n8

while True:

    #check for events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
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
        

    #variable to hold specific key pressed
    key = pygame.key.get_pressed()

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

    windowSurface.fill(BLACK)

    #build maze from list
    for wall in walls:
        pygame.draw.rect(windowSurface, (0, 0, 255), wall.rect)
    

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

    pygame.draw.rect(windowSurface, RED, ghost)
    pygame.draw.rect(windowSurface, YELLOW, player)

    pygame.display.update()
    mainClock.tick(40)
