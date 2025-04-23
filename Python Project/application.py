from operations import GamesSimulator
from menu import Menu
import sys

menu = Menu()
sim = GamesSimulator()
choice = 0 


while choice != 5:
    print('''
        *************************
        Choose your game
        *************************     
        1. Rock Paper Scissor    
        2. Number guessing    
        3. Dice rolling game  
        4. Number run         
        5. Exit               
        *************************  
        ''')
    
    choice = int(input("Enter your game number: "))

    if choice == 1:
        print("\"Rock Paper Scissor game started\"")
        menu.game_menu(sim.rock_paper_scissor)
            
    elif choice == 2:
        print("\"Number guessing game is started\"")  
        menu.game_menu(sim.number_guessing)
            
    elif choice == 3:
        print("\"Dice rolling game is started\"")
        menu.game_menu(sim.dice_rolling)   

    elif choice == 4:
        print("\"Number run game is started\"")
        menu.game_menu(sim.number_run)

    elif choice == 5:
        print('exiting the appplication')
        sys.exit()  