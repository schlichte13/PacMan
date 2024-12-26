
# Python code to
# demonstrate readlines()
 
newScore = 300
scoreString = str(newScore)
scoreList = []
topScores = []
highestScores = []
highscore = 0
removeScore = False

 
# writing to file
file1 = open('myfile.txt', 'a')
file1.write(scoreString + "\n")
file1.close()
 
# Using readlines()
file1 = open('myfile.txt', 'r')
Lines = file1.read().splitlines()

file1.close()

for i in range(len(Lines)):
    scoreList.append(int(Lines[i]))


lowestScore = 0
highscore = max(scoreList)

while len(highestScores) < 5:
    highestScores.append(max(scoreList))
    scoreList.remove(max(scoreList))
    



print(highscore)
print("All other scores: ")
print(scoreList)
print("Highscores: ")
print(highestScores)
