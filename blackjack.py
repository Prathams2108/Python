import random
def deal_card():
  """Returns a random card from the deck"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card=random.choice(cards)
  return card
def calculate_score(c):
  """Used to calculate the score"""
  if sum(c)==21 and len(c)==2:
    return 0
  if 11 in c and sum(c)>21:
    c.remove(11)
    c.append(1)
  else:
    return sum(c)
def compare(u_score,com_score):
  if u_score==com_score:
    return("It is a draw")
  elif com_score==0:
    return("You Lose Computer has a BlackJack")
  elif u_score==0:
    return("You Win You Have a BlackJack")
  elif u_score>21:
    return("You Lose It is a Bust")
  elif com_score>21:
    return("You Win Computer has a bust")
  elif u_score>com_score:
    return("You Win")
  else:
    return("You Lose")
user_cards=[]
computer_cards=[]
game_over=False
for i in range(2):
  user_cards.append(deal_card())
  computer_cards.append(deal_card())
while game_over==False:
  u_score=calculate_score(user_cards)
  print(f"Your Cards:{user_cards} Your Score:{u_score}")
  com_score=calculate_score(computer_cards)
  print(f"Computer Card: {computer_cards[0]}")
  if u_score==0 or u_score>21 or com_score==0:
    game_over=True
  else:
    deal=input("Would you like to deal another card?Type y or n: ")
    if deal=="y":
      user_cards.append(deal_card())
      u_score=calculate_score(user_cards)
      while com_score!=0 and com_score<17:
        computer_cards.append(deal_card())
        com_score=calculate_score(computer_cards)
    else:
      game_over=True
print(f"Your Final Hand: {user_cards},final score:{u_score}")
print(f"Computer's Final Hand:{computer_cards},final score={com_score}")
print(compare(u_score,com_score))


