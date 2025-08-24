import random
import sys

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

cards = [11, 2, 3,4,5,6,7,8,9,10,10,10,10]

def new_card(card_collection):
    card_collection.append(random.choice(cards))
    return card_collection

while True:
      print(f"{logo}\n")
      user_cards = []
      user_cards = new_card(user_cards)
      user_cards = new_card(user_cards)
      computer_cards = []
      computer_cards = new_card(computer_cards)
      computer_cards = new_card(computer_cards)
      more_user_cards_req = True
      more_comp_cards_req = True


      print(f"Your cards: {user_cards}")
      print(f"The Computer's first card: {computer_cards[0]}")

      is_blackjack = False
      if sum(user_cards)==21 and sum(computer_cards)<21:
            print("User BLACKJACK!!! You Win!")
            is_blackjack = True
      elif sum(user_cards)==21 and sum(computer_cards) == 21:
            print("User and Computer BLACKJACK!!! Game Tied")
            is_blackjack = True

      while more_user_cards_req and not is_blackjack:
            new_card_req = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if new_card_req == 'y':
                  user_cards = new_card(user_cards)
            else :
                  more_user_cards_req = False
            
            while sum(user_cards) > 21:
                  if 11 in user_cards :
                        index = user_cards.index(11)
                        user_cards[index] = 1
                  else:
                        more_user_cards_req = False
            
            print(f"Your cards: {user_cards}")

      if sum(user_cards)<=21 and not is_blackjack:
            while more_comp_cards_req:
                  if sum(computer_cards) < 17 :
                        computer_cards = new_card(computer_cards)
                  elif 17 <= sum(computer_cards) < 21:
                        more_comp_cards_req = False
                  else :
                        while sum(computer_cards)>21:
                              if 11 in computer_cards :
                                    index = computer_cards.index(11)
                                    computer_cards[index] = 1
                              else:
                                    more_comp_cards_req = False
      
      if not is_blackjack:
            print(f"Your cards: {user_cards} and their sum = {sum(user_cards)}")
            print(f"The Computer's cards: {computer_cards} and their sum = {sum(computer_cards)}")
            if (sum(user_cards)>sum(computer_cards) and sum(user_cards)<=21) or sum(computer_cards) > 21:
                  print("You win")
            elif sum(user_cards) == sum(computer_cards) and sum(user_cards)<=21 and sum(computer_cards) <= 21:
                  print("The Game is Tied")
            else:
                  print("You Lose")

      play_again = input("Do you want to play again? Type 'y' or 'n': ")
      if play_again == 'n':
            print("Goodbye")
            break
