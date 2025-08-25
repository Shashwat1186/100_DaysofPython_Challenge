import random
#ASCII ART
import art

#Import data for the game
from data import data

#create a function to randomly choose 2 people from data and print their characteristics
def select_data():
   account = random.choice(data)
   return account



#compare function to compare the followers of the contestants and update score for correct answer
def compare_acc(acc1, acc2, user_response, sc):
   is_game_running = True
   if acc1["follower_count"] == acc2["follower_count"] :
      print("Both had the same number of followers therefore your score will remain the same")
   elif (acc1["follower_count"] > acc2["follower_count"] and user_response == 'a') or (acc1["follower_count"] < acc2["follower_count"] and user_response == 'b'):
      sc += 1
   else :
      is_game_running = False
   
   return sc, is_game_running

score = 0
#loop and increase score for correct answer and continue the game , for wrong answer end the game
is_game_running=True
account_1 = random.choice(data) 
print(art.logo)
while is_game_running:
   
   account_2 = select_data()
   
   print(f"Compare A: {account_1['name']}, a {account_1['description']}, from {account_1['country']}.")
   print(f"{art.vs_logo}")
   print(f"Compare B: {account_2['name']}, a {account_2['description']}, from {account_2['country']}.")
   user_response = input("Who has more followers? Type 'A' or 'B': ").lower()
   score, is_game_running = compare_acc(account_1, account_2, user_response, score)
   print("\n" * 20)
   print(art.logo)
   if is_game_running:
      print(f"You're right! Your current score: {score}")
   else:
      print(f"Sorry, that's wrong. Final score: {score}")
   account_1 = account_2


