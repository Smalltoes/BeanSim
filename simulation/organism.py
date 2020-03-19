import random


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
        self.speed = random.normalvariate(mu=species.speed, sigma=0.1*species.speed)
        self.size = random.normalvariate(mu=species.size, sigma=0.1*species.size)
        self.color = ((clamp(0, 255, random.normalvariate(mu=species.color[0], sigma=10))),
                      (clamp(0, 255, random.normalvariate(mu=species.color[1], sigma=10))),
                      (clamp(0, 255, random.normalvariate(mu=species.color[2], sigma=10))))

        self.prey = species.prey
        self.herbivore = species.herbivore
        self.numOffspring = species.numOffspring
        self.gender = random.randint(0, 2)


def reproduce(org1, org2):
    offspring = []
    if org1.speciesName == org2.speciesName and org1.gender != org2.gender:
        # makes sure that species match and genders are opposite

        if org1.gender == 1:
            org1, org2 = org2, org1
        # ensures that organism1 has gender 0, which is female gender for now

        num_offspring = max(round(random.normalvariate(mu=org1.numOffspring, sigma=0.5*org1.numOffspring)), 0)
        # randomizes the number of offspring
        for i in range(num_offspring):
            child = Organism(org1.x, org1.y, org1.species)
            child.speed = random.normalvariate(mu=0.5 * (org1.speed + org2.speed), sigma=0.1 * org1.species.speed)
            child.size = random.normalvariate(mu=0.5 * (org1.size + org2.size), sigma=0.1 * org1.species.size)
            child.color = (clamp(0, 255, random.normalvariate(mu=0.5 * (org1.color[0] + org2.color[0]), sigma=10)),
                           clamp(0, 255, random.normalvariate(mu=0.5 * (org1.color[1] + org2.color[1]), sigma=10)),
                           clamp(0, 255, random.normalvariate(mu=0.5 * (org1.color[2] + org2.color[2]), sigma=10)))
            # sets up parameters for child to be weighted around the average of parent parameters
            offspring.append(child)

    return offspring


def clamp(lower, upper, value):
    return min(upper, max(lower, value))

