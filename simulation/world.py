#This file contains all sorts of map creating junk. 
#Ideally it works with as simple as creating a World Object and then using the arguments.
#considering that there are almost zero comments, other than half deleted code, this file is probably going to become black magic in a couple months.
#I know what your saying, fix the file then.
#My response is "I could... but nah. Seems boring"


import copy
import random
import queue
import statistics
import numpy as np
darkToLightCharacters = ".'`,^:\";~-_+<>i!lI?/\\|()1{}[]rcvunxzjftLCJUYXZO0Qoahkbdpqwm*WMB8&%$#@"
#in the landscape map, S means Sea

#B = means beach, next to water, and height lower than 75

#G = means grass, not next to sea, but height lower than 75
#H = hill, not grass or beach, height lower than 150
#M = mountain, not the others, height higher than 150
#U = under the sea level, but on land.


class World:

    def __init__(self, width, height, plateAmount, heightVariability, waterLevel):
        self.width = width
        self.height = height

        self.plateAmount= plateAmount
        self.heightVariability = heightVariability
        self.waterLevel = waterLevel
        self.tectonicMap = self.createEmptyMap(True)
        self.temperatureMap = self.createEmptyMap(False)
        self.heightMap = self.createEmptyMap(False)
        self.boundaryMap = self.createEmptyMap(True)
        self.landscapeMap = self.createEmptyTextMap()

        self.tectonicMap, self.seeds = self.voronoiMap(self.tectonicMap, self.plateAmount)
        self.getHeightFromTectonics()
        self.createBoundaryMap()
        #self.printMap(self.tectonicMap, 2)
        #print()
        #self.printMap(self.heightMap, 2)
        #self.printHigherLighter(self.heightMap, self.heightVariability)
        #for x in range(90):
            #self.randomWeatherHeight()
        for x in range(15):
            self.weatherBasedOnHeight()
        
        self.createLandscapeMapFromHeightMap()
        #self.printHigherLighter(self.heightMap, self.heightVariability)
        #self.heightMap = self.perlinSmoothMap(self.heightMap)
        print()
        #self.printHigherLighter(self.heightMap, self.heightVariability)

    def createEmptyMap(self, inttrue):
        if inttrue:
            newMap = np.zeros((self.width, self.height), dtype=np.int32)
        else:
            newMap = np.zeros((self.width, self.height))
        return newMap
    def createEmptyTextMap(self):
        newMap = []
        for x in range(self.width):
            newMap.append([])
            for y in range(self.height):
                newMap[x].append("")
        return newMap

    def getTilesAroundTile(self, x, y):
        otherTiles = []
        if x == 0:
            otherTiles.append((x+1, y))

        elif x == self.width- 1:
            otherTiles.append((x-1, y))
        else:
            otherTiles.append((x+1, y))
            otherTiles.append((x-1, y))

        if y == 0:
            otherTiles.append((x, y + 1))
        elif y == self.height - 1:
            otherTiles.append((x, y-1))
        else:
            otherTiles.append((x, y-1))
            otherTiles.append((x, y+1))

        return otherTiles

    def createLandscapeMapFromHeightMap(self):
        initialWaterTile = [0, 0]
        #self.landscapeMap[initialWaterTile[0]][initialWaterTile[1]] = "S"
        checked = set()
        frontier = queue.Queue()
        frontier.put(initialWaterTile)
        while frontier.empty() != True:
            
            tile = frontier.get()
            self.landscapeMap[tile[0]][tile[1]]="S"
            for otherTile in self.getTilesAroundTile(tile[0], tile[1]):
                #print(otherTile)
                if self.heightMap[otherTile[0],otherTile[1]] < self.waterLevel and otherTile not in checked:
                    frontier.put(otherTile)
                    checked.add(otherTile)
                elif self.heightMap[otherTile[0],otherTile[1]] < 100 and otherTile not in checked:
                    self.landscapeMap[otherTile[0]][otherTile[1]] = "B"

        for x in range(self.width):
            for y in range(self.height):
                if self.landscapeMap[x][y] != "S" and self.landscapeMap[x][y] != "B":
                    if self.heightMap[x][y] < self.waterLevel:
                        self.landscapeMap[x][y] = "U"
                    elif self.heightMap[x][y] < 130:
                        self.landscapeMap[x][y] = "G"
                    elif self.heightMap[x][y] < 175:
                        self.landscapeMap[x][y] = "H"
                    else:
                        self.landscapeMap[x][y] = "M"


    def getHeightFromTectonics(self):
        heights = [
            random.randint(int(
                self.heightVariability/10)+1,
                self.heightVariability//10 * 8) for x in range(self.plateAmount)]
        #print(len(self.tectonicMap))
        #print(len(self.tectonicMap[1]))
        for x in range(self.width):
            #print(self.tectonicMap[x][-1])
            heights[self.tectonicMap[x,0]-1] = 0
            heights[self.tectonicMap[x,-1]-1]= 0

        for y in range(self.height):
            heights[self.tectonicMap[0,y]-1] = 0
            heights[self.tectonicMap[-1,y]-1]= 0
        #print(self.heightMap)
        for x in range(self.width):
            for y in range(self.height):
                #print(self.tectonicMap[x,y])
                
                self.heightMap[x,y] = heights[self.tectonicMap[x,y]-1]

    def randomWeatherHeight(self):
        heightsChanged=[]
        for x in range(self.width):
            for y in range(self.height):
                if (random.random()+self.heightMap[x,y]/(self.heightVariability*1.2)) > 1.05 and self.heightMap[x,y] != 0:
                    heightsChanged.append(self.heightMap[x,y])
                    self.heightMap[x,y] -= 1

        #print(statistics.median(heightsChanged))

    def perlinSmoothMap(self, mapToChange):
        for x in range(self.width - 1):
            for y in range(self.height -1):
                mapToChange[x,y] = min(mapToChange[x,y], mapToChange[x,y+1])
        return mapToChange

    def weatherBasedOnHeight(self):
        for x in range(self.width-1):
            for y in range(self.height-1):
                xHeightDifference = self.heightMap[x,y] - self.heightMap[x+1,y]
                if abs(xHeightDifference) > 1:
                    #print("yas")
                    self.heightMap[x,y] -= xHeightDifference//2
                    self.heightMap[x+1,y] += xHeightDifference//2

                    #print(self.heightMap[x][y])
                yHeightDifference = self.heightMap[x,y] - self.heightMap[x,y+1]
                if abs(yHeightDifference) > 1:
                    #print("yas")
                    self.heightMap[x,y] -= yHeightDifference//2
                    self.heightMap[x,y+1] += yHeightDifference//2
    def createBoundaryMap(self):

        for x in range(self.width - 1):
            for y in range(self.height - 1):
                if self.tectonicMap[x,y] != self.tectonicMap[x+1,y] and self.heightMap[x,y] != 0 and self.heightMap[x+1,y] != 0:
                    self.boundaryMap[x,y] = 1
                    #self.boundaryMap[x+1][y] = 1
                if self.tectonicMap[x,y] != self.tectonicMap[x,y+1] and self.heightMap[x,y] != 0 and self.heightMap[x,y+1] != 0:
                    self.boundaryMap[x,y] = 1
                    #self.boundaryMap[x][y+1] = 1

    def voronoiMap(self, mapToChange, seedCount):
        seeds = []
        for i in range(seedCount):
            seeds.append((random.randint(0, self.width -1), random.randint(0, self.height -1 )))

        iterX = 1
        for seed in seeds:
            mapToChange[seed[0],seed[1]] = iterX
            iterX+=1

        zeros = 1
        while zeros > 0:
            newMap = np.copy(mapToChange)
            # self.printMap(mapToChange, 3)
            # print()
            zeros = 0
            for x in range(self.width):
                for y in range(self.height):
                    value = mapToChange[x,y]
                    if value == 0:
                        zeros += 1
                    else:
                        for tile in self.getTilesAroundTile(x, y):
                            #print(tile)
                            if mapToChange[tile[0],tile[1]] == 0:
                                newMap[tile[0],tile[1]] = value

                        #self.safeChangeCell(newMap, x-1, y, value)
                        #self.safeChangeCell(newMap, x+1, y, value)
                        #self.safeChangeCell(newMap, x, y-1, value)
                        #self.safeChangeCell(newMap, x, y+1, value)
            mapToChange = newMap
        # self.printMap(mapToChange, 3)
        # print()
        return mapToChange, seeds

    def safeChangeCell(self, cellMap, x, y, newValue):
        correctedX = max(min(x, self.width -1 ), 0)
        correctedY = max(min(y, self.height-1), 0)
        if cellMap[correctedX,correctedY] == 0: 
            cellMap[correctedX,correctedY] = newValue

    def printMap(self, printMap, cellSize):
        for y in range(self.height):
            printLaya = []
            for x in range(self.width):
                seedStringSize = len(str(printMap[x,y]))
                printLaya.append(str(printMap[x,y]) + ' ' * (cellSize - seedStringSize))
            print("".join(printLaya))

    def printHigherLighter(self, printMap, maxInMap):
        for y in range(self.height):
            printLaya = []
            for x in range(self.width):
                normalizedValue = int(printMap[x,y]/maxInMap * (len(darkToLightCharacters)-1))
                # print(normalizedValue)
                printLaya.append(darkToLightCharacters[normalizedValue]) 

            print("".join(printLaya))