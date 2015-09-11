######### CSC 113
######### Project 2
######### Qi Feng Huang
######### Mastermind


import pygame

def getGSPosition(easy, guess_num):
    if easy:
        return (179+(64*guess_num),200)
    else:
        return (115+(64*guess_num),200)
        

# squares to show player's current guess

class GuessSquare(pygame.sprite.Sprite):
    def __init__(self, color, guessNum, easy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,50))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.guessNumber = guessNum
        position = getGSPosition(easy,guessNum)
        self.rect.x = position[0]
        self.rect.y = position[1]
    
    
    def update(self):
        pass	
                
    def removeFromGroup(self):
        self.kill()
            
    def getSpriteIndex(self):
        return self.guessNumber