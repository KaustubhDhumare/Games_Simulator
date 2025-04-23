class Menu():
    def game_menu(self,game_function):

        while True:
                print('''
                    ***************  
                    Game menu
                    ***************  
                    1. Play game    
                    2. Exit
                    ***************
                    ''')
                try:
                    game_choice = int(input("Enter your Game setting: "))
                    if game_choice == 1:
                        game_function()
                    else:
                        break
                except ValueError:
                    print("Please enter a valid number.")