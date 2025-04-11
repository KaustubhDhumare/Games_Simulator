from operations import GamesSimulator
import sys
sim = GamesSimulator()

choice = 0 

while choice != 3:
    print('''
        Choose your game:  
        1. Rock Paper Scissor    
        2. Number guessing   
        3. Exit
          ''')
    
    choice = int(input("Enter your game number: "))

    if choice == 1:
        print("\"Rock Paper Scissor game started\"")
        i = 1
        chance = int(input("Enter the number of time you want to play this game : "))
        while i <= chance:
            print(f"You have {chance} chance you use {i} chance")
            sim.rock_paper_scissor()
            i += 1
    
    elif choice == 2:
        print("\"Number guessing game is started\"")
        sim.number_guessing()

    elif choice == 3:
        print("Exiting the application")
        sys.exit()
