import random

while True:
    choice = input("Choose rock, paper, or scissors: ")

    options = ["rock", "paper", "scissors"]
    if choice not in options:
        print("Invalid choice!")
        continue
    computer_choice = random.choice(options)

    print(choice)
    print(computer_choice)

    if choice == computer_choice:
        print("It's a tie!")
    elif choice == "rock" and computer_choice == "scissors":
        print("You win!")
    elif choice == "paper" and computer_choice == "rock":
        print("You win!")
    elif choice == "scissors" and computer_choice == "paper":
        print("You win!")
    else:
        print("You lose and Computer wins!")
    play_again = input("Play again? (yes/no) ")
    
    if play_again == "no":
        break
        
        
    




