import pygame, random, math
class Asteroid:
    def __init__(self, surf, screenSize):
        self.ds = surf
        self.screenSize = screenSize
        self.r = random.randint(40,80) # temp r, eventualy have variable assets with set Rs
        self.pos = self.generatePos()
        self.g = -7 # eventually random, link fall speed to r
        self.h = 270 # eventually asteroids fall at a slant, but only if they land in view
        self.filePaths = ["assets/asteroidPlaceholder1.png", "assets/asteroidPlaceholder2.png", "assets/asteroidPlaceholder3.png"]
        self.image = pygame.image.load(random.choice(self.filePaths))
        self.image = pygame.transform.scale(self.image, (self.r, self.r))
        # eventuall throw in random rotation speed

    def generatePos(self):
        x = random.randint(0 + self.r, self.screenSize[0] - self.r)
        y = random.randint(self.r - 200, 0 - self.r)
        pos = [x, y]
        return pos

    def newPos(self):
        x = int(self.pos[0] + (self.g * math.cos(math.radians(self.h))))
        y = int(self.pos[1] + (self.g * math.sin(math.radians(self.h))))
        self.pos = [x, y]

    def update(self):
        self.newPos()


    def render(self):
        self.ds.blit(self.image, self.pos)
    