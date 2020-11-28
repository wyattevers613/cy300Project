import pygame
class Collision:
    def __init__(self, surf, pos, frameTag):
        self.active = True
        self.ds = surf
        self.pos = pos
        self.imageFilePaths = ["assets/collision1.png", "assets/collision2.png", "assets/collision3.png"]
        # Time stamp explosions
        self.startExplosion = frameTag
        self.explosionLength = 1  # in seconds, later add randomness with random or with varying projectile
        self.endExplosion = self.startExplosion + (self.explosionLength * 60)
        self.curFrame = 0 # incremented after frameLength
        # Load individual frames
        self.frames, self.frameLength = self.loadFrames()

    def loadFrames(self):
        # load frames, done by length of filepath list to future proof for more frames if needed
        frames = []
        # load all frames as images and store in list
        for i in self.imageFilePaths:
            frames.append(pygame.image.load(i))
        # determine how long each frame should be shown
        frameLength = (self.explosionLength * 60) // (len(frames))
        return frames, frameLength

    def render(self, frameTag):
        if self.active == True:
            #self.ds.blit(self.frames[self.curFrame ], self.pos)
            frameNum = 1
            if frameTag == self.startExplosion + self.frameLength and not frameNum == len(self.frames):
                self.ds.blit(self.frames[self.curFrame], self.pos)
                self.curFrame += 1
                self.startExplosion = frameTag
                frameNum += 1
            elif frameTag == self.endExplosion - 1:
                self.active = False
            elif self.active:
                self.ds.blit(self.frames[self.curFrame], self.pos)


