# Tetris-Bot
A program that plays Tetris (NES) on its own

**Note:** I decided to put the "plays" functionality on hold. After doing some research it seems that using Python to send inputs to an application on Mac could be a lot more tedious than I was expecting.  
Due to this, I'm going to spend more time working on the algorithm that finds the best position for the next piece. If I get that working well, *then* I'll look more into how I can control the application through code so it can play itself.

**TODO:** 

1. Figure out how I'm actually going to calculate the best position for the next piece
  * Currently thinking of minimizing perimeter somehow. The way I currently calculate perimeter (excluding the border of the game board) should lend itself nicely to this.  
  Main hurdle with that is that I'm not sure how I should be testing each position.
2. Implement some kind of loop for screengrabs and calculations
  * Currently I need to run `python main.py` in order to do everything once.
  * Ideally it should loop every time the next piece changes
3. Allow the program to control the game on its own
  * Literally no idea how I'm going to do this. There seems to be a lot of options, but many I've found are specific to Windows. In a perfect world this would be able to run on Windows or Mac, but based on what I've read that would be twice the work.

**Known Issues:**

1. The program detects whether or not a block exists by seeing if each space is black or not. Black means no block, not black means there's a block. This will stop working if the game ever gets to level 146 because that's the first level where the center of a block becomes black.  
Not a critical issue *at least* until the game can play itself because getting to level 146 manually would take a *while*. 

2. The perimeter/area (but most importantly perimeter) calculation will only ignore the falling piece if there is at least 1 empty row between the falling piece and the highest point of the tower.  
Not a critical issue at the moment because ideally the game should only be calculating as soon as the next piece changes, so the falling piece will be at its highest point.

3. The game needs to be in a precise position in order for literally everything to work correctly.  
Not a critical issue because the program will always launch in that position, even if I move it around before closing it. I would like for this program to be more flexible with the game's position, though.