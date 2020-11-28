import pygame
import math
class Projectile:
    def __init__(self, surf, h, cannonSize, cannonPos):
        self.pos = self.getInitialPos(h, cannonSize, cannonPos) # math - determine start point from cannon dim. and h
        self.ds = surf
        self.h = h
        self.vel = 10 #upgradeable
        self.bulletFilePath = "assets/bulletPlaceholder.png"
        self.bulletImage = pygame.image.load(self.bulletFilePath)
        self.r = 12

    def render(self):
        self.ds.blit(self.bulletImage, self.pos)

    def getInitialPos(self, h, cannonSize, cannonPos):
        x = (cannonSize * math.cos(math.radians(h))) + cannonPos[0]
        y = (-1 * cannonSize * math.sin(math.radians(h))) + cannonPos[1]
        initialPos = [x, y]
        return initialPos

    def update(self):
        newX = self.vel * math.cos(math.radians(self.h)) + self.pos[0]
        newY = (-1* self.vel * math.sin(math.radians(self.h))) + self.pos[1]
        self.pos = [newX, newY]
        