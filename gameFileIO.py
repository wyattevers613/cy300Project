import pygame, menuButton
from datetime import datetime

def updateLeaderboard(ldrData): # ldrData will be package of all data to display on leaderboard, score, dayNum, etc.
    with open("leaderboard.txt", "a") as leaderboard:
        date = datetime.today()
        print(f"{ldrData[0]},{ldrData[1]},{date}",file=leaderboard)


def leaderboardToList():
    with open("leaderboard.txt", "r") as readFile:
        leaderboardDataList = []
        for line in readFile:
            if len(line) < 1: #Easy way to ignore last line
                continue
            day, score, enterDate = line.strip().split(",")
            enterDate = datetime.strptime(enterDate, '%Y-%m-%d %H:%M:%S.%f')
            # for help with strptime I used https://stackabuse.com/converting-strings-to-datetime-in-python/
            dataTup = score, day, enterDate
            leaderboardDataList.append(dataTup)
    return leaderboardDataList

def setupLeaderboard(leaderboardDataList, size):
    ds = pygame.Surface(size)
    elements = []

    limitDisplay = 10
    elCreated = 0

    yStart = 200

    leaderboardDataList = sorted(leaderboardDataList, reverse=True)

    backButton = menuButton.MenuButton(ds, "Back to Menu", (400, 600 - 50), size, "Back")

    elements.append(backButton)

    for entry in leaderboardDataList:
        if elCreated == limitDisplay:
            break

        # For strftime help I used https://www.programiz.com/python-programming/datetime/strftime

        formattedDate = entry[2].strftime("%m/%d/%Y, %H:%M")
        text = f"{entry[0]} Score Achieved  |  {entry[1]} Days Survived  |  Achieved on {formattedDate}"

        displayedEntry = menuButton.MenuButton(ds, text, (400, yStart), size, None)
        displayedEntry.size = 15  # shrink text
        elements.append(displayedEntry)
        yStart += 50

    headingText = pygame.font.Font(pygame.font.match_font("yugothicyugothicuisemiboldyugothicuibold"), 100)
    headingTextSurface = headingText.render(f"Leaderboard", True, (255, 255, 255))
    headingTextRect = headingTextSurface.get_rect()
    headingTextRect.center = (size[0] / 2, size[1] / 6)
    headingPackage = (headingTextSurface, headingTextRect)
        

    return ds, elements, headingPackage

def drawLeaderboard(dS, scr, el, header):
    dS.fill((0, 0, 0))
    dS.blit(header[0], header[1])
    for i in el:
        i.render()
        if i.triggerLoop == "Back":
            returnMess = i.checkInteraction(pygame.mouse.get_pos(), pygame.mouse.get_pressed())
            if not(returnMess == None):
                trigLoop = returnMess
                return trigLoop
    scr.blit(dS, (0,0))
    pygame.display.update()