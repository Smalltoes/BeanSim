import pygame


class Species:
    def __init__(self, name, speed, size, color, prey, herbivore):
        self.name = name
        self.speed = speed
        self.size = size
        self.color = color
        self.prey = prey
        self.herbivore = herbivore


class Organism:
    def __init__(self, x, y, species):
        self.x = x
        self.y = y
        self.species = species
        self.speed = species.speed
        self.speciesName = species.name
        self.color = species.color
        self.prey = species.prey
        self.herbivore = species.herbivore



