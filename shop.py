class Shop:
    def __init__(self, surf):
        self.ds = surf

        self.availableUpgrades = [] # list filled with available upgrades
        self.purchasedUpgrades = []

    def setup(self): # sets up shop HUD
        pass

    def update(self, mousePos, events): # check if buttons selected similair to menuButton system
        pass


    def upgrade(self): # if button clicked on specific upgrade, activate that upgrade by removing it from available and putting it in purchased
        pass