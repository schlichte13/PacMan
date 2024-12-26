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
player = pygame.Rect(250, 250, 10, 10)
A = pygame.Rect(30, 30, 10, 10) 
B = pygame.Rect(250, 30, 10, 10)
C = pygame.Rect(250, 100, 10, 10)
D = pygame.Rect(140, 100, 10, 10) 
E = pygame.Rect(140, 250, 10, 10)
F = pygame.Rect(250, 250, 10, 10)
G = pygame.Rect(30, 250, 10, 10)
H = pygame.Rect(30, 180, 10, 10)


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
    ('A', 'B', 220),
    #e8
    ('A', 'H', 150),
    #e2
    ('B', 'C', 70),
    #e3
    ('C', 'D', 110),
    #e4
    ('D', 'E', 150),
    #e5
    ('E', 'F', 110),
    #e6
    ('E', 'G', 110),
    #e7
    ('G', 'H', 70),
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

next_spot = A

while True:

    #check for events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    for i in range(len(path)):
        if i >= 1:
            if path[1] == 'A':
                next_spot = A
            if path[1] == 'B':
                next_spot = B
            if path[1] == 'C':
                next_spot = C
            if path[1] == 'D':
                next_spot = D
            if path[1] == 'H':
                next_spot = H
            if path[1] == 'G':
                next_spot = G
            if path[1] == 'E':
                next_spot = E
            if path[1] == 'F':
                next_spot = F
        
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
    

    if ghost.contains(A):
        path = []
        ghostPos = 'A'
        dijsktra(graph, playerPos, ghostPos, path)

    if ghost.contains(B):
        path = []
        ghostPos = 'B'
        dijsktra(graph, playerPos, ghostPos, path)
        
    if ghost.contains(C):
        path = []
        ghostPos = 'C'
        dijsktra(graph, playerPos, ghostPos, path)
        
    if ghost.contains(D):
        path = []
        ghostPos = 'D'
        dijsktra(graph, playerPos, ghostPos, path)

    if ghost.contains(E):
        path = []
        ghostPos = 'E'
        dijsktra(graph, playerPos, ghostPos, path)
        
    if ghost.contains(F):
        path = []
        ghostPos = 'F'
        dijsktra(graph, playerPos, ghostPos, path)
        
    if ghost.contains(G):
        path = []
        ghostPos = 'G'
        dijsktra(graph, playerPos, ghostPos, path)
        
    if ghost.contains(H):
        path = []
        ghostPos = 'H'
        dijsktra(graph, playerPos, ghostPos, path)


    if player.colliderect(A):
        playerPos = 'A'
        #dijsktra(graph, playerPos, ghostPos, path)
    if player.colliderect(B):
        playerPos = 'B'
        #dijsktra(graph, playerPos, ghostPos, path)
    if player.colliderect(C):
        playerPos = 'C'
        #dijsktra(graph, playerPos, ghostPos, path)
    if player.colliderect(D):
        playerPos = 'D'
        #dijsktra(graph, playerPos, ghostPos, path)
    if player.colliderect(E):
        playerPos = 'E'
        #dijsktra(graph, playerPos, ghostPos, path)
    if player.colliderect(F):
        playerPos = 'F'
        #dijsktra(graph, playerPos, ghostPos, path)
    if player.colliderect(G):
        playerPos = 'G'
        #dijsktra(graph, playerPos, ghostPos, path)
    if player.colliderect(H):
        playerPos = 'H'
        #dijsktra(graph, playerPos, ghostPos, path)

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
    
    pygame.draw.rect(windowSurface, WHITE, A)
    pygame.draw.rect(windowSurface, WHITE, B)
    pygame.draw.rect(windowSurface, WHITE, C)
    pygame.draw.rect(windowSurface, WHITE, D)
    pygame.draw.rect(windowSurface, WHITE, E)
    pygame.draw.rect(windowSurface, WHITE, F)
    pygame.draw.rect(windowSurface, WHITE, G)
    pygame.draw.rect(windowSurface, WHITE, H)
    pygame.draw.rect(windowSurface, RED, ghost)
    pygame.draw.rect(windowSurface, YELLOW, player)

    pygame.display.update()
    mainClock.tick(40)
