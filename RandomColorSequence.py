######### CSC 113
######### Project 2
######### Qi Feng Huang
######### Mastermind

from random import randint
import pygame

class RandomColorSequence:
    
    def __init__(self, easy):
        # if easy, only 4 colors needed; if hard, 6 colors needed
        if easy:
            self.numOfSlots = 4
        else:
            self.numOfSlots = 6
        self.solution = [randint(1,6) for x in range(self.numOfSlots)]    # generate random array as solution
        self.guess = [0 for x in range(self.numOfSlots)]                  # generate list of 0's to hold guesses
        self.slotsTaken = 0 
        
    def isFull(self):
        return self.slotsTaken == self.numOfSlots
    
    def isEmpty(self):
        return self.slotsTaken == 0
    
    def pushGuess(self,num):
        if not self.isFull():
            self.guess[self.slotsTaken] = num
            self.slotsTaken+=1
            return True
            
    def popGuess(self):
        if not self.isEmpty():
            self.slotsTaken-=1
            self.guess[self.slotsTaken] = 0
            return True
    
    # clear current guess array
    def clearGuess(self):
        if not self.isEmpty():
            for x in self.guess:
                x = 0
            self.slotsTaken = 0
    
    # returns most resent guess input's sprite
    def getCurrentSpriteIndex(self):
        return self.slotsTaken - 1
    
    
    # returns (num. of correct place and color, num. of corret color but out of place)
    def checkGuess(self):
        tGuess = list(self.guess)            # get temp version of player's guess
        tSolution = list(self.solution)      # get temp version of game's solution 
        outOfPlace = 0
        correct = 0
        count = 0
        while (count < self.numOfSlots):
            # if corrent color and place, change the temps to 0s so they won't be reconsidered later
            if tGuess[count] == tSolution [count]:
                tGuess[count] = 0
                tSolution[count] = 0
                correct += 1
            count+=1
        # check how many out of place but correct color
        for x in range(0,self.numOfSlots):
            if tGuess[x] != 0:
                for y in range(0,self.numOfSlots):
                    # set colors that match to 0 so they aren't reconsidered
                    if tGuess[x] == tSolution[y]:
                        tGuess[x] = 0
                        tSolution[y] = 0
                        outOfPlace += 1
                        break
        return (correct, outOfPlace)
    
    #debugging purposes
    def printSolution(self):
        print ("Solution: ",self.solution)
