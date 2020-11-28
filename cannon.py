import pygame, projectile
class Cannon:
    def __init__(self, size, surf):
        # Setup
        self.pos = (size[0] / 2, size[1] * 0.85) # 0.85 is hardcoded value to position cannon towards bottom of screen
        self.h = 90 # heading, angle for calculations
        self.ds = surf
        self.cannonSize = 100 / 2 # Keeps record of rad of image in pixels for calculation
        self.screenSize = size
        # image and rotation handling
        self.cannonFilePath = "assets/cannonPlaceholder.png"
        self.baseFilePath = "assets/towerBase.png"
        self.baseImage = pygame.image.load(self.baseFilePath)
        self.origImage = pygame.image.load(self.cannonFilePath) # always rotate original to preserve image quality
        self.rect = self.origImage.get_rect(center = self.pos)
        self.disImage = self.firstUpdate()
        self.rotationSpeed = 3
        self.baseRect = self.baseImage.get_rect(center = self.pos)
        # Reload Handling
        self.startReload = 0
        self.reloading = False
        self.reloadDelay = 1 #2 upgradeable, set low now for testing
        self.endReload = 0
        # Projectile Handling
        self.projectiles = [] # Holds all currently shot projectiles
        self.roundsFired = 0 # int that holds total rounds shot

    def firstUpdate(self):
        disImage = pygame.transform.rotozoom(self.origImage, self.h, 1)
        return disImage

    def render(self):
        self.ds.blit(self.disImage, self.rect)
        self.ds.blit(self.baseImage, self.baseRect)

        for proj in self.projectiles:
            proj.render()
    
        
    def rotate(self, direction):
        if direction == "left" and (self.h + self.rotationSpeed < 180):
            self.h += self.rotationSpeed
        
        elif direction == "right" and (self.h - self.rotationSpeed > 0):
            self.h -= self.rotationSpeed
        if self.h > 360:
            self.h -= 360
        elif self.h < 0:
            self.h += 360
        self.disImage = pygame.transform.rotozoom(self.origImage, self.h, 1)
        self.rect = self.disImage.get_rect()
        self.rect.center = self.pos

    def shoot(self):
        newProj = projectile.Projectile(self.ds, self.h, self.cannonSize, self.pos)
        self.projectiles.append(newProj)
        self.roundsFired += 1

    def update(self, keys, frameTag):
        if keys[pygame.K_LEFT]:
            self.rotate("left")
        if keys[pygame.K_RIGHT]:
            self.rotate("right")
        if keys[pygame.K_SPACE] and self.reloading == False:
            self.shoot()
            self.reloading = True
            self.startReload = frameTag
            self.endReload = self.startReload + (self.reloadDelay * 60)
        
        if self.reloading == True:
            if frameTag == self.endReload:
                self.reloading = False
        
        
        for i, j in enumerate(self.projectiles):
            j.update()
            if j.pos[0] > self.screenSize[0] or j.pos[0] < 0:
                del self.projectiles[i]
            elif j.pos[1] > self.screenSize[1] or j.pos[1] < 0:
                del self.projectiles[i]
        