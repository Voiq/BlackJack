from art import logo
import random
import os
print(logo)

user_cards=[]
computer_cards=[]

def dealer_card():       #Random card
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]             
    card=random.choice(cards)
    return card

def score(cards):
    if 11  in cards and 10 in cards and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards)>21:
        user_cards.remove(11)
        return user_cards.append(1)
    return sum(cards)


def compare(score1,score2):
   if score1 == score2:
      return "Draw"
   elif score1 == 0:
      return "You win"
   elif score2==0:
      return "You lose"
   elif score1>21:
      return "You lose"
   elif score2>21:
      return "You win"
   elif score1>score2:
      return "You win"
   elif score2>score1:
      return "You lose"




def blackjack():
    print(logo)
    game_over=False
    for _ in range(2):
        user_cards.append((dealer_card()))
        computer_cards.append((dealer_card()))
    while not game_over:
      player_score=score(user_cards)
      computer_score=score(computer_cards)
      print(f"Your cards {user_cards}, your score {player_score}")
      print(f"Computer's first card {computer_cards[0]}")
      if player_score==0 or computer_score==0 or player_score>21:
        game_over=True
      else:
         draw_again=input("Type y if you want to draw again or n to pass")
         if draw_again=="y":
            user_cards.append(dealer_card())
         else:
            game_over=True      

    while computer_score != 0 and computer_score<17:
     computer_cards.append(dealer_card())
     computer_score=score(computer_cards)

    print(compare(player_score,computer_score)) 


while input("Do you want to play another game of black jack type y or n") == "y":
   os.system('cls')
   blackjack()
