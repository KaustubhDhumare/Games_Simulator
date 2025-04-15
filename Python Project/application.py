from operations import GamesSimulator
import sys

sim = GamesSimulator()
choice = 0 

def game_menu(game_function):
    while True:
            print('''
                1. Play game
                2. Exit
                ''')
            game_choice = int(input("Enter your Game setting: "))
            if game_choice == 1:
                game_function()
            else:
                break
    
while choice != 4:
    print('''
        Choose your game:  
        1. Rock Paper Scissor    
        2. Number guessing   
        3. Dice rolling game
        4. Exit
          ''')
    
    choice = int(input("Enter your game number: "))

    if choice == 1:
        print("\"Rock Paper Scissor game started\"")
        game_menu(sim.rock_paper_scissor)
            
    elif choice == 2:
        print("\"Number guessing game is started\"")  
        game_menu(sim.number_guessing)
            
    elif choice == 3:
        print("\"Dice rolling game is started\"")
        game_menu(sim.dice_rolling)
        

    elif choice == 4:
        print('exiting the appplication')
        sys.exit()  