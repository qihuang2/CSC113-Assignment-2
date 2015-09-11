######### Project 2
######### Qi Feng Huang
######### Mastermind

#Colors used in game

class ColorsUsed:
    def __init__(self):
        self.colorArray = [(204,153,255), (255,204,153), (102,178,255), (153,255,153), (255,153,153), (255,255,153),(255,255,255)]
        '''L -> R:  Purple, Tan, Blue, Green, Pink, Yellow, White'''
    
    def getColor(self, num):
       return self.colorArray[num-1] 