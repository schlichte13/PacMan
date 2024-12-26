import pygame, sys, random, os
from pygame.locals import *
from collections import defaultdict

def saveFile(score):
    # Python code to
    # demonstrate readlines()
     
    #score = 400
    scoreString = str(score)
    scoreList = []
    nameList = []
    topScores = []
    scoreAndName = {}
    highestScores = {}
    highNameScore = {}
    highscore = 0
    removeScore = False

    print('Enter your name: ')
    name = input()

    #scoreAndName = name + " " + scoreString + "\n"

     
    # writing to file
    file1 = open('myfile.txt', 'a')
    file1.write(scoreString + "\n")
    file1.close()

    file2 = open('names', 'a')
    file2.write(name + "\n")
    file2.close()
     
    # Using readlines()
    file1 = open('myfile.txt', 'r')
    Lines = file1.read().splitlines()

    file1.close()

    file2 = open('names', 'r')
    nameLines = file2.read().splitlines()

    #for i in range(len(nameLines)):
        #nameList.append(str(nameLines[i]))
    
    #print(Lines)
    #print(nameLines)
    for i in range(len(Lines)) and range(len(nameLines)):
        scoreAndName.update({str(nameLines[i]): int(Lines[i])})

    #print(scoreAndName)

    while len(highestScores) < 5:
        lowestScore = 0
        #print(scoreAndName)
        #print(highestScores)
        highscore = max(scoreAndName.values())
        highname = max(scoreAndName, key = scoreAndName.get)
        highNameScore = {highname: highscore}
        #print(highNameScore)
        del scoreAndName[highname]
        #print(scoreAndName)
        #del scoreAndName[highscore]
        highestScores.update(highNameScore)

    #if score in highestScores:
        #print("Enter your name:")
        #playerName = input()
    print(highestScores)
    #if len(highestScores) < 5:
        #print(highNameScore)
        #getNextDict(scoreAndName)
        #highestScores.update(highNameScore)

        #highestScores.append(max(scoreList))
        #del scoreAndName[highNameScore]


    #playerName = ''
    #scoreNames = {}


    #print(highestScores)
    #if score in highestScores:
        #print("Enter your name:")
        #playerName = input() 
        #scoreNames.update({playerName: score})
    
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

    font = pygame.font.SysFont('Corbel', 35)
    def drawText2(text, font, surface, x, y):
        textobj = font.render(text, 1, blue)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)

    scoreX = 200
    scoreY = 100



    def drawScores(highestScores):
        scoreX = 100
        scoreY = 150
        for key in highestScores:
            namePrint = key
            scorePrint = str(highestScores[key])
            #print(scorePrint)
            #print(namePrint)
            drawText2(namePrint, font, screen, scoreX, scoreY)
            drawText2(scorePrint, font, screen, 300, scoreY)
                #print(highestScores)
            scoreY = scoreY + 50

        
    while True: 
      
        for ev in pygame.event.get(): 
          
            if ev.type == pygame.QUIT: 
                pygame.quit()

        screen.fill(black)

        drawText2("High Scores: ", font, screen, 100, 50)
        #print(highestScores)
        drawScores(highestScores)
    #for key in highestScores:
        #namePrint = '"'+key+'"'
        #scorePrint = '"'+str(highestScores[key])+'"'
        #print(scorePrint)
        #print(namePrint)
        #drawText2(namePrint, font, screen, scoreX, scoreY)
        #drawText2(scorePrint, font, screen, 250, scoreY)
            #print(highestScores)
        #scoreY = scoreY + 20
    #drawText2(str(highestScores[0]), font, screen, scoreX, 100)   
    #drawText2(str(highestScores[1]), font, screen, scoreX, 150)
    #drawText2(str(highestScores[2]), font, screen, scoreX, 200)
    #drawText2(str(highestScores[3]), font, screen, scoreX, 250)
    #drawText2(str(highestScores[4]), font, screen, scoreX, 300)
        
        pygame.display.update()


    #print(highestScores[keys])
    #print(highscore)
    #print("All other scores: ")
    #print(scoreList)
    #print("Highscores: ")
    #print(highestScores)


