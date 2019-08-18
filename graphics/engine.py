#Here in the silicon forge, we have crafted the ultra-mediocre engine.

import pygame
from pygame.locals import *
class Engine():
    def __init__(self, windowWidth, windowHeight, title, desiredFPS):
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.title = title
        self.desiredFPS = desiredFPS

        pygame.init()
        self.displaySurf = pygame.display.set_mode((self.windowWidth, self.windowWidth), SCALED)
        pygame.display.set_caption(title)
        self.FPSCLOCK = pygame.time.Clock()

    def run(self):
        running = True
        while running:
            self.displaySurf.fill(pygame.color.Color("White"))

            for event in pygame.event.get():
                if event.type == EXIT:
                    running = False




            self.display.update()
            FPSCLOCK.tick(self.desiredFPS)

        self.end()
    def end(self):
        pygame.quit()
        sys.exit()
