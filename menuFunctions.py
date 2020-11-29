import pygame, menuButton

# take menu surface, screen, and current button configuration and push to screen
def drawMenu(mS, scr, btns, menuLoop):
    mS.fill((0, 0, 0))
    for b in btns:
        b.render()
        returnMess = b.checkInteraction(pygame.mouse.get_pos(), pygame.mouse.get_pressed())
        if not(returnMess == None):
            trigLoop = returnMess
            return trigLoop

    scr.blit(mS, (0,0))
    pygame.display.update()
    return menuLoop



# set up main menu with option to start new game, continue old game, or view leaderboard
def mainMenuSetup(size):
    menuSurf = pygame.Surface(size)
    buttons = []
    newGameButton = menuButton.MenuButton(menuSurf, "New Game", (150, 300), size, "newGame")
    buttons.append(newGameButton)

    loadGameButton = menuButton.MenuButton(menuSurf, "Load Game", (150, 400), size, "loadGame")
    buttons.append(loadGameButton)
    menuSetup = True

    ldrBrdButton = menuButton.MenuButton(menuSurf, "Leaderboard", (150, 500), size, "ldrBrd")
    buttons.append(ldrBrdButton)

    return menuSurf, buttons, menuSetup


def gameOverSetup(size, gameData):
    gameOverSurf = pygame.Surface(size)
    buttons = []
    elements = []


    exitButton = menuButton.MenuButton(gameOverSurf, "Exit", (size[0] / 2, 500), size, "exit")
    buttons.append(exitButton)

    """
    backMenuButton = menuButton.MenuButton(gameOverSurf, "Main Menu", (200, 500), size, "mainMenu")
    buttons.append(backMenuButton)
    """

    displayText = pygame.font.Font(pygame.font.match_font("yugothicyugothicuisemiboldyugothicuibold"), 25)
    displayTextSurface = displayText.render(f"You survived {gameData[0]} days and achieved a score of {gameData[1]}", True, (255, 255, 255))
    displayTextRect = displayTextSurface.get_rect()
    displayTextRect.center = (size[0] / 2, size[1] / 2)
    textPackage = (displayTextSurface, displayTextRect)
    elements.append(textPackage)


    headingText = pygame.font.Font(pygame.font.match_font("yugothicyugothicuisemiboldyugothicuibold"), 100)
    headingTextSurface = headingText.render(f"Game Over", True, (255, 255, 255))
    headingTextRect = headingTextSurface.get_rect()
    headingTextRect.center = (size[0] / 2, size[1] / 6)
    headingPackage = (headingTextSurface, headingTextRect)
    elements.append(headingPackage)

    

    return gameOverSurf, buttons, elements
    
     

def gameOverDraw(gOSurf, scr, buttons, elements):
    gOSurf.fill((0, 0, 0))
    for el in elements:
        # pygame.draw.rect(self.ds, self.curCol, self.rect.inflate(self.xOff, self.yOff))
        gOSurf.blit(el[0], el[1])
    for b in buttons:
        b.render()
        returnMess = b.checkInteraction(pygame.mouse.get_pos(), pygame.mouse.get_pressed())
        if not(returnMess == None):
            trigLoop = returnMess
            return trigLoop

    scr.blit(gOSurf, (0,0))
    pygame.display.update()

    

