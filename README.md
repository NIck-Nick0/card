# card
#Card Clash: Terminal-Based TCGA strategic, turn-based Trading Card Game (TCG) engine built with Python. 

#This project demonstrates core Object-Oriented Programming (OOP) principles, game state management, and unit testing.

#Features Hero-Card Inheritance: Utilizing Python's class inheritance to share attributes between Heroes and Minions.Dynamic AP System: Actions consume Action Points (AP) which scale as the game progresses ($3 + Turn$).Battlefield Mechanics: A dedicated field state where summoned units can attack either the enemy hero or other units.Armor & Damage Logic: Advanced damage calculation factoring in unit armor:$$Net Damage = \max(0, ATK - AR)$$Cross-Platform UI: Automatic terminal clearing using os.name for a clean experience on Windows and 

#Linux.Unit Testing: Comprehensive test suite using pytest to ensure logic integrity.
#How to PlayClone the Repository:Bash
#git clone https://ghttps://github.com/NIck-Nick0/card-clash.git
#cd card-clash
#Install Requirements:Bashpip install -r requirements.txt if need to test for any reason :) Bash : pytest test_main.py
#Run the Game:python main.py
#Commands:Number (Index): Summon a card from your hand.'a': Perform a Hero Attack (Costs 3 AP).
#'u': Command a unit on the field to attack.
#'e': End your current turn. Running TestsThe project includes unit tests to verify damage calculations, AP management, and health states.


