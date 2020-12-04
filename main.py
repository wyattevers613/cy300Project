# import packages
import pygame, sys, cannon, asteroid, collision, math, menuButton, gameFileIO, menuFunctions, hud
from pygame.locals import *

# Global Variables
size = (800, 600)
clock = pygame.time.Clock() 
FPS = 60
frameTag = 0
diffScale = 5
dayLength = 20 # sets uniform day length seconds * fps 20default
dayFrames = dayLength * 60



# Set Up
pygame.init()
screen = pygame.display.set_mode(size)





# Set which loop is showing
menu = "menu"
game = "game"
shop = "shop"

activeLoop = menu    # starting on game loop until menu system operational

menuSetup = False
gameSetup = False
ldrBoardSetup = False


# Draw Game Function
def drawGame(frameTag):
    gameSurf.blit(background, (0,0))
    #gameSurf.fill((0, 0, 0))
    for i in asteroids:
        i.render()
    cann.render()
    for i in collisions:
        i.render(frameTag)
    for i in groundImpacts:
        i.render(frameTag)
    pygame.display.update()
    screen.blit(gameSurf, (0,0))


def collisionDetection():
    for pInd, projectile in enumerate(cann.projectiles):
        for aInd, asteroid in enumerate(asteroids):
            if projectile.rect.colliderect(asteroid.rect):
                newCol = collision.Collision(gameSurf, asteroid.pos, frameTag)
                collisions.append(newCol)
                del asteroids[aInd]
                del cann.projectiles[pInd]
                gameData[1] += 100
    for aInd, asteroid in enumerate(asteroids):
        if asteroid.pos[1] > size[1]:
            newGroundCol = collision.GroundImpact(gameSurf, asteroid.pos, frameTag)
            groundImpacts.append(newGroundCol)
            del asteroids[aInd]
            gameData[2] -= 1
                



# Main Game Loop
while True:
    # EVENT LOOP
    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()

    
    if activeLoop == menu:
        if menuSetup == False:
            menuSurf, buttons, menuSetup = menuFunctions.mainMenuSetup(size)
            mainMenu = "mainMenu"
            menuLoop = mainMenu
            menuBack = pygame.image.load("assets/menuBackground.png")
        else:
            if menuLoop == mainMenu:
                menuLoop = menuFunctions.drawMenu(menuSurf, screen, buttons, menuLoop, menuBack)
            elif menuLoop == "newGame":
                activeLoop = game
                day = 0
                score = 0
                health = 3
                gameData = [day, score, health]
                menuSetup = False
            elif menuLoop == "ldrBrd":
                if ldrBoardSetup == False:
                    menuSetup = False
                    ldrBoardSetup = True
                    ldrData = gameFileIO.leaderboardToList()
                    ldrSurf, ldrEl, heading = gameFileIO.setupLeaderboard(ldrData, size)
                else:
                    trigLoop = gameFileIO.drawLeaderboard(ldrSurf, screen, ldrEl, heading)
                    if trigLoop:
                        ldrBoardSetup = False
                        menuLoop = mainMenu
                
                
                
                
                


    if activeLoop == game:

        if gameSetup == False:
            gameData[0] += 1
            gameSurf = pygame.Surface(size)
            hudElements = hud.createHUD(gameData, gameSurf, size)
            

            # Create Objects and Object containers
            
            cann = cannon.Cannon(size, gameSurf)
            collisions = []
            groundImpacts = []      #    track seperately to allow seperate animations
            asteroids = []
            startDayFrame = frameTag

            # load assets
            background = pygame.image.load("assets/gameBackground.png")

            score = 0 # right now score is reset, will change when load game feature implemented
            oldScore = 0    
            gameSetup = True
            betweenDays = False

            try:
                astNum = dayLength // (dayLength - (gameData[0] * diffScale)) + 3
            except ZeroDivisionError:
                astNum = 5
            dropInterval = dayFrames // astNum

        hud.drawHUD(gameSurf, screen, hudElements, gameData)
        collisionDetection()

        # Day incrementor + Actions on Day change
        if (frameTag - startDayFrame) % dayFrames == 0 and not frameTag == startDayFrame:
            gameData[0] += 1
            betweenDays = True
            # Difficulty Incrementor
            try:
                astNum = dayLength // (dayLength - (gameData[0] * diffScale)) + 3
            except ZeroDivisionError:
                astNum += 2
            dropInterval = dayFrames // astNum
        
        if not betweenDays:
            if frameTag % dropInterval == 0:
                astero = asteroid.Asteroid(gameSurf, size)
                asteroids.append(astero)
        
        if betweenDays:
            # launch store menu
            startDayFrame = frameTag
            betweenDays = False

        cann.update(keys, frameTag)
        for i in asteroids:
            i.update()

        if gameData[2] < 1:
            activeLoop = "gameOver"
            gameSetup = False
            gameOverSetup = False
            gameFileIO.updateLeaderboard(gameData)
            

        drawGame(frameTag)

    if activeLoop == "gameOver":
        if gameOverSetup == False:
            gameOverSurf, buttons, elements = menuFunctions.gameOverSetup(size, gameData)
            gameOverSetup = True


        jumpToLoop = menuFunctions.gameOverDraw(gameOverSurf, screen, buttons, elements)

        if not jumpToLoop == "Pass":
            if jumpToLoop == "mainMenu":
                gameSetup = False
                gameData = (0, 0, 3)
                activeLoop = menu
                menuLoop = mainMenu
            elif jumpToLoop == "exit":
                pygame.quit()
                sys.exit()
        
    # Quick quit for testing
    if keys[pygame.K_q]:
        pygame.quit()
        sys.exit()
    
    

    

    
    clock.tick(FPS) # control frame rate
    frameTag += 1 # frameTag operates as a time-keeping feature
    
