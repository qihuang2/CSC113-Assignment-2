######### CSC 113
######### Project 2
######### Qi Feng Huang
######### Mastermind

import pygame

def getBCPosition(index):
    return (40+(90*(index-1)),450)

# maps key to colored circle

class ButtonCircle(pygame.sprite.Sprite):	
    def __init__(self, color, index): 
        pygame.sprite.Sprite.__init__(self)
        self.color = index
        self.image = pygame.Surface([70,70])
        self.image.fill((0,0,0))
        pygame.draw.circle(self.image, color, (35, 35), 35, 0)
        self.rect = self.image.get_rect()
        position = getBCPosition(index)
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.image.set_alpha(200)
        
    def update(self):
        pass
        