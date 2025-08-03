print("Welcome to the Treasure Island.\nYour mission is to find the treausre.")
crossroad = input('''You are at a crossroad. Where do you want to go? \n       type "left" or "right"\n''').lower()
if crossroad == "left" :
    lake_crossing = input("""You've come to a lake. There is a island in the middle of the lake. \n  Type "wait" to wait for the boat. Type "swim" to swim across. \n""").lower()
    if lake_crossing == "wait" :
        colour = input("You arrive at the island unharmed. There is a house with 3 doors. \n One red, one blue and one yellow. Which colour do you choose? ").lower()
        if colour == "yellow":
            print("You win")
        elif colour == "red":
            print("You were burned by fire. Game over")
        elif colour == "blue":
            print("You were eaten by beasts. Game Over. ")
        else :
            print("Game over")
    else :
        print("You were attacked by a trout. Game over")
else :
    print("You fall into a hole. Game over")
