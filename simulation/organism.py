import numpy as np


class Species:
    def __init__(self, name, speed, size, color, prey, herbivore, num_offspring):
        self.name = name
        self.speed = speed
        self.size = size
        self.color = color
        self.prey = prey
        self.herbivore = herbivore
        self.numOffspring = num_offspring


class Organism:
    def __init__(self, x, y, species):
        self.x = x
        self.y = y
        self.species = species
        self.speciesName = species.name
        self.speed = np.random.normal(loc=species.speed, scale=0.1*species.speed)
        self.size = np.random.normal(loc=species.size, scale=0.1*species.size)
        self.color = (np.random.normal(loc=species.color[0], scale=10),
                      np.random.normal(loc=species.color[1], scale=10),
                      np.random.normal(loc=species.color[2], scale=10))
        self.prey = species.prey
        self.herbivore = species.herbivore
        self.numOffspring = species.numOffspring
        self.gender = np.random.randint(0, 2)


def reproduce(org1, org2):
    offspring = []
    if org1.speciesName == org2.speciesName:
        # makes sure that species match

        if org1.gender == 1:
            org1, org2 = org2, org1
        # ensures that organism1 has gender 0, which is female gender for now

        num_offspring = max(round(np.random.normal(loc=org1.numOffspring, scale=0.5*org1.numoffspring)), 0)
        # randomizes the number of offspring

        for i in range(num_offspring):
            child = Organism(org1.x, org1.y, org1.speciesName)
            child.speed = np.random.normal(loc=0.5 * (org1.speed + org2.speed), scale=0.1 * org1.species.speed)
            child.size = np.random.normal(loc=0.5 * (org1.size + org2.size), scale=0.1 * org1.species.size)
            child.color = (np.random.normal(loc=0.5 * (org1.color[0] + org2.color[0]), scale=10),
                           np.random.normal(loc=0.5 * (org1.color[1] + org2.color[1]), scale=10),
                           np.random.normal(loc=0.5 * (org1.color[2] + org2.color[2]), scale=10))
            # sets up parameters for child to be weighted around the average of parent parameters

    return offspring




