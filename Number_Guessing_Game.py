import random

number = random.randint(1,100)


def game(num_guesses):  
    game_condition = False
    for i in range(num_guesses, 0, -1):
        print(f"You have {i} guesses for the number I'm thinking of")
        user_guess = int(input("Take a guess: "))
        if user_guess > number :
            print("Too high")
        elif user_guess < number :
            print("Too Low")
        else :
            print(f"Correct! The answer was {user_guess}. Thanks for completing that!\n")
            game_condition = True
            break

        if not game_condition and i == 1 :
            print("You couldn't guess the correct number. Please try again.\n")


while True:
    print("I'm thinking of a number between 1 and 100, try to guess it")
    difficulty_type = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if difficulty_type == "hard":
        num_guesses = 5
    elif difficulty_type == "easy":
        num_guesses = 10
    else:
        print("Invalid Input")

    game(num_guesses)

    play_again = input("Do you want to play again. Type 'y' for yes and 'n' for no: \n")
    
    if play_again != 'y':
        print("GoodBye")
        break


