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






