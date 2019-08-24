#Here in the silicon forge, we have crafted the ultra-mediocre engine.

import pygame
import sys
from pygame.locals import *
class Engine:
    def __init__(self, windowWidth, windowHeight, title, desiredFPS):
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.title = title
        self.desiredFPS = desiredFPS

        pygame.init()
        self.displaySurf = pygame.display.set_mode((self.windowWidth, self.windowHeight))
        pygame.display.set_caption(title)
        self.FPSCLOCK = pygame.time.Clock()
        self.currentState = None


        self.randomGameData = {}

    def switchState(self, newstate):
        if self.currentState != None:
            self.currentState.close()
        self.currentState = newstate(self.displaySurf, self.randomGameData, self.switchState)


    def addData (self, data, dataTitle):
        self.randomGameData[dataTitle] = data
    def run(self):
        assert(self.currentState != None, "Make sure a state is active before calling run().")
        running = True
        while running:
            self.displaySurf.fill(pygame.color.Color("White"))

            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                else:
                    self.currentState.processEvent(event)

                    
            self.currentState.update()
            self.currentState.render()



            pygame.display.update()
            self.FPSCLOCK.tick(self.desiredFPS)

        self.end()
    def end(self):
        pygame.quit()
        #sys.exit()
