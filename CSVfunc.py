def writeScore (score):
    score = str(score)
    f = open('score.txt', 'w')
    f.write(score) # appends score to end

def getHighScore():
    f = open('score.txt', 'r')
    highScore = eval(f.read())
    return highScore
def something(currScore):
    highScore = getHighScore()
    if currScore > highScore:
        writeScore(currScore)
        print('YAYYY NEW HIGHSCOREEE')
    else:
        print('TRY AGAIN')

def init() :
    try:
        print('Chose Survival Mode. Current High Score is ',getHighScore())
    except: # error because empty
        writeScore(0)
        
        

    
