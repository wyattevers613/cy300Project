# This file will contain the funtions needed to save and load the game

saveGameFile = "saveGame.txt"

def saveGame(saveGameFile, gameData): #gameData will be a list or tuple, probably nested, of all attributes (upgrades, dayNum, score) to be written to the save file
    # this function will write gameData to the saveFile in a format to be read by load game
    pass


def loadGame(saveGameFile):
    # loadGame will open the saveGame file, pick out the gameData, and return a packaged nested list of gameData for the game to load
    # return gameData
    pass

leaderboard = "leaderboard.txt"

def updateLeaderboard(leaderboardFile, ldrData): # ldrData will be package of all data to display on leaderboard, score, dayNum, etc.
    pass