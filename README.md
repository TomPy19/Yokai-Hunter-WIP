# WIP
 
Team Members:
Evan Sok
Thomas Personett 

**Part 1: Game Design**
We will be creating a 2D roguelike game similar to Vampire Survivors with additional attributes similar to Risk of Rain. 

Gimmick : random drops from chests and time-scaling(gets stronger over time)  monsters

Concept Sketch(UI under develop):


Our MC makes a deal with a time demon to go back in time to eradicate the yokai. She goes through different ages to collect souls(could change) from the bosses found in these places. 

Game Mechanics:
-Only arrow keys
-the combat is sort of like passive effects from the items obtained in chests
-inventory is the items collected but it is only just a way to display what you have

Collectables:
-Gain exp and gold on monster kill
-Collect weapons through weapon chests (max 6 at once)
-Collect upgrade items to improve stats through item chests

**Part 2: Development Design**
Main - Control gameplay loop: All classes must pass information through this class to interact
Model - Control logic
View - Control display
Controller - Control inputs
Animation class - Control animations
Enemy class - Holds information about stats of every enemy
Stats class - Holds all information about game statistics
Player class - Holds information about inventory and player stats
Weapon class - Holds information about all weapons
Boss classes - Holds information about each boss in separate classes
Item class - Holds information about each item
Chest class - Controls logic of chest spawning/looting

UI: Health, Exp, Time, Displayed Inventory, Control Popups, Pause Menu, Startup Screen

**Part 3: Division of Labor**
Evan will mostly be working on art/sound design for the game, but would like to code some aspects as well. Thomas will be doing the opposite, working mostly on coding the functionality of the game, but will work a bit on art/sound design.

Evan - 60 hours total
Thomas - 60 hours total

Time constraint will probably be our biggest potential issue but we plan to spend a lot of free time working on the project to create at least something we are proud of. We also will probably run into problems implementing certain aspects of our game through the pygame library, but through a lot of creative problem solving I’m sure our collaborative minds can make anything happen.

**Part 4: Timeline**
You will have 3 milestones to complete before submitting your final game project. The timeline should include tasks and deadlines for each milestone. Use your Game and Development Design sections to help build this timeline. Assign a group member to each task according to their roles and responsibilities.



*Milestone 1: March 29*
Completed by Thomas:
	- Basic player movement and monster that follows player: March 15
	- Figure out monster ai: March 27
Completed by Evan:
	- Full concept art for all entities and items: 27 //map still in progress

*Milestone 2: April 12*
	- Mechanic done where a weapon comes into contact with entity: March 15 //POSTPONED TO MILESTONE 2
	- Figure out all item management: March 27 //POSTPONED TO MILESTONE 2
	- Figure out damage scaling math: March 22 //POSTPONED TO MILESTONE 2
	- Full sprites and level design complete (unpolished): April 12
	- Figure out core gameplay loop mechanics: April 12
	- Time portals to move between stages
	- Boss movesets
	- Loop/end/reset game
	- Stat tracking for final endscreen

*Final Game Submission: April 26*
	- Completed and polished game
	- Completed Game Document game

*Final Exam Presentation & Submission: May 4*
	- Presentation materials (e.g. slides, videos)

*MVP:*
	- Single map, some weapons working and dealing damage to monsters(that have some ai to follow where mc is going). Probably a boss fight once the timer hits a certain time. 


*Random Brain Dumping*
	- Single pc - Mari Chitose (千歳真璃）
	- 3 stages - village, feudal, modern tokyo - starting sequence: apocalyptic tokyo; ending sequence: neo tokyo
	- 3 bosses
	- 5 enemy types
	- Endless playability
	- Time scaling damage and health
	- Random/Pickable Chests
	- Exp + Gold drops



#UPDATES:
**MILESTONE 1 UPDATES:**
	-Our game is slowly evolving, as expected time was our biggest opponent. We have decided to shoot for our Minimum Viable Product, a single map with the mc fighting monsters, and a boss fight in the end.

Technical Challenges:
	Evan: Currently in the process of making the sprites and map design, both of which I have no experience doing. This adds a learning curve for me to overcome. I do not think that these challenges will significantly impact the development timeline. After doing some research, I understand the gist of it and will now focus on creating it instead of how to create it.

	Thomas: I had a bit of trouble implementing the kind of movement I wanted, but got it figured out. I also had trouble figuring out animations, but it was mostly my fault because I was being stubborn and not organizing my code into classes. With those two challenges taking a tad longer than expected, I did not have time to work on any basic weapon mechanics yet. I am getting faster and faster at understanding core concepts of pygame the longer I use it, however. I do not believe our final development timeline will be impacted.

Project Timeline:
	- Postponed tasks will be updated above. A name will be attached to the task that was delegated to that person.
