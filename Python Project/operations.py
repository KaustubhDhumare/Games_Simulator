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
    

