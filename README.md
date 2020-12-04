# AstroDefense 3000
## CY300 Final Project Submission - CDT Wyatt Evers

### Project Overview
This project is a simple game inspired by retro arcade games such as Missile Defense. The player is a rotating cannon at the bottom of the screen that shoots at asteroids falling towards the planet. The player scores points for each asteroid they destroy, and they lose health for each asteroid that makes contact with the planet. The game revolves around a day system, with the game getting progressively harder each day. The user is able to view their best scores on the leaderboard accessible from the main menu.

### Instructions
#### Installation and Running the Game
To run the game, download and extract the .zip file. Open the folder, and run the **main.py** file through a python interpreter. The user must have the **pygame** module installed. This can be done easily through the pip install process.
#### Game Instructions / Controls
After running the **main.py** file, the main menu will launch. To start a new game, click **New Game**. The cannon is rotated left and right using the **left and right arrow keys**, and the cannon is fired using the **spacebar**. The goal is to shoot the asteroids before they collide with the planet. If three collide, the player loses and the **Game Over** screen appears. From here, the player can either exit or return to the main menu.
#### Leaderboard Feature
After playing at least one round, the leaderboard menu will have records to display. The leaderboard is accesses by clicking the **Leaderboard** button on the main menu. Here, the player can view their top 6 games, with the score, days survived, and date displayed.

### File Walkthrough
#### Assets Folder:
Contains all assets needed for game to run.
#### .gitignore:
Used to prevent git from committing the pygame cache and personal leaderboard
#### README.md
The file you are currently reading, formatted to look fancy in GitHub
#### asteroid.py
Contains the custom Asteroid class for asteroid functionality
#### cannon.py
Contains the custom Cannon class for cannon functionality
#### collision.py
Contains the custom Collision class for collision functionality
#### gameFileIO.py
Contains the custom functions needed for file IO and leaderboard functionality
#### hud.py
Contains the custom functions needed to create the Heads Up Display in the game window. Also contains hudButton class which is subclass of the MenuButton class.
#### main.py
Contains the main game loop. This file is run for the program to launch.
#### menuButton.py
Contains the custom MenuButton class which forms the foundation of all interactive elements in menus.
#### menuFunctions.py
Contains custom functions to augment usage of MenuButton class.
#### projectile.py
Contains custom Projectile class which handles all projectiles shot by player.
#### sampleLeaderboard.txt
This is an example of what **leaderboard.txt** will look like after the user plays a few games. The **leaderboard.txt** file is not meant to be viewed as a text file, it simply contains raw data that is formatted by the **Leaderboard** loop n the menu.

### Possible Future Improvements
#### Sound
Due to time constraints, I was unable to incorporate sound into the product. This was a low priority that was cut but could be implemented fairly easily with a little more development time.
#### Progression
Some sort of progression would make the game more enjoyable. Faster cannon rotation, larger projectiles, and faster reloading would ideally be available to purchase by the player using their earned score.
#### Save/Load game
Hand in hand with the implementation of progression would have been a save and load game feature. Progression and the Save/Load game feature would give the player motivation to keep coming back to the game to progress further.


### Citations and Code Ownership
To create this project, I mainly relied on the Python and Pygame references. Initially, I used a variety of Pygame tutorials to learn how to get started with the basic functionality, but no tutorial that I used had any relation with my game concept. All of the code in this project is my own, except for 2 partial lines I needed when integrating the Python datetime library into the leaderboard system. Those 2 partial lines contain URL citations in comments and are located in **gameFileIO.py**
