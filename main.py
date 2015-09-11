######### CSC 113
######### Project 2
######### Qi Feng Huang
######### Mastermind

import pygame
from RandomColorSequence import RandomColorSequence
from GuessSquare import GuessSquare
from ButtonCircle import ButtonCircle
from ColorsUsed import ColorsUsed


# global variables
colorsUsed = ColorsUsed()      # colors used in game
mainLoop = True                # should take key inputs?
easy = True                    # is difficulty easy?
lives = 10                     # attempts left


'''CHANGING SCENES'''

# if win, stop excepting game input keys and go to win scene with new input keys
def winAction(screen):
    pos = (200,150)
    label = mainfont.render("You won in "+str(10-lives)+" turns.", True, (0,0,0))
    label1 = mainfont.render("<R> : Restart", True, (0,0,0))
    label2 = mainfont.render("<M> : Main Menu", True, (0,0,0))
    rect = pygame.Rect(pos[0],pos[1], 400, 300)
    pygame.draw.rect(screen,(0,51,102), rect)
    screen.blit(label, (pos[0] + 100, pos[1] + 100))
    screen.blit(label2, (pos[0] + 100, pos[1] + 130))
    screen.blit(label1, (pos[0] + 100, pos[1] + 160))
    global mainLoop
    mainLoop = True
    while mainLoop:
        for event in pygame.event.get():
            winScreenEventCheck(event)
        pygame.display.flip()

# checks which key was pressed
def winScreenEventCheck(event):
    global mainLoop
    if event.type == pygame.QUIT:
        mainLoop = False
        return
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_m:
            mainLoop = False
            mainMenu(screen)
            return
        # restart
        elif event.key == pygame.K_r:
            mainLoop = False
            game(screen)
            return

# out of lives, go to lose scene
def loseAction(screen):
    pos = (200,150)
    label = mainfont.render("You lost. Try again.", True, (0,0,0))
    label1 = mainfont.render("<R> : Restart", True, (0,0,0))
    label2 = mainfont.render("<M> : Main Menu", True, (0,0,0))
    rect = pygame.Rect(pos[0],pos[1], 400, 300)
    pygame.draw.rect(screen,(153,0,0), rect)
    screen.blit(label, (pos[0] + 100, pos[1] + 100))
    screen.blit(label2, (pos[0] + 100, pos[1] + 130))
    screen.blit(label1, (pos[0] + 100, pos[1] + 160))
    global mainLoop
    mainLoop = True
    while mainLoop:
        for event in pygame.event.get():
            loseScreenEventCheck(event)
        pygame.display.flip()

def loseScreenEventCheck(event):
    global mainLoop
    if event.type == pygame.QUIT:
        mainLoop = False
        return
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_m:
            mainLoop = False
            mainMenu(screen)
            return
        elif event.key == pygame.K_r:
            mainLoop = False
            game(screen)
            return          

difficulty = ["HARD","EASY"]   # game difficulties

# main menu, can select difficulty of game
def mainMenu(screen):
    global difficulty
    pos = (225,225)
    screen.fill(pygame.Color("black"))  # make background black
    
    # add Title and instructions
    label = mainfont.render("MASTERMIND: QH Edition", True, (255,255,255))
    label0 = mainfont.render("<P> : Play game", True, (0,0,255))
    label1 = mainfont.render("<C> : Change difficulty", True, (0,0,255))
    label2 = mainfont.render("Difficulty: " + str(difficulty[easy]), True, (255,0,0))
    screen.blit(label, (pos[0], pos[1]))
    screen.blit(label0, (pos[0], pos[1] + 40))
    screen.blit(label1, (pos[0], pos[1] + 80))
    screen.blit(label2, (pos[0], pos[1] + 120))
    
    global mainLoop
    mainLoop = True
    
    while mainLoop:
        for event in pygame.event.get():
            mainMenuEventCheck(event, pos)
        pygame.display.flip()

# checks what key was pressed
def mainMenuEventCheck(event, pos):
    global mainLoop
    global easy
    global difficulty
    if event.type == pygame.QUIT:
        mainLoop = False
        return
    if event.type == pygame.KEYDOWN:
        # p for play
        if event.key == pygame.K_p:
            mainLoop = False
            game(screen)
            return
        # change difficulty
        elif event.key == pygame.K_c:
            easy = not easy
            rect = pygame.Rect(pos[0],pos[1]+120, 175, 30)
            pygame.draw.rect(screen,(0,0,0),rect)
            newLabel = mainfont.render("Difficulty: " + str(difficulty[easy]), True, (255,0,0))
            screen.blit(newLabel, (pos[0] , pos[1]+120))

# the game scene
def game(screen):
    global easy
    screen.fill(pygame.Color("black")) # erases the entire screen surface
    guessGroup = pygame.sprite.Group()
    setupGameInstr(screen)      # game instructiosn
    createOptions(screen)       # key and color
    createBackgroundSquare(screen)  # background for guesses
    createAttemptedBackground()     # previous attempt background
    game = RandomColorSequence(easy)    # create sequence we need to guess
    game.printSolution()    # shows solution in terminal
    global lives
    lives = 10              # set lives to 10
    global mainLoop
    mainLoop = True
    while mainLoop:
        for event in pygame.event.get():
            gameEventCheck(event,game, guessGroup)
        if lives <=0:       # out of lives, game over
            mainLoop = False
            loseAction(screen)
            return
        createBackgroundSquare(screen)
        guessGroup.draw(screen)
        pygame.display.flip()

# checks keys pressed in game
def gameEventCheck(event, game, guessGroup):
    global mainLoop
    global easy
    global lives
    if event.type == pygame.QUIT:
        mainLoop = False
        return
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_m:
            mainLoop = False
            mainMenu(screen)
            return
        # if 1-6 key pressed, try adding to guess list; if added, draw guess square
        elif event.key == pygame.K_1:
            if game.pushGuess(1):
                guessGroup.add(GuessSquare(colorsUsed.getColor(1), game.getCurrentSpriteIndex(),easy))
        elif event.key == pygame.K_2:
            if game.pushGuess(2):
                guessGroup.add(GuessSquare(colorsUsed.getColor(2), game.getCurrentSpriteIndex(),easy))
        elif event.key == pygame.K_3:
            if game.pushGuess(3):
                guessGroup.add(GuessSquare(colorsUsed.getColor(3), game.getCurrentSpriteIndex(),easy))
        elif event.key == pygame.K_4:
            if game.pushGuess(4):
                guessGroup.add(GuessSquare(colorsUsed.getColor(4), game.getCurrentSpriteIndex(),easy))
        elif event.key == pygame.K_5:
            if game.pushGuess(5):
                guessGroup.add(GuessSquare(colorsUsed.getColor(5), game.getCurrentSpriteIndex(),easy))
        elif event.key == pygame.K_6:
            if game.pushGuess(6):
                guessGroup.add(GuessSquare(colorsUsed.getColor(6), game.getCurrentSpriteIndex(),easy))

        # undo previous guess
        elif event.key == pygame.K_d:
            if game.popGuess():
                for sprite in guessGroup:
                    if sprite.getSpriteIndex() == (game.getCurrentSpriteIndex()+1):
                        sprite.removeFromGroup()
        # clear guesses
        elif event.key == pygame.K_c:
            game.clearGuess()
            for sprite in guessGroup:
                sprite.removeFromGroup()
        # check if sequence is correct
        elif event.key == pygame.K_x:
            if game.isFull():
                check = game.checkGuess()
                createTracker(screen, game.guess, check)
                game.clearGuess()
                for sprite in guessGroup:
                    sprite.removeFromGroup()
                lives -= 1
                if check[0] == game.numOfSlots:
                    mainLoop = False
                    winAction(screen)
                    return

'''FUNCTIONS FOR SETTING UP SCREEN'''


# how to play
def setupGameInstr(screen):
    pos = (20,20)
    font = pygame.font.SysFont(None, 20)
    label = font.render("<D> : Delete one", True, (255,255,255))
    label0 = font.render("<C> : Clear all", True, (255,255,255))
    label1 = font.render("<X> : Check", True, (255,255,255))
    label2 = font.render("<M> : Main Menu", True, (255,255,255))
    label3 = font.render("C : Correct slot and color", True, (255,255,255))
    label4 = font.render("OOP : Correct color / wrong slot", True, (255,255,255))
    screen.blit(label, (pos[0], pos[1]))
    screen.blit(label0, (pos[0] , pos[1] + 20))
    screen.blit(label1, (pos[0] , pos[1] + 40))
    screen.blit(label2, (pos[0] , pos[1] + 60))
    screen.blit(label3, (pos[0] + 350, pos[1]))
    screen.blit(label4, (pos[0] + 350, pos[1]+20))

# creates circle that maps color to key
def createOptions(screen):
    buttonGroup = pygame.sprite.Group()
    # creates circle for each color
    for color in range(1,7):
        sprite = ButtonCircle(colorsUsed.getColor(color), color)
        buttonGroup.add(sprite)
    
    buttonGroup.draw(screen) # draws sprites
    # adds text
    for sprite in buttonGroup:
        label = mainfont.render("<"+str(sprite.color)+">", True, (0,0,0))
        screen.blit(label, (sprite.rect.x+17, sprite.rect.y+26))

# background for guess squares
def createBackgroundSquare(screen):
    pos = getBackgroundSquarePos()
    bgRect = pygame.Rect(pos[0],pos[1], 256, 64)
    global easy
    # if hard, draw bigger background
    if not easy:
        bgRect = pygame.Rect(pos[0],pos[1], 384, 64)
    pygame.draw.rect(screen, (255,255,255), bgRect)

def getBackgroundSquarePos():
    global easy
    # easy and hard background have different positions
    if easy:
        return (172,193)
    else:
        return (108,193)

# shows boxes for storing previous guesses
def createAttemptedBackground():
    for x in range(0,10):
        pos = getAttemptedSquarePosition(x)
        bgRect = pygame.Rect(pos[0],pos[1], 195, 50)
        pygame.draw.rect(screen, (192,192,192), bgRect)

def getAttemptedSquarePosition(num):
    return(600, 5 + (num*55))

# displays correct and out of place for previous cuesses
def createTracker(screen, guessList, check):
    global lives
    if lives > 0:
        font = pygame.font.SysFont(None, 12)
        fPos = getTrackerFPos(lives)
        for square in guessList:
            rect = pygame.Rect(fPos[0],fPos[1], 10, 10)
            fPos = (fPos[0]+13,fPos[1])
            pygame.draw.rect(screen,colorsUsed.getColor(square), rect)
        label = font.render("C: "+str(check[0]), True, (0,0,0))
        label1 = font.render("OOP: "+str(check[1]), True, (0,0,0))
        screen.blit(label, (fPos[0] + 20, fPos[1]))
        screen.blit(label1, (fPos[0] + 15, fPos[1] + 10))

def getTrackerFPos(attemptNum):
    return (615, 20 + (10-attemptNum)*55)




''' init and start the game'''

pygame.init()
screen = pygame.display.set_mode((800,600)) # screen size
mainfont = pygame.font.SysFont(None, 30)    # set font
mainMenu(screen) # go to main menu