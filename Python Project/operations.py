class GamesSimulator:
    def rock_paper_scissor(self):
        import random
        '''
        1 Rock
        -1 Paper
        0 scissor
        '''
        computer = random.choice([1, -1, 0]) 
        print("Choose from \n r: rock \n p: paper \n s: scissor")
        youstr = input("Enter your choice: ")
        youdict = {"r": 1, "p": -1, "s": 0}
        reversedict = { 1: "Rock", -1: "Paper", 0: "scissor"}
        you = youdict[youstr]

        print(f"you chose {reversedict[you]}\ncomputer chose {reversedict[computer]}")

        if(computer == you ):
            print("Its a Draw!")
        else:
            if(computer == 1 and you == -1): 
                print("You Win!")
            
            elif(computer == 1 and you == 0):
                print("You Lose!")
            
            elif(computer == -1 and you == 1):
                print("You Lose!")
            
            elif(computer == -1 and you == 0):
                print("You WIn!")
            
            elif(computer == 0 and you == 1):
                print("You Win!")
            
            elif(computer == 0 and you == -1):
                print("You Lose!")
            
            elif():
                print("Something went wrong!")
    
    def number_guessing(self):
        from random import randint
        print("Input only integers")

        num = randint(1, 20)
        for i in range (3, 0, -1):
            print(f"You have left {i} chance")
            print()
            guess = int(input("Enter your guess: "))
            if num == guess:
                print("Correct answer!, You win")
                break
            else:
                print("Wrong answer!, Try again")

        print()

        if i == 1:
            print("You lost the game, play again")
    
    def dice_rolling(self):
        from random import randint
        # Player 1
        player1 = []
        p1 = 0
        click = "Roll"
        start = click.upper()
        r1 = input("Player 1\nType \"Roll\" to start: ")
        u1 = r1.upper()
        for i in range(3):
            if u1 != start:
                print("Only type \"Roll\" to play the game")
                break
            else:
                dice1 = randint(1,6)
                player1.append(dice1)
                        
        for i in player1:
            if i == 6:
                extra_roll = randint(1,6)
                player1.append(extra_roll)

        for p1_Score in player1:
            p1 = p1_Score + p1


        # Player 2
        player2 = []
        p2 = 0
        r2 = input("Player 2\nType \"Roll\" to start: ")
        u2 = r2.upper()
        for i in range(3):
            if u2 != start:
                print("Only type \"Roll\" to play the game")
                break
            else:
                dice2 = randint(1,6)
                player2.append(dice2)
                        
        for i in player2:
            if i == 6:
                extra_roll = randint(1,6)
                player2.append(extra_roll)

        for p2_Score in player2:
            p2 = p2_Score + p2


        print(f"Player 1 Score is {p1}\nPlayer 2 score is {p2}")
        print()

        if p1 == p2 :
            print("It's a draw")

        else:
            if p1 > p2 :
                print("Winner is player 1")
            else:
                print("Winner is player 2")

