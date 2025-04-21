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

        print(f"you choose {reversedict[you]}\ncomputer choose {reversedict[computer]}")

        if(computer == you ):
            print("Its a Draw!")
        else:
            if(computer == 1 and you == -1) or (computer == -1 and you == 0) or (computer == 0 and you == 1) : 
                print("You Win!")

            else:
                print("You Lose")
    
    def number_guessing(self):
        from random import randint
        num = randint(1,100)
        print("Guess the number between 1 to 100")
        attempts = 0
        while True:
            guess = int(input("Enter a number: "))
            attempts += 1
            if guess > num :
                print("Number is too high!")
            elif guess < num:
                print("Number is too low!")
            else:
                print(f"Correct! you took {attempts} attempts to guess")
                break
    
    def roll_dice(self, player_name):
        from random import randint
        player = []
        total = 0
        start = "ROLL"
        r = input(f"{player_name}\nType \"Roll\" to start: ").upper()
        for i in range(3):
            if r != start:
                print("Only type \"Roll\" to play the game")
                break
            else:
                roll = randint(1,6)
                player.append(roll)
                        
        for i in player:
            if i == 6:
                player.append(randint(1,6))

        for score in player:
            total += score

        return total
    
    def dice_rolling(self):
        p1 = self.roll_dice("Player 1")
        p2 = self.roll_dice("Player 2")

        print(f"Player 1 Score is {p1}\nPlayer 2 Score is {p2}")
        print()

        if p1 == p2:
            print("It's a draw")
        elif p1 > p2:
            print("Winner is Player 1")
        else:
            print("Winner is Player 2")

    def number_run(self):
        from random import randint
        score = 0
        print("Enter number betweem 1 to 10 to start number run")

        while True :
            computer = randint(1,10)
            player = int(input("Enter a number: "))
            print(f"Your number: {player}, Computer's number: {computer}")

            if computer == player :
                print(f"You Lose, \nYour Score is {score}")
                break
            
            score += 1
                
        
