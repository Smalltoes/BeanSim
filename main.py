from graphics import engine
from graphics import state
from simulation import world, organism

import random

import pygame


class SimState(state.State):
    def __init__(self, display, data, switchFunc):

        #ignore - this is for the graphics basically
        super().__init__(display,data,switchFunc)

        self.drawLoadingMessage()



        self.world = world.World(320, 180, 100, 255, 90)
        margin = 50
        self.boxSize = min((display.get_width()-margin * 2) //self.world.width, (display.get_height()-margin * 2) //self.world.height)
        self.startX = display.get_width() //2 -self.boxSize * self.world.width//2
        self.startY = display.get_height() // 2 - self.boxSize * self.world.height //2
        

        
        self.intializeEcosystem(20, 5)


    def render(self):
        iterX = 0
        iterY = 0
        color = pygame.color.Color("Black")
        for x in range(self.world.width):
            for y in range(self.world.height):
                rect = (self.startX + iterX * self.boxSize, self.startY + self.boxSize * iterY, self.boxSize, self.boxSize)
                #print(rect)
                if self.world.landscapeMap[x][y] == "S":
                    color = pygame.color.Color("aquamarine")
                elif self.world.landscapeMap[x][y] == "B":
                    color = pygame.color.Color("Yellow")
                elif self.world.landscapeMap[x][y] == "G":
                    color = pygame.color.Color("darkGreen")
                elif self.world.landscapeMap[x][y] == "H":
                    color = pygame.color.Color("darkgoldenrod")
                elif self.world.landscapeMap[x][y] == "M":
                    color = pygame.color.Color("Gray")
                elif self.world.landscapeMap[x][y] == "U":
                    color = pygame.color.Color("Beige")
                
                #print(rect)
                pygame.draw.rect(self.displaysurf, color, rect)
                iterY +=1

            iterY = 0
            iterX += 1
        for animal in self.animals:
            
            pygame.draw.circle(self.displaysurf, animal.color, (int(animal.x * self.boxSize + self.startX), int(animal.y * self.boxSize + self.startY)), int(animal.size))

    def intializeEcosystem(self, initialSmallBeanAmount, initialBeanEaterAmount):
        self.animals = []
        smallBean = organism.Species("smallBean", 5, 20, (0, 200, 100), [], True, 4)

        beanEater = organism.Species("beanEater", 10, 10, (255, 0, 0), ["smallBean"], False, 2)
        for x in range(initialSmallBeanAmount):
            animalX, animalY = self.findRandomUsableTile()
            self.animals.append(organism.Organism(animalX, animalY, smallBean))

        for x in range(initialBeanEaterAmount):
            animalX, animalY = self.findRandomUsableTile()
            self.animals.append(organism.Organism(animalX, animalY, beanEater))

    def findRandomUsableTile(self):
        x = random.randint(1, self.world.width-2)
        y = random.randint(1, self.world.height-2)
        while (self.world.landscapeMap[x][y] == "S"):
            x = random.randint(1, self.world.width-2)
            y = random.randint(1, self.world.height-2)
        return x,y

    def drawLoadingMessage(self):
        self.displaysurf.fill(pygame.color.Color("White"))
        basicFont = pygame.font.SysFont("Arial", 24)
        fontSurf = basicFont.render("Initializing...", True, (0,0,0), (255,255,255))
        self.displaysurf.blit(fontSurf, (self.displaysurf.get_width()//2 - fontSurf.get_width()//2, self.displaysurf.get_height()//2 - fontSurf.get_width()//2))
        pygame.display.update()




game = engine.Engine(1600, 900, "Hello, World!", 20)
game.switchState(SimState)
game.run()
