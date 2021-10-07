#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      saver6522
#
# Created:     18/12/2017
# Copyright:   (c) saver6522 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from graphics import*
from button import*
import time
from random import randrange

def main():
    menuHelp()
    category = categorySelec()
    whatGame = levelSelec(category)
    isGameOver,mistakesMade,wordGuessed = game(whatGame)
    summary(isGameOver,mistakesMade,wordGuessed)

#window that opens when you win
def summary(isGameOver,mistakesMade,wordGuessed):
    try:
        if isGameOver == "gameover":
            won = GraphWin("Summary",400,600)
            won.setCoords(0.0, 0.0, 500, 500)
            won.setBackground('white')
            text = Text(Point(250,150),"Congratulations! You guessed")
            text.setSize(12)
            text.draw(won)
            text = Text(Point(250,125)," ".join(wordGuessed))
            text.setSize(11)
            text.draw(won)
            text = Text(Point(250,100),"with {0} mistakes".format(mistakesMade))
            text.setSize(12)
            text.draw(won)
            victoryAnimation(won)
            summaryButtons(won)
    except GraphicsError:
        print("Use a designated 'QUIT' button to close the window.")
        quit()
    except:
        quit()

#window that opens when you lose
def lost(word):
    try:
        lost = GraphWin("Summary",400,600)
        lost.setCoords(0.0, 0.0, 500, 500)
        lost.setBackground('white')
        text = Text(Point(250,150),"You lost! The word was:")
        text.setSize(12)
        text.draw(lost)
        text = Text(Point(250,125)," ".join(word))
        text.setSize(11)
        text.draw(lost)
        deathAnimation(lost)
        summaryButtons(lost)
    except GraphicsError:
        print("Use a designated 'QUIT' button to close the window.")
        quit()
    except:
        quit()

#animation for when you lose
def deathAnimation(lost):
#DRAWINGS
    stand = Image(Point(250,300), "lost_1.gif")
    fall = Image(Point(250,300), "lost_2.gif")
    drop = Image(Point(250,300), "lost_3.gif")
    hang = Image(Point(250,300), "lost_4.gif")
    deadStraight = Image(Point(250,300), "lost_5.gif")
    deadLeft = Image(Point(250,300), "lost_5_left.gif")
    deadRight = Image(Point(250,300), "lost_5_right.gif")
#ANIMATION
    stand.draw(lost)
    time.sleep(.25)
    stand.undraw()
    fall.draw(lost)
    time.sleep(.10)
    fall.undraw()
    drop.draw(lost)
    time.sleep(.10)
    drop.undraw()
    hang.draw(lost)
    time.sleep(.10)
    hang.undraw()
    deadStraight.draw(lost)
    time.sleep(.20)
    deadStraight.undraw()
    deadLeft.draw(lost)
    time.sleep(.20)
    deadLeft.undraw()
    deadStraight.draw(lost)
    time.sleep(.20)
    deadStraight.undraw()
    deadRight.draw(lost)
    time.sleep(.20)
    deadRight.undraw()
    deadStraight.draw(lost)
    time.sleep(.20)
    deadStraight.undraw()
    deadLeft.draw(lost)
    time.sleep(.20)
    deadLeft.undraw()
    deadStraight.draw(lost)
    time.sleep(.20)

#animation for when you win
def victoryAnimation(won):
#IMAGES
    stand = Image(Point(250,300), "won_1.gif")
    knife1 = Image(Point(250,300), "won_2.gif")
    knife2 = Image(Point(250,300), "won_3.gif")
    knife3 = Image(Point(250,300), "won_4.gif")
    knife4 = Image(Point(250,300), "won_5.gif")
    knife5 = Image(Point(250,300), "won_6.gif")
    knife6 = Image(Point(250,300), "won_7.gif")
    knife7 = Image(Point(250,300), "won_8.gif")
    knife8 = Image(Point(250,300), "won_9.gif")
    happy1 = Image(Point(250,300), "won_10.gif")
    happy2 = Image(Point(250,300), "won_11.gif")
    happy3 = Image(Point(250,300), "won_12.gif")
    happy4 = Image(Point(250,300), "won_13.gif")
#ANIMATIONS
    stand.draw(won)
    time.sleep(.25)
    stand.undraw()
    knife1.draw(won)
    time.sleep(.10)
    knife1.undraw()
    knife2.draw(won)
    time.sleep(.10)
    knife2.undraw()
    knife3.draw(won)
    time.sleep(.10)
    knife3.undraw()
    knife4.draw(won)
    time.sleep(.10)
    knife4.undraw()
    knife5.draw(won)
    time.sleep(.10)
    knife5.undraw()
    knife6.draw(won)
    time.sleep(.10)
    knife6.undraw()
    knife7.draw(won)
    time.sleep(.10)
    knife7.undraw()
    knife8.draw(won)
    time.sleep(.10)
    knife8.undraw()
    happy1.draw(won)
    time.sleep(.10)
    happy1.undraw()
    happy2.draw(won)
    time.sleep(.10)
    happy2.undraw()
    happy3.draw(won)
    time.sleep(.10)
    happy3.undraw()
    happy4.draw(won)
    time.sleep(.10)

#buttons to play again or quit after you lose or win
def summaryButtons(screen):
#PLAY AGAIN
    again = Button(screen,Point(100,75),150,20,"Play Again?")
    again.activate()
#QUIT
    summaryQuit = Button(screen,Point(400,75),150,20,"Quit")
    summaryQuit.activate()

#CHECK CLICKS
    while True:
        clicks = screen.getMouse()
        if summaryQuit.clicked(clicks):
                    screen.close()
                    quit()
        elif again.clicked(clicks):
            screen.close()
            main()

#When the game ends
def gameOver(rightAnswers,length,startGame,word):
    if " " in word:
        length = length - (word.count(" "))
    if rightAnswers == length:
       return "gameover"
#===============================================================================
#===============================================================================
#===============================================================================
#===============================================================================

#===============================================================================
#SPORTS GAMES

#creates a word list for sports - hard
def sportsGameHard():
    #sports_allFile
    fileName = "sports_all.txt"
    infile = open(fileName,"r")
    data = " "
    words = []
    while data != "":
        data = infile.readline()
        words.append(data)

    fileName1 = "sports_all_blank.txt"
    infile1 = open(fileName1,"r")
    dataBlank = " "
    wordsBlank = []
    infile = open(fileName,"r")
    data = " "
    while dataBlank != "":
        dataBlank = infile1.readline()
        wordsBlank.append(dataBlank)

        n = randrange(0,101)
    word = words[n].upper()
    wordBlank = wordsBlank[n].upper()
    #print(words[n])
    wordList = putWordsIntoList(word)
    blankWordList = putBlankWordsIntoList(wordBlank)
    length = len(wordList)
    mainWord = wordList[0:(length-1)]
    mainBlankWord = blankWordList[0:(length-1)]
    isGameOver,mistakesMade,wordGuessed = startSportsGameHard(mainWord,mainBlankWord)
    if isGameOver =="gameover":
        return "gameover",mistakesMade,wordGuessed

#creates a word list for sports - med
def sportsGameMed():
    #sports_all File
    fileName = "sports_all.txt"
    infile = open(fileName,"r")
    data = " "
    words = []
    while data != "":
        data = infile.readline()
        words.append(data)

    fileName1 = "sports_all_blank.txt"
    infile1 = open(fileName1,"r")
    dataBlank = " "
    wordsBlank = []
    infile = open(fileName,"r")
    data = " "
    while dataBlank != "":
        dataBlank = infile1.readline()
        wordsBlank.append(dataBlank)


    n = randrange(0,101)
    word = words[n].upper()
    wordBlank = wordsBlank[n].upper()
    #print(words[n])
    wordList = putWordsIntoList(word)
    blankWordList = putBlankWordsIntoList(wordBlank)
    length = len(wordList)
    mainWord = wordList[0:(length-1)]
    mainBlankWord = blankWordList[0:(length-1)]
    isGameOver,mistakesMade,wordGuessed = startSportsGameMedium(mainWord,mainBlankWord)
    if isGameOver =="gameover":
        return "gameover",mistakesMade,wordGuessed

#creates a word list for sports - easy
def sportsGameEasy():
    #sports_all File
    fileName = "sports_all.txt"
    infile = open(fileName,"r")
    data = " "
    words = []
    while data != "":
        data = infile.readline()
        words.append(data)

    fileName1 = "sports_all_blank.txt"
    infile1 = open(fileName1,"r")
    dataBlank = " "
    wordsBlank = []
    infile = open(fileName,"r")
    data = " "
    while dataBlank != "":
        dataBlank = infile1.readline()
        wordsBlank.append(dataBlank)


    n = randrange(0,101)
    word = words[n].upper()
    wordBlank = wordsBlank[n].upper()
    #print(words[n])
    wordList = putWordsIntoList(word)
    blankWordList = putBlankWordsIntoList(wordBlank)
    length = len(wordList)
    mainWord = wordList[0:(length-1)]
    mainBlankWord = blankWordList[0:(length-1)]
    isGameOver,mistakesMade,wordGuessed = startSportsGameEasy(mainWord,mainBlankWord)
    if isGameOver =="gameover":
        return "gameover",mistakesMade,wordGuessed

#open game window
def startSportsGameHard(word,wordBlank):
#Open the startGame window
    try:
        startGame = GraphWin("Sports - Hard",500,500)
        startGame.setCoords(0.0, 0.0, 1000, 1000)
        startGame.setBackground('white')

        wordText = Text(Point(500,650)," ".join(wordBlank))
        wordText.setSize(20)
        wordText.draw(startGame)

        mistakeLimit = 3

        isGameOver,mistakesMade,wordGuessed = drawAlphabet(startGame,word,wordBlank,wordText,mistakeLimit)
        if isGameOver =="gameover":
            return "gameover",mistakesMade,wordGuessed
    except GraphicsError:
        print("Use a designated 'QUIT' button to close the window.")
        quit()
    except:
        print("Unknown error occured")
        quit()

#open game window
def startSportsGameMedium(word,wordBlank):
#Open the startGame window
    try:
        startGame = GraphWin("Sports - Medium",500,500)
        startGame.setCoords(0.0, 0.0, 1000, 1000)
        startGame.setBackground('white')

        wordText = Text(Point(500,650)," ".join(wordBlank))
        wordText.setSize(20)
        wordText.draw(startGame)

        mistakeLimit = 4

        isGameOver,mistakesMade,wordGuessed = drawAlphabet(startGame,word,wordBlank,wordText,mistakeLimit)
        if isGameOver =="gameover":
            return "gameover",mistakesMade,wordGuessed

    except GraphicsError:
        print("Use a designated 'QUIT' button to close the window.")
        quit()
    except:
        quit()

#open game window
def startSportsGameEasy(word,wordBlank):
#Open the startGame window
    try:
        startGame = GraphWin("Sports - Easy",500,500)
        startGame.setCoords(0.0, 0.0, 1000, 1000)
        startGame.setBackground('white')

        wordText = Text(Point(500,650)," ".join(wordBlank))
        wordText.setSize(20)
        wordText.draw(startGame)

        mistakeLimit = 6

        isGameOver,mistakesMade,wordGuessed = drawAlphabet(startGame,word,wordBlank,wordText,mistakeLimit)
        if isGameOver =="gameover":
            return "gameover",mistakesMade,wordGuessed
    except GraphicsError:
        print("Use a designated 'QUIT' button to close the window.")
        quit()
    except:
        quit()
#===============================================================================
#===============================================================================
#===============================================================================
#===============================================================================

#===============================================================================
#COUNTRY GAMES

#creates a word list for countries - hard
def countriesGameHard():
    #countries_all File
    fileName = "countries_all.txt"
    infile = open(fileName,"r")
    data = " "
    words = []
    while data != "":
        data = infile.readline()
        words.append(data)

    fileName1 = "countries_all_blank.txt"
    infile1 = open(fileName1,"r")
    dataBlank = " "
    wordsBlank = []
    infile = open(fileName,"r")
    data = " "
    while dataBlank != "":
        dataBlank = infile1.readline()
        wordsBlank.append(dataBlank)

        n = randrange(0,104)
    word = words[n].upper()
    wordBlank = wordsBlank[n].upper()
    #print(words[n])
    wordList = putWordsIntoList(word)
    blankWordList = putBlankWordsIntoList(wordBlank)
    length = len(wordList)
    mainWord = wordList[0:(length-1)]
    mainBlankWord = blankWordList[0:(length-1)]
    isGameOver,mistakesMade,wordGuessed = startCountriesGameHard(mainWord,mainBlankWord)
    if isGameOver =="gameover":
        return "gameover",mistakesMade,wordGuessed

#creates a word list for countries - med
def countriesGameMed():
    #countries_all File
    fileName = "countries_all.txt"
    infile = open(fileName,"r")
    data = " "
    words = []
    while data != "":
        data = infile.readline()
        words.append(data)

    fileName1 = "countries_all_blank.txt"
    infile1 = open(fileName1,"r")
    dataBlank = " "
    wordsBlank = []
    infile = open(fileName,"r")
    data = " "
    while dataBlank != "":
        dataBlank = infile1.readline()
        wordsBlank.append(dataBlank)


    n = randrange(0,104)
    word = words[n].upper()
    wordBlank = wordsBlank[n].upper()
    #print(words[n])
    wordList = putWordsIntoList(word)
    blankWordList = putBlankWordsIntoList(wordBlank)
    length = len(wordList)
    mainWord = wordList[0:(length-1)]
    mainBlankWord = blankWordList[0:(length-1)]
    isGameOver,mistakesMade,wordGuessed = startCountriesGameMedium(mainWord,mainBlankWord)
    if isGameOver =="gameover":
        return "gameover",mistakesMade,wordGuessed

#creates a word list for countries - easy
def countriesGameEasy():
    #countries_all File
    fileName = "countries_all.txt"
    infile = open(fileName,"r")
    data = " "
    words = []
    while data != "":
        data = infile.readline()
        words.append(data)

    fileName1 = "countries_all_blank.txt"
    infile1 = open(fileName1,"r")
    dataBlank = " "
    wordsBlank = []
    infile = open(fileName,"r")
    data = " "
    while dataBlank != "":
        dataBlank = infile1.readline()
        wordsBlank.append(dataBlank)

    n = randrange(0,104)
    word = words[n].upper()
    wordBlank = wordsBlank[n].upper()
    #print(words[n])
    wordList = putWordsIntoList(word)
    blankWordList = putBlankWordsIntoList(wordBlank)
    length = len(wordList)
    mainWord = wordList[0:(length-1)]
    mainBlankWord = blankWordList[0:(length-1)]
    isGameOver,mistakesMade,wordGuessed = startCountriesGameEasy(mainWord,mainBlankWord)
    if isGameOver =="gameover":
        return "gameover",mistakesMade,wordGuessed

#open game window
def startCountriesGameHard(word,wordBlank):
#Open the startGame window
    try:
        startGame = GraphWin("Countries - Hard",500,500)
        startGame.setCoords(0.0, 0.0, 1000, 1000)
        startGame.setBackground('white')

        wordText = Text(Point(500,650)," ".join(wordBlank))
        wordText.setSize(20)
        wordText.draw(startGame)

        mistakeLimit = 3

        isGameOver,mistakesMade,wordGuessed = drawAlphabet(startGame,word,wordBlank,wordText,mistakeLimit)
        if isGameOver =="gameover":
            return "gameover",mistakesMade,wordGuessed

    except GraphicsError:
        print("Use a designated 'QUIT' button to close the window.")
        quit()
    except:
        quit()

#open game window
def startCountriesGameMedium(word,wordBlank):
#Open the startGame window
    try:
        startGame = GraphWin("Countries - Medium",500,500)
        startGame.setCoords(0.0, 0.0, 1000, 1000)
        startGame.setBackground('white')

        wordText = Text(Point(500,650)," ".join(wordBlank))
        wordText.setSize(20)
        wordText.draw(startGame)

        mistakeLimit = 4

        isGameOver,mistakesMade,wordGuessed = drawAlphabet(startGame,word,wordBlank,wordText,mistakeLimit)
        if isGameOver =="gameover":
            return "gameover",mistakesMade,wordGuessed
    except GraphicsError:
        print("Use a designated 'QUIT' button to close the window.")
        quit()
    except:
        quit()

#open game window
def startCountriesGameEasy(word,wordBlank):
#Open the startGame window
    try:
        startGame = GraphWin("Countries - Easy",500,500)
        startGame.setCoords(0.0, 0.0, 1000, 1000)
        startGame.setBackground('white')

        wordText = Text(Point(500,650)," ".join(wordBlank))
        wordText.setSize(20)
        wordText.draw(startGame)

        mistakeLimit = 6

        isGameOver,mistakesMade,wordGuessed = drawAlphabet(startGame,word,wordBlank,wordText,mistakeLimit)
        if isGameOver =="gameover":
            return "gameover",mistakesMade,wordGuessed
    except GraphicsError:
        print("Use a designated 'QUIT' button to close the window.")
        quit()
        quit()
#===============================================================================
#===============================================================================
#===============================================================================
#===============================================================================

#===============================================================================
#CAR GAMES

#creates a word list for cars - hard
def carsGameHard():
    #cars_hardFile
    fileName = "cars_hard.txt"
    infile = open(fileName,"r")
    data = " "
    words = []
    while data != "":
        data = infile.readline()
        words.append(data)

    fileName1 = "cars_hard_blank.txt"
    infile1 = open(fileName1,"r")
    dataBlank = " "
    wordsBlank = []
    infile = open(fileName,"r")
    data = " "
    while dataBlank != "":
        dataBlank = infile1.readline()
        wordsBlank.append(dataBlank)

        n = randrange(0,35)
    word = words[n].upper()
    wordBlank = wordsBlank[n].upper()
    #print(words[n])
    wordList = putWordsIntoList(word)
    blankWordList = putBlankWordsIntoList(wordBlank)
    length = len(wordList)
    mainWord = wordList[0:(length-1)]
    mainBlankWord = blankWordList[0:(length-1)]
    isGameOver,mistakesMade,wordGuessed = startCarsGameHard(mainWord,mainBlankWord)
    if isGameOver =="gameover":
        return "gameover",mistakesMade,wordGuessed

#creates a word list for cars - med
def carsGameMed():
    #cars_medium File
    fileName = "cars_medium.txt"
    infile = open(fileName,"r")
    data = " "
    words = []
    while data != "":
        data = infile.readline()
        words.append(data)

    fileName1 = "cars_medium_blank.txt"
    infile1 = open(fileName1,"r")
    dataBlank = " "
    wordsBlank = []
    infile = open(fileName,"r")
    data = " "
    while dataBlank != "":
        dataBlank = infile1.readline()
        wordsBlank.append(dataBlank)


    n = randrange(0,28)
    word = words[n].upper()
    wordBlank = wordsBlank[n].upper()
    #print(words[n])
    wordList = putWordsIntoList(word)
    blankWordList = putBlankWordsIntoList(wordBlank)
    length = len(wordList)
    mainWord = wordList[0:(length-1)]
    mainBlankWord = blankWordList[0:(length-1)]
    isGameOver,mistakesMade,wordGuessed = startCarsGameMedium(mainWord,mainBlankWord)
    if isGameOver =="gameover":
        return "gameover",mistakesMade,wordGuessed

#creates a word list for cars - easy
def carsGameEasy():
    #cars_easy File
    fileName = "cars_easy.txt"
    infile = open(fileName,"r")
    data = " "
    words = []
    while data != "":
        data = infile.readline()
        words.append(data)

    fileName1 = "cars_easy_blank.txt"
    infile1 = open(fileName1,"r")
    dataBlank = " "
    wordsBlank = []
    infile = open(fileName,"r")
    data = " "
    while dataBlank != "":
        dataBlank = infile1.readline()
        wordsBlank.append(dataBlank)


    n = randrange(0,37)
    word = words[n].upper()
    wordBlank = wordsBlank[n].upper()
    #print(words[n])
    wordList = putWordsIntoList(word)
    blankWordList = putBlankWordsIntoList(wordBlank)
    length = len(wordList)
    mainWord = wordList[0:(length-1)]
    mainBlankWord = blankWordList[0:(length-1)]
    isGameOver,mistakesMade,wordGuessed = startCarsGameEasy(mainWord,mainBlankWord)
    if isGameOver =="gameover":
        return "gameover",mistakesMade,wordGuessed

#open window for game
def startCarsGameHard(word,wordBlank):
    try:
        startGame = GraphWin("Cars - Hard",500,500)
        startGame.setCoords(0.0, 0.0, 1000, 1000)
        startGame.setBackground('white')

        wordText = Text(Point(500,650)," ".join(wordBlank))
        wordText.setSize(25)
        wordText.draw(startGame)

        mistakeLimit = 3

        isGameOver,mistakesMade,wordGuessed= drawAlphabet(startGame,word,wordBlank,wordText,mistakeLimit)
        if isGameOver =="gameover":
            return "gameover",mistakesMade,wordGuessed
    except GraphicsError:
        print("Use a designated 'QUIT' button to close the window.")
        quit()
    except:
        quit()

#open window for game
def startCarsGameMedium(word,wordBlank):
#Open the startGame window
    try:
        startGame = GraphWin("Cars - Medium",500,500)
        startGame.setCoords(0.0, 0.0, 1000, 1000)
        startGame.setBackground('white')

        wordText = Text(Point(500,650)," ".join(wordBlank))
        wordText.setSize(20)
        wordText.draw(startGame)

        mistakeLimit = 4

        isGameOver,mistakesMade,wordGuessed = drawAlphabet(startGame,word,wordBlank,wordText,mistakeLimit)
        if isGameOver =="gameover":
            return "gameover",mistakesMade,wordGuessed
    except GraphicsError:
        print("Use a designated 'QUIT' button to close the window.")
        quit()
    except:
        quit()

#open window for game
def startCarsGameEasy(word,wordBlank):
#Open the startGame window
    try:
        startGame = GraphWin("Cars - Easy",500,500)
        startGame.setCoords(0.0, 0.0, 1000, 1000)
        startGame.setBackground('white')

        wordText = Text(Point(500,650)," ".join(wordBlank))
        wordText.setSize(25)
        wordText.draw(startGame)

        mistakeLimit = 6

        isGameOver,mistakesMade,wordGuessed = drawAlphabet(startGame,word,wordBlank,wordText,mistakeLimit)
        if isGameOver =="gameover":
            return "gameover",mistakesMade,wordGuessed

    except GraphicsError:
        print("Use a designated 'QUIT' button to close the window.")
        quit()
    except:
        quit()

#===============================================================================
#===============================================================================
#===============================================================================
#===============================================================================

#===============================================================================
#VIDEO GAMES GAMES

#get word list for games - hard
def gamesGameHard():
    #games_all.txt
    fileName = "games_all.txt"
    infile = open(fileName,"r")
    data = " "
    words = []
    while data != "":
        data = infile.readline()
        words.append(data)

    fileName1 = "games_all_blank.txt"
    infile1 = open(fileName1,"r")
    dataBlank = " "
    wordsBlank = []
    infile = open(fileName,"r")
    data = " "
    while dataBlank != "":
        dataBlank = infile1.readline()
        wordsBlank.append(dataBlank)

        n = randrange(0,101)
    word = words[n].upper()
    wordBlank = wordsBlank[n].upper()
    #print(words[n])
    wordList = putWordsIntoList(word)
    blankWordList = putBlankWordsIntoList(wordBlank)
    length = len(wordList)
    mainWord = wordList[0:(length-1)]
    mainBlankWord = blankWordList[0:(length-1)]
    isGameOver,mistakesMade,wordGuessed = startGamesGameHard(mainWord,mainBlankWord)
    if isGameOver =="gameover":
        return "gameover",mistakesMade,wordGuessed

#gets word list for games - medium
def gamesGameMed():
    #cars_medium File
    fileName = "games_all.txt"
    infile = open(fileName,"r")
    data = " "
    words = []
    while data != "":
        data = infile.readline()
        words.append(data)

    fileName1 = "games_all_blank.txt"
    infile1 = open(fileName1,"r")
    dataBlank = " "
    wordsBlank = []
    infile = open(fileName,"r")
    data = " "
    while dataBlank != "":
        dataBlank = infile1.readline()
        wordsBlank.append(dataBlank)


    n = randrange(0,101)
    word = words[n].upper()
    wordBlank = wordsBlank[n].upper()
    #print(words[n])
    wordList = putWordsIntoList(word)
    blankWordList = putBlankWordsIntoList(wordBlank)
    length = len(wordList)
    mainWord = wordList[0:(length-1)]
    mainBlankWord = blankWordList[0:(length-1)]
    isGameOver,mistakesMade,wordGuessed = startGamesGameMedium(mainWord,mainBlankWord)
    if isGameOver =="gameover":
        return "gameover",mistakesMade,wordGuessed

#gets word list for games - easy
def gamesGameEasy():
    #cars_easy File
    fileName = "games_all.txt"
    infile = open(fileName,"r")
    data = " "
    words = []
    while data != "":
        data = infile.readline()
        words.append(data)

    fileName1 = "games_all_blank.txt"
    infile1 = open(fileName1,"r")
    dataBlank = " "
    wordsBlank = []
    infile = open(fileName,"r")
    data = " "
    while dataBlank != "":
        dataBlank = infile1.readline()
        wordsBlank.append(dataBlank)


    n = randrange(0,101)
    word = words[n].upper()
    wordBlank = wordsBlank[n].upper()
    #print(words[n])
    wordList = putWordsIntoList(word)
    blankWordList = putBlankWordsIntoList(wordBlank)
    length = len(wordList)
    mainWord = wordList[0:(length-1)]
    mainBlankWord = blankWordList[0:(length-1)]
    isGameOver,mistakesMade,wordGuessed = startGamesGameEasy(mainWord,mainBlankWord)
    if isGameOver =="gameover":
        return "gameover",mistakesMade,wordGuessed

#window for the hard - videogames category
def startGamesGameHard(word,wordBlank):
#Open the startGame window
    try:
        startGame = GraphWin("Games - Hard",500,500)
        startGame.setCoords(0.0, 0.0, 1000, 1000)
        startGame.setBackground('white')

        wordText = Text(Point(500,650)," ".join(wordBlank))
        wordText.setSize(25)
        wordText.draw(startGame)

        mistakeLimit = 3

        isGameOver,mistakesMade,wordGuessed= drawAlphabet(startGame,word,wordBlank,wordText,mistakeLimit)
        if isGameOver =="gameover":
            return "gameover",mistakesMade,wordGuessed
    except GraphicsError:
        print("Use a designated 'QUIT' button to close the window.")
        quit()
    except:
        quit()

#window for the medium - videogames category
def startGamesGameMedium(word,wordBlank):
#Open the startGame window
    try:
        startGame = GraphWin("Games - Medium",500,500)
        startGame.setCoords(0.0, 0.0, 1000, 1000)
        startGame.setBackground('white')

        wordText = Text(Point(500,650)," ".join(wordBlank))
        wordText.setSize(20)
        wordText.draw(startGame)

        mistakeLimit = 4

        isGameOver,mistakesMade,wordGuessed = drawAlphabet(startGame,word,wordBlank,wordText,mistakeLimit)
        if isGameOver =="gameover":
            return "gameover",mistakesMade,wordGuessed
    except GraphicsError:
        print("Use a designated 'QUIT' button to close the window.")
        quit()
    except:
        quit()

#window for the easy - videogames category
def startGamesGameEasy(word,wordBlank):
#Open the startGame window
    try:
        startGame = GraphWin("Games - Easy",500,500)
        startGame.setCoords(0.0, 0.0, 1000, 1000)
        startGame.setBackground('white')

        wordText = Text(Point(500,650)," ".join(wordBlank))
        wordText.setSize(25)
        wordText.draw(startGame)

        mistakeLimit = 6

        isGameOver,mistakesMade,wordGuessed = drawAlphabet(startGame,word,wordBlank,wordText,mistakeLimit)
        if isGameOver =="gameover":
            return "gameover",mistakesMade,wordGuessed

    except GraphicsError:
        print("Use a designated 'QUIT' button to close the window.")
        quit()
    except:
        quit()

#===============================================================================
#===============================================================================
#===============================================================================
#===============================================================================
#DIFFICULTIES FOR THE SPORTS CATEGORY
def sportsLevel():
    try:
        sportsLevels = GraphWin("How good are you with sports?",250,300)
        sportsLevels.setCoords(0.0, 0.0, 2.5, 3.0)
        sportsLevels.setBackground('white')

        sLevelText = Text(Point(1.25,2.5),"Choose your difficulty:")
        sLevelText.setSize(14)
        sLevelText.draw(sportsLevels)

        levelSelected = False

        #EASY LEVEL BUTTON
        sportsEasyButton = Rectangle(Point(.6,1.85),Point(1.9,2.15))
        sportsEasyButton.setFill("grey")
        sportsEasyButton.draw(sportsLevels)
        sportsEasyButtonText = Text(Point(1.25,2), "EASY")
        sportsEasyButtonText.draw(sportsLevels)
        #MEDIUM LEVEL BUTTON
        sportsMediumButton = Rectangle(Point(.6,1.35),Point(1.9,1.65))
        sportsMediumButton.setFill("grey")
        sportsMediumButton.draw(sportsLevels)
        sportsMediumButtonText = Text(Point(1.25,1.5), "MEDIUM")
        sportsMediumButtonText.draw(sportsLevels)
        #HARD LEVEL BUTTON
        sportsHardButton = Rectangle(Point(.6,.85),Point(1.9,1.15))
        sportsHardButton.setFill("grey")
        sportsHardButton.draw(sportsLevels)
        sportsHardButtonText = Text(Point(1.25,1), "HARD")
        sportsHardButtonText.draw(sportsLevels)
        #BACK BUTTON
        sportsLevelBackButton = Rectangle(Point(.6,.15),Point(1.9,.45))
        sportsLevelBackButton.setFill("grey")
        sportsLevelBackButton.draw(sportsLevels)
        sportsLevelBackButtonText= Text(Point(1.25,.3), "BACK")
        sportsLevelBackButtonText.draw(sportsLevels)

        while True:
            click = sportsLevels.getMouse()
            x = click.getX()
            y = click.getY()
            #print(x,y)
            #check EASY
            if x <= 1.9 and x >=.6 and y <2.15 and y>=1.85:
                sportsLevels.close()
                return "sports easy"
                break
            #check MEDIUM
            elif x <= 1.9 and x >=.6 and y <=1.65 and y>=1.35:
                sportsLevels.close()
                return "sports med"
                break
            #check HARD
            elif x <= 1.9 and x >=.6 and y <=1.15 and y>=.85:
                sportsLevels.close()
                return "sports hard"
                break
            #check BACK
            elif x <= 1.9 and x >=.6 and y <=.45 and y>=.15:
                sportsLevels.close()
                #quit()
                main()
        sportsLevels.close()

    except GraphicsError:
        print("Use a designated 'QUIT' button to close the window.")
        quit()
    except:
        quit()


#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#DIFFICULTIES FOR THE COUNTRY CATEGORY
def countryLevel():
    try:
        countryLevels = GraphWin("How good are you with countries?",250,300)
        countryLevels.setCoords(0.0, 0.0, 2.5, 3.0)
        countryLevels.setBackground('white')

        cLevelText = Text(Point(1.25,2.5),"Choose your difficulty:")
        cLevelText.setSize(14)
        cLevelText.draw(countryLevels)

        levelSelected = False

        #EASY LEVEL BUTTON
        countriesEasyButton = Rectangle(Point(.6,1.85),Point(1.9,2.15))
        countriesEasyButton.setFill("grey")
        countriesEasyButton.draw(countryLevels)
        countriesEasyButtonText = Text(Point(1.25,2), "EASY")
        countriesEasyButtonText.draw(countryLevels)
        #MEDIUM LEVEL BUTTON
        countriesMediumButton = Rectangle(Point(.6,1.35),Point(1.9,1.65))
        countriesMediumButton.setFill("grey")
        countriesMediumButton.draw(countryLevels)
        countriesMediumButtonText = Text(Point(1.25,1.5), "MEDIUM")
        countriesMediumButtonText.draw(countryLevels)
        #HARD LEVEL BUTTON
        countriesHardButton = Rectangle(Point(.6,.85),Point(1.9,1.15))
        countriesHardButton.setFill("grey")
        countriesHardButton.draw(countryLevels)
        countriesHardButtonText = Text(Point(1.25,1), "HARD")
        countriesHardButtonText.draw(countryLevels)
        #BACK BUTTON
        countriesLevelBackButton = Rectangle(Point(.6,.15),Point(1.9,.45))
        countriesLevelBackButton.setFill("grey")
        countriesLevelBackButton.draw(countryLevels)
        countriesLevelBackButtonText= Text(Point(1.25,.3), "BACK")
        countriesLevelBackButtonText.draw(countryLevels)

        while True:
            click = countryLevels.getMouse()
            x = click.getX()
            y = click.getY()
            #print(x,y)
            #check EASY
            if x <= 1.9 and x >=.6 and y <2.15 and y>=1.85:
                countryLevels.close()
                return "countries easy"
                break
            #check MEDIUM
            elif x <= 1.9 and x >=.6 and y <=1.65 and y>=1.35:
                countryLevels.close()
                return "countries med"
                break
            #check HARD
            elif x <= 1.9 and x >=.6 and y <=1.15 and y>=.85:
                countryLevels.close()
                return "countries hard"
                break
            #check BACK
            elif x <= 1.9 and x >=.6 and y <=.45 and y>=.15:
                countryLevels.close()
                #quit()
                main()
        countryLevels.close()

    except GraphicsError:
        print("Use a designated 'QUIT' button to close the window.")
        quit()
    except:
        quit()
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
#DIFFICULTIES FOR THE CAR CATEGORY
def carsLevel():
#DIFFICULTY SCREEN
    try:
        cLevels = GraphWin("How good are you with cars?",250,300)
        cLevels.setCoords(0.0, 0.0, 2.5, 3.0)
        cLevels.setBackground('white')

        levelText = Text(Point(1.25,2.5),"Choose your difficulty:")
        levelText.setSize(14)
        levelText.draw(cLevels)

        levelSelected = False

        #EASY LEVEL BUTTON
        carsEasyButton = Rectangle(Point(.6,1.85),Point(1.9,2.15))
        carsEasyButton.setFill("grey")
        carsEasyButton.draw(cLevels)
        carsEasyButtonText = Text(Point(1.25,2), "EASY")
        carsEasyButtonText.draw(cLevels)
        #MEDIUM LEVEL BUTTON
        carsMediumButton = Rectangle(Point(.6,1.35),Point(1.9,1.65))
        carsMediumButton.setFill("grey")
        carsMediumButton.draw(cLevels)
        carsMediumButtonText = Text(Point(1.25,1.5), "MEDIUM")
        carsMediumButtonText.draw(cLevels)
        #HARD LEVEL BUTTON
        carsHardButton = Rectangle(Point(.6,.85),Point(1.9,1.15))
        carsHardButton.setFill("grey")
        carsHardButton.draw(cLevels)
        carsHardButtonText = Text(Point(1.25,1), "HARD")
        carsHardButtonText.draw(cLevels)
        #BACK BUTTON
        carsLevelBackButton = Rectangle(Point(.6,.15),Point(1.9,.45))
        carsLevelBackButton.setFill("grey")
        carsLevelBackButton.draw(cLevels)
        carsLevelBackButtonText= Text(Point(1.25,.3), "BACK")
        carsLevelBackButtonText.draw(cLevels)

        while True:
            click = cLevels.getMouse()
            x = click.getX()
            y = click.getY()
            #print(x,y)
            #check EASY
            if x <= 1.9 and x >=.6 and y <2.15 and y>=1.85:
                cLevels.close()
                return "cars easy"
                break

            #check MEDIUM
            elif x <= 1.9 and x >=.6 and y <=1.65 and y>=1.35:
                cLevels.close()
                return "cars med"
                break

            #check HARD
            elif x <= 1.9 and x >=.6 and y <=1.15 and y>=.85:
                cLevels.close()
                return "cars hard"
                break

            #check BACK
            elif x <= 1.9 and x >=.6 and y <=.45 and y>=.15:
                cLevels.close()
                #quit()
                main()
        cLevels.close()

    except GraphicsError:
        print("Use a designated 'QUIT' button to close the window.")
        quit()
    except:
        quit()

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
#DIFFICULTIES FOR THE GAMES CATEGORY
def gamesLevel():
#DIFFICULTY SCREEN
    try:
        gLevels = GraphWin("How good are you with video games?",250,300)
        gLevels.setCoords(0.0, 0.0, 2.5, 3.0)
        gLevels.setBackground('white')

        levelText = Text(Point(1.25,2.5),"Choose your difficulty:")
        levelText.setSize(14)
        levelText.draw(gLevels)

        levelSelected = False

        #EASY LEVEL BUTTON
        gamesEasyButton = Rectangle(Point(.6,1.85),Point(1.9,2.15))
        gamesEasyButton.setFill("grey")
        gamesEasyButton.draw(gLevels)
        gamesEasyButtonText = Text(Point(1.25,2), "EASY")
        gamesEasyButtonText.draw(gLevels)
        #MEDIUM LEVEL BUTTON
        gamesMediumButton = Rectangle(Point(.6,1.35),Point(1.9,1.65))
        gamesMediumButton.setFill("grey")
        gamesMediumButton.draw(gLevels)
        gamesMediumButtonText = Text(Point(1.25,1.5), "MEDIUM")
        gamesMediumButtonText.draw(gLevels)
        #HARD LEVEL BUTTON
        gamesHardButton = Rectangle(Point(.6,.85),Point(1.9,1.15))
        gamesHardButton.setFill("grey")
        gamesHardButton.draw(gLevels)
        gamesHardButtonText = Text(Point(1.25,1), "HARD")
        gamesHardButtonText.draw(gLevels)
        #BACK BUTTON
        gamesLevelBackButton = Rectangle(Point(.6,.15),Point(1.9,.45))
        gamesLevelBackButton.setFill("grey")
        gamesLevelBackButton.draw(gLevels)
        gamesLevelBackButtonText= Text(Point(1.25,.3), "BACK")
        gamesLevelBackButtonText.draw(gLevels)

        while True:
            click = gLevels.getMouse()
            x = click.getX()
            y = click.getY()
            #print(x,y)
            #check EASY
            if x <= 1.9 and x >=.6 and y <2.15 and y>=1.85:
                gLevels.close()
                return "games easy"
                break

            #check MEDIUM
            elif x <= 1.9 and x >=.6 and y <=1.65 and y>=1.35:
                gLevels.close()
                return "games med"
                break

            #check HARD
            elif x <= 1.9 and x >=.6 and y <=1.15 and y>=.85:
                gLevels.close()
                return "games hard"
                break

            #check BACK
            elif x <= 1.9 and x >=.6 and y <=.45 and y>=.15:
                gLevels.close()
                #quit()
                main()
        gLevels.close()

    except GraphicsError:
        print("Use a designated 'QUIT' button to close the window.")
        quit()
    except:
        quit()
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------


#put words into a list
def putWordsIntoList(word): #take the chosen string from the file and put it into a list
    length = len(word)
    index = 0
    WORD = []
    while index < length:
        WORD.append(word[index])
        index = index + 1
    return WORD

#Put blank words into a list with same indexes as normal word list
def putBlankWordsIntoList(word): #take the chosen blank string from the file and put it into a list
    length = len(word)
    index = 0
    WORD = []
    while index < length:
        WORD.append(word[index])
        index = index + 1
    return WORD

#checks if letter is in the word and acts accordignly
def checkWord(startGame,word,wordBlank,wordText,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,one,two,three,four,five,six,seven,eight,nine,quitGame,mistakeLimit):
    length = len(word)
    guesses = 0
    mistakes = 0
    mistakesText = Text(Point(500,850),mistakes*("X"))
    mistakesText.setSize(30)
    mistakesText.setFill("red")
    mistakesText.draw(startGame)
    newBlankList = wordBlank
    index = 0
    rightAnswers = 0
    isGameOver,mistakesMade,wordGuessed = guess(startGame,word,wordBlank,wordText,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,one,two,three,four,five,six,seven,eight,nine,quitGame,mistakes,guesses,index,length,newBlankList,mistakesText,rightAnswers,mistakeLimit)
    if isGameOver == "gameover":
        return "gameover",mistakesMade,wordGuessed

def guess(startGame,word,wordBlank,wordText,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,one,two,three,four,five,six,seven,eight,nine,quitGame,mistakes,guesses,index,length,newBlankList,mistakesText,rightAnswers,mistakeLimit):
    try:
        while guesses < (length + mistakeLimit):
            letter = alphabetClicked(startGame,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,one,two,three,four,five,six,seven,eight,nine,quitGame)
            index = 0
            if letter == None:
                guess(startGame,word,wordBlank,wordText,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,one,two,three,four,five,six,seven,eight,nine,quitGame,mistakes,guesses,index,length,newBlankList,mistakesText,rightAnswers,mistakeLimit)
            while index < length:
                if letter in word[index]:
                    newBlankList = newBlankList[:index] + [letter] + newBlankList[index+1:]
                    wordText.setText(" ".join(newBlankList))
                    index = index + 1
                    rightAnswers = rightAnswers + 1
                    isGameOver = gameOver(rightAnswers,length,startGame,word)
                    if isGameOver == "gameover":
                        startGame.close()
                        return "gameover",mistakes,word
                else:
                    index = index + 1
            if letter not in word:
                mistakes = mistakes + 1
                mistakesText.setText(mistakes*(" X "))
                if mistakes >= mistakeLimit:
                    startGame.close()
                    lost(word)
            guesses = guesses + 1
    except TypeError:
        print("Unknown Error Occured")
        quit()
    except GraphicsError:
        print("Use a designated 'QUIT' button to close the window.")
        quit()
    except:
        quit()
#===============================================================================
#===============================================================================
#===============================================================================
#===============================================================================

#===============================================================================
#ALPHABET STUFF
def drawAlphabet(startGame,word,wordBlank,wordText,mistakeLimit):
#Buttons for the alphabet
    keyboardOutline = Rectangle(Point(90,410),Point(910,60))
    keyboardOutline.setFill('black')
    keyboardOutline.draw(startGame)

    quitGame = Button(startGame,Point(950,30),80,50,"QUIT")
    quitGame.activate()
    #
    A = Button(startGame,Point(140,360),80,80,"A")
    A.activate()
    #
    B = Button(startGame,Point(220,360),80,80,"B")
    B.activate()
    #
    C = Button(startGame,Point(300,360),80,80,"C")
    C.activate()
    #
    D = Button(startGame,Point(380,360),80,80,"D")
    D.activate()
    #
    E = Button(startGame,Point(460,360),80,80,"E")
    E.activate()
    #
    F = Button(startGame,Point(540,360),80,80,"F")
    F.activate()
    #
    G = Button(startGame,Point(620,360),80,80,"G")
    G.activate()
    #
    H = Button(startGame,Point(700,360),80,80,"H")
    H.activate()
    #
    I = Button(startGame,Point(780,360),80,80,"I")
    I.activate()
    #
    J = Button(startGame,Point(860,360),80,80,"J")
    J.activate()
    #
    K = Button(startGame,Point(180,280),80,80,"K")
    K.activate()
    #
    L = Button(startGame,Point(260,280),80,80,"L")
    L.activate()
    #
    M = Button(startGame,Point(340,280),80,80,"M")
    M.activate()
    #
    N = Button(startGame,Point(420,280),80,80,"N")
    N.activate()
    #
    O = Button(startGame,Point(500,280),80,80,"O")
    O.activate()
    #
    P = Button(startGame,Point(580,280),80,80,"P")
    P.activate()
    #
    Q = Button(startGame,Point(660,280),80,80,"Q")
    Q.activate()
    #
    R = Button(startGame,Point(740,280),80,80,"R")
    R.activate()
    #
    S = Button(startGame,Point(820,280),80,80,"S")
    S.activate()
    #
    T = Button(startGame,Point(260,200),80,80,"T")
    T.activate()
    #
    U = Button(startGame,Point(340,200),80,80,"U")
    U.activate()
    #
    V = Button(startGame,Point(420,200),80,80,"V")
    V.activate()
    #
    W = Button(startGame,Point(500,200),80,80,"W")
    W.activate()
    #
    X = Button(startGame,Point(580,200),80,80,"X")
    X.activate()
    #
    Y = Button(startGame,Point(660,200),80,80,"Y")
    Y.activate()
    #
    Z = Button(startGame,Point(740,200),80,80,"Z")
    Z.activate()
    #
    zero = Button(startGame,Point(140,110),80,80,"0")
    zero.activate()
    #
    one = Button(startGame,Point(220,110),80,80,"1")
    one.activate()
    #
    two = Button(startGame,Point(300,110),80,80,"2")
    two.activate()
    #
    three = Button(startGame,Point(380,110),80,80,"3")
    three.activate()
    #
    four = Button(startGame,Point(460,110),80,80,"4")
    four.activate()
    #
    five = Button(startGame,Point(540,110),80,80,"5")
    five.activate()
    #
    six = Button(startGame,Point(620,110),80,80,"6")
    six.activate()
    #
    seven = Button(startGame,Point(700,110),80,80,"7")
    seven.activate()
    #
    eight = Button(startGame,Point(780,110),80,80,"8")
    eight.activate()
    #
    nine = Button(startGame,Point(860,110),80,80,"9")
    nine.activate()
    #
    isGameOver,mistakesMade,wordGuessed = checkWord(startGame,word,wordBlank,wordText,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,one,two,three,four,five,six,seven,eight,nine,quitGame,mistakeLimit)
    if isGameOver =="gameover":
        return "gameover",mistakesMade,wordGuessed

def alphabetClicked(startGame,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,one,two,three,four,five,six,seven,eight,nine,quitGame):
#GetMouse for alphabet
    click = startGame.getMouse()
#Alphabet from A to Z
    if quitGame.clicked(click):
        startGame.close()
        quit()
        return "A"
    elif A.clicked(click):
        A.deactivate()
        return "A"
    elif B.clicked(click):
        B.deactivate()
        return "B"
    elif C.clicked(click):
        C.deactivate()
        return "C"
    elif D.clicked(click):
        D.deactivate()
        return "D"
    elif E.clicked(click):
        E.deactivate()
        return "E"
    elif F.clicked(click):
        F.deactivate()
        return "F"
    elif G.clicked(click):
        G.deactivate()
        return "G"
    elif H.clicked(click):
        H.deactivate()
        return "H"
    elif I.clicked(click):
        I.deactivate()
        return "I"
    elif J.clicked(click):
        J.deactivate()
        return "J"
    elif K.clicked(click):
        K.deactivate()
        return "K"
    elif L.clicked(click):
        return "L"
    elif M.clicked(click):
        M.deactivate()
        return "M"
    elif N.clicked(click):
        N.deactivate()
        return "N"
    elif O.clicked(click):
        O.deactivate()
        return "O"
    elif P.clicked(click):
        P.deactivate()
        return "P"
    elif Q.clicked(click):
        Q.deactivate()
        return "Q"
    elif R.clicked(click):
        R.deactivate()
        return "R"
    elif S.clicked(click):
        S.deactivate()
        return "S"
    elif T.clicked(click):
        T.deactivate()
        return "T"
    elif U.clicked(click):
        U.deactivate()
        return "U"
    elif V.clicked(click):
        V.deactivate()
        return "V"
    elif W.clicked(click):
        W.deactivate()
        return "W"
    elif X.clicked(click):
        X.deactivate()
        return "X"
    elif Y.clicked(click):
        Y.deactivate()
        return "Y"
    elif Z.clicked(click):
        Z.deactivate()
        return "Z"
    elif one.clicked(click):
        one.deactivate()
        return "1"
    elif two.clicked(click):
        two.deactivate()
        return "2"
    elif three.clicked(click):
        three.deactivate()
        return "3"
    elif four.clicked(click):
        four.deactivate()
        return "4"
    elif five.clicked(click):
        five.deactivate()
        return "5"
    elif six.clicked(click):
        six.deactivate()
        return "6"
    elif seven.clicked(click):
        seven.deactivate()
        return "7"
    elif eight.clicked(click):
        eight.deactivate()
        return "8"
    elif nine.clicked(click):
        nine.deactivate()
        return "9"
#===============================================================================
#===============================================================================
#===============================================================================
#===============================================================================

#===============================================================================
#CATEGORY SELECT // LEVEL SELECT // GAME START CODE
def game(whatGame):
#CAR LEVELS
    if whatGame == "cars easy":
        isGameOver,mistakes,word = carsGameEasy()
        if isGameOver == "gameover":
            return "gameover",mistakes,word
    elif whatGame == "cars med":
        isGameOver,mistakes,word = carsGameMed()
        if isGameOver == "gameover":
            return "gameover",mistakes,word
    elif whatGame == "cars hard":
        isGameOver,mistakes,word = carsGameHard()
        if isGameOver == "gameover":
            return "gameover",mistakes,word

#COUNTRIES LEVELS
    elif whatGame == "countries easy":
        isGameOver,mistakes,word = countriesGameEasy()
        if isGameOver == "gameover":
            return "gameover",mistakes,word
    elif whatGame == "countries med":
        isGameOver,mistakes,word = countriesGameMed()
        if isGameOver == "gameover":
            return "gameover",mistakes,word
    elif whatGame == "countries hard":
        isGameOver,mistakes,word = countriesGameHard()
        if isGameOver == "gameover":
            return "gameover",mistakes,word

#SPORTS LEVELS
    elif whatGame == "sports easy":
        isGameOver,mistakes,word = sportsGameEasy()
        if isGameOver == "gameover":
            return "gameover",mistakes,word
    elif whatGame == "sports med":
        isGameOver,mistakes,word = sportsGameMed()
        if isGameOver == "gameover":
            return "gameover",mistakes,word
    elif whatGame == "sports hard":
        isGameOver,mistakes,word = sportsGameHard()
        if isGameOver == "gameover":
            return "gameover",mistakes,word

#GAMES LEVELS
    elif whatGame == "games easy":
        isGameOver,mistakes,word = gamesGameEasy()
        if isGameOver == "gameover":
            return "gameover",mistakes,word
    elif whatGame == "games med":
        isGameOver,mistakes,word = gamesGameMed()
        if isGameOver == "gameover":
            return "gameover",mistakes,word
    elif whatGame == "games hard":
        isGameOver,mistakes,word = gamesGameHard()
        if isGameOver == "gameover":
            return "gameover",mistakes,word

#module that returns level to figure out which category to play
def levelSelec(category):
    if category == "cat1":
        level = carsLevel()
        return level
    elif category == "cat2":
        level = countryLevel()
        return level
    elif category == "cat3":
        level = sportsLevel()
        return level
    elif category == "cat4":
        level = gamesLevel()
        return level

#category buttons
def categorySelec():
    try:
        categories = GraphWin("CATEGORIES",200,350)
        categories.setCoords(0.0, 0.0, 2.0, 3.5)
        categories.setBackground('white')

        categoryText = Text(Point(1,3),"CATEGORIES")
        categoryText.setSize(14)
        categoryText.draw(categories)

        #HELP BUTTON
        categoryHelpButton = Rectangle(Point(1.7,3.45),Point(1.95,3.2))
        categoryHelpButton.setFill("grey")
        categoryHelpButton.draw(categories)
        categoryHelpButtonText = Text(Point(1.825,3.325), "?")
        categoryHelpButtonText.setSize(17)
        categoryHelpButtonText.draw(categories)

        #CATEGORY 1 BUTTON
        category1Button = Rectangle(Point(.25,2.35),Point(1.75,2.65))
        category1Button.setFill("grey")
        category1Button.draw(categories)
        category1ButtonText = Text(Point(1,2.5), "CARS")
        category1ButtonText.draw(categories)

        #CATEGORY 2 BUTTON
        category2Button = Rectangle(Point(.25,1.85),Point(1.75,2.15))
        category2Button.setFill("grey")
        category2Button.draw(categories)
        category2ButtonText = Text(Point(1,2), "COUNTRIES")
        category2ButtonText.draw(categories)

        #CATEGORY 3 BUTTON
        category3Button = Rectangle(Point(.25,1.35),Point(1.75,1.65))
        category3Button.setFill("grey")
        category3Button.draw(categories)
        category3ButtonText = Text(Point(1,1.5), "SPORTS")
        category3ButtonText.draw(categories)

        #CATEGORY 4 BUTTON
        category4Button = Rectangle(Point(.25,.85),Point(1.75,1.15))
        category4Button.setFill("grey")
        category4Button.draw(categories)
        category4ButtonText= Text(Point(1,1), "VIDEO GAMES")
        category4ButtonText.draw(categories)

        #CATEGORY QUIT BUTTON
        categoryQuitButton = Rectangle(Point(.25,.15),Point(1.75,.45))
        categoryQuitButton.setFill("grey")
        categoryQuitButton.draw(categories)
        categoryQuitButtonText= Text(Point(1,.3), "BACK")
        categoryQuitButtonText.draw(categories)

        while True:
            click = categories.getMouse()
            x = click.getX()
            y = click.getY()

            # check CAT1
            if x <= 1.75 and x >=.25 and y <=2.65 and y>=2.35:
                categories.close()
                return "cat1"
            #check CAT2
            elif x <= 1.75 and x >=.25 and y <=2.15 and y>=1.85:
                categories.close()
                return "cat2"
            #check CAT3
            elif x <= 1.75 and x >=.25 and y <=1.65 and y>=1.35:
                categories.close()
                return "cat3"
            # check CAT4
            elif x <= 1.75 and x >=.25 and y <=1.15 and y>=.85:
                categories.close()
                return "cat4"

            # check BACK
            elif x <= 1.75 and x >=.25 and y <=.45 and y>=.15:
                break

        categories.close()
        main()

    except GraphicsError:
        print("Use a designated 'QUIT' button to close the window.")
        quit()
    except:
        quit()
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

def gameHelp():
#GAME HELP SCREEN (press ? on category select)
    try:
        gameHelp = GraphWin("HELP",500,500)
        gameHelp.setCoords(0.0, 0.0, 5.0, 5.0)
        gameHelp.setBackground('white')

        helptext = Text(Point(2.5,4.75),"'CARS' tests your ability with car brands,")
        helptext.setSize(12)
        helptext.draw(gameHelp)
        helptext = Text(Point(2.5,4.5),"everything from your basic Acura, to the exotic Zhiguli.")
        helptext.setSize(12)
        helptext.draw(gameHelp)
        helptext = Text(Point(2.5,4),"'Countries' makes you guess the name of a country")
        helptext.setSize(12)
        helptext.draw(gameHelp)
        helptext = Text(Point(2.5,3.5),"'Sports' tests your ability to guess exotic sports")
        helptext.setSize(12)
        helptext.draw(gameHelp)
        helptext = Text(Point(2.5,3),"'Games' tests your ability to guess loads of fun games (TIP: use numbers!")
        helptext.setSize(12)
        helptext.draw(gameHelp)
        helptext = Text(Point(2.5,2.5),"After choosing a category, you will be asked to choose a difficulty.")
        helptext.setSize(12)
        helptext.draw(gameHelp)
        helptext = Text(Point(2.5,2.25),"Some categories will include different words for each difficulty.")
        helptext.setSize(12)
        helptext.draw(gameHelp)
        helptext = Text(Point(2.5,2),"The main difference is how many tries you get before you fail.")
        helptext.setSize(12)
        helptext.draw(gameHelp)
        helptext = Text(Point(2.5,1.75),"Easy = 6 tries")
        helptext.setSize(12)
        helptext.draw(gameHelp)
        helptext = Text(Point(2.5,1.5),"Medium = 4 tries")
        helptext.setSize(12)
        helptext.draw(gameHelp)
        helptext = Text(Point(2.5,1.25),"Hard = 3 tries")
        helptext.setSize(12)
        helptext.draw(gameHelp)
        helptext = Text(Point(2.5,1),"Mistakes are marked with red X's")
        help.setFill('red')
        helptext.setSize(12)
        helptext.draw(gameHelp)
        helptext = Text(Point(2.5,.5),"(CLICK ANYWHERE TO CLOSE)")
        helptext.setSize(10)
        helptext.draw(gameHelp)

        gameHelp.getMouse()
        gameHelp.close()

    except GraphicsError:
        print("Use a designated 'QUIT' button to close the window.")
        quit()
    except:
        quit()

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#MENU WITH ANIMATION
def menuHelp():
#OPEN GRAHPICS WINDOW
    try:
        menu = GraphWin("MENU",400,350)
        menu.setCoords(0.0, 0.0, 4.0, 3.5)
        title = Image(Point(2,2.5), "hangman_title.gif")
        menu.setBackground('white')

        author = Text(Point(3.2,0.1), "Made by: Roman Savelyev")
        author.setSize(9)
        author.draw(menu)
        title.draw(menu)

    #START BUTTON
        mainStartButton = Rectangle(Point(.65,1.45),Point(1.35,.95))
        mainStartButton.setFill("grey")
        mainStartButton.draw(menu)
        mainStartButtonText = Text(Point(1,1.2), "START")
        mainStartButtonText.draw(menu)
        clicked = False
    #QUIT BUTTON
        mainQuitButton = Rectangle(Point(2.65,1.45),Point(3.35,.95))
        mainQuitButton.setFill("grey")
        mainQuitButton.draw(menu)
        mainQuitButtonText = Text(Point(3,1.2), "QUIT")
        mainQuitButtonText.draw(menu)
        clicked = False
    #ANIMATION
        while clicked == False:
            title1 = Image(Point(1.9,2.12), "hangman_1.gif")
            title2 = Image(Point(1.98,2.15), "hangman_2.gif")
            title3 = Image(Point(2.07,2.13), "hangman_3.gif")
            title1.draw(menu)
            time.sleep(.25)
            title1.undraw()
            title2.draw(menu)
            time.sleep(.25)
            title2.undraw()
            title3.draw(menu)
            time.sleep(.25)
            title3.undraw()
            title2.draw(menu)
            time.sleep(.25)
            title2.undraw()


            click = menu.checkMouse()
            if click == None:
                click = Point(0,0)
            x = click.getX()
            y = click.getY()
            # check START
            if x <= 1.35 and x >=.65 and y <=1.45 and y>=.95:
                clicked = True
                menu.close()
            # check QUIT
            elif x <= 3.35 and x >=2.65 and y <=1.45 and y>=.95:
                clicked = True
                menu.close()
                quit()
    except GraphicsError:
        print("Use a designated 'QUIT' button to close the window.")
        quit()
    except:
        quit()

main()