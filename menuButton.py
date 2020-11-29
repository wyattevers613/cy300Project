import pygame

class MenuButton:
    def __init__(self, Wsurf, text, pos, screenSize, triggerLoop): # a setup function will create a list of button for each menu, and cycle through them to update
        self.ds = Wsurf
        self.text = text
        self.pos = pos
        self.size = 30
        self.font = pygame.font.match_font("yugothicyugothicuisemiboldyugothicuibold")
        self.color = (255, 255, 255)
        self.selected = False
        self.triggerLoop = triggerLoop
        self.xOff = 20
        self.yOff = 10
        self.rect = None
        self.backCol = (255, 0, 0)
        self.selectCol = (0, 255, 0)
        self.curCol = self.backCol

    def render(self):
        #print("render")
        buttonFont = pygame.font.Font(self.font, self.size)
        buttonSurface = buttonFont.render(self.text, True, self.color)
        self.rect = buttonSurface.get_rect()
        self.rect.center = self.pos
        pygame.draw.rect(self.ds, self.curCol, self.rect.inflate(self.xOff, self.yOff))
        self.ds.blit(buttonSurface, self.rect)
        
        # not currently displaying in menuLoop, need to fix
        

    def checkInteraction(self, mousePos, mouseClicks):
        #print("check")
        if self.rect.collidepoint(mousePos):
            #print("collide")
            self.curCol = self.selectCol
        else:
            self.curCol = self.backCol

        if self.rect.collidepoint(mousePos) and mouseClicks[0] == True:
            print("trigger")
            return self.triggerLoop
        else:
            return None


    def update(self, mousePos, events):
        # This function will take in the mouse position and click status to determine if the button is currently selected (hovered over)
        pass