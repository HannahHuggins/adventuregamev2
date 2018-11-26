Adventure Game V2
=====
###How to run###

- Open the terminal and change into the Adventure game v2 folder using `cd adventuregamev2`

- You can then run the project by typing `python adventuregamev2.py` or by pressing the play button.
---
###Idea for the game###

I'm currently reading through _learn python the hard way_ by Zed Shaw, and have previously
created a text adventure game from one of the tasks in the book.
This time, I followed the skeleton the author laid out more closely, in an effort to gain a further 
understanding of classes and functions.  

Before I started to write the code for the game, I mapped out the different aspects of the game
and the class hierarchy to see how they interact with each other.  

- The map holds a dictionary of the levels in the game, and enables access to the different
classes.  
 
- The engine says that the game will continue playing through the scenes for as long as the current 
scene is not the last one.  
 
- Each scene is a different class with an _enter_ function that forwards the story and links to other
classes dependant on the option the player chooses.  
 
- Three functions are imported from various built-in dictionaries - exit, randint and dedent.  
Exit will end the game at the current point, randint lets us call a random number (used in line `124`), 
and dedent provides indentations that help to format the strings correctly.  



 