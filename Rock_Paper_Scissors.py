import random
user_choice = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors\n"))
if user_choice < 0 or user_choice >= 3 :
    print("Invalid Number")
else :
    computer_choice = random.randint(0,2)
    if computer_choice == 0:
        print("Computer chose rock")
    elif computer_choice == 1:
        print("Computer chose paper")
    else :
        print("Computer chose scissors")
    

    if user_choice == computer_choice :
        print("Tie")
    elif (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1) :
        print("You win")
    else :
        print("You lose")
