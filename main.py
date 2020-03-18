from graphics import engine
from graphics import state
from simulation import world, organism

import pygame


class SimState(state.State):
    def __init__(self, display, data, switchFunc):
        super().__init__(display,data,switchFunc)
        self.world = world.World(160, 90, 100, 255, 90)
        margin = 50
        self.boxSize = min((display.get_width()-margin * 2) //self.world.width, (display.get_height()-margin * 2) //self.world.height)
        self.startX = display.get_width() //2 -self.boxSize * self.world.width//2
        self.startY = display.get_height() // 2 - self.boxSize * self.world.height //2
        print (self.boxSize, self.startX, self.startY)
        
    def render(self):
        iterX = 0
        iterY = 0
        color = pygame.color.Color("Black")
        for x in range(self.world.width):
            for y in range(self.world.height):
                rect = (self.startX + iterX * self.boxSize, self.startY + self.boxSize * iterY, self.boxSize, self.boxSize)
                #print(rect)
                if self.world.landscapeMap[x][y] == "S":
                    color = pygame.color.Color("Blue")
                elif self.world.landscapeMap[x][y] == "B":
                    color = pygame.color.Color("Yellow")
                elif self.world.landscapeMap[x][y] == "G":
                    color = pygame.color.Color("Green")
                elif self.world.landscapeMap[x][y] == "H":
                    color = pygame.color.Color("Brown")
                elif self.world.landscapeMap[x][y] == "M":
                    color = pygame.color.Color("Gray")
                elif self.world.landscapeMap[x][y] == "U":
                    color = pygame.color.Color("Beige")
                
                #print(rect)
                pygame.draw.rect(self.displaysurf, color, rect)
                iterY +=1

            iterY = 0
            iterX += 1
        #print("rendered")


smallBean = organism.Species("smallBean", 5, 20, (0, 200, 100), [], True)

beanEater = organism.Species("beanEater", 10, 10, (255, 0, 0), ["smallBean"], False)


game = engine.Engine(1600, 900, "Hello, World!", 20)
game.switchState(SimState)
game.run()
