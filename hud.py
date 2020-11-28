import pygame, menuButton




class hudButton(menuButton.MenuButton):
    def checkInteraction(self, mousePos, mouseClicks):
        if self.triggerLoop == "ToMenu":
            if self.rect.collidepoint(mousePos):
                self.curCol = self.selectCol
            else:
                self.curCol = self.backCol

            if self.rect.collidepoint(mousePos) and mouseClicks[0] == True:
                return self.triggerLoop
            else:
                return None
        else:
            return None




def createHUD(gameData, gs, screenSize):
    elements = []
    #dayCount = menuButton.MenuButton(gs, f"Day {gameData[0]}", (740, 35), screenSize, "dayCount")
    elements.append(hudButton(gs, f"Day {gameData[0]}", (740, 35), screenSize, "dayCount"))
    elements.append(hudButton(gs, f"Health: {gameData[2]}", (100, 550), screenSize, "healthBar"))

    return elements



def drawHUD(gs, scr, elements, gameData):
    for el in elements:
        if el.triggerLoop == "dayCount":
            el.text = f"Day {gameData[0]}"
        el.render()
        returnMess = el.checkInteraction(pygame.mouse.get_pos(), pygame.mouse.get_pressed())
        if not(returnMess == None):
            trigLoop = returnMess
            return trigLoop
        
    scr.blit(gs, (0,0))
    pygame.display.update()