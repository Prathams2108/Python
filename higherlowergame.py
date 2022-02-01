# Import the random Module
import random
#import the module which has the list data
from game_data import data
from art import logo
#define a function called game
def game():
  #From the list Choose a random value 1
  comp_a=random.choice(data)
  name1=comp_a["name"]
  abt1=comp_a["description"]
  cntry1=comp_a["country"]
  #declare a flag and set it's value to true
  final_result=True
  score=0
  #the while loop runs until the flag is true
  while final_result is True:
    print(logo)
    # Display The current Score
    print(f"You're Right! Currrent Score: {score}")
    print(f"Compare A: {name1}, a {abt1}, from{cntry1}")
    from art import vs
    print(vs)
    #From the list choose another random value
    comp_b=random.choice(data)
    if comp_a==comp_b:
      comp_b=random.choice(data)
    name2=comp_b["name"]
    abt2=comp_b["description"]
    cntry2=comp_b["country"]
    print(f"Against B: {name2}, a {abt2}, from {cntry2}")
    #Ask the user for a input 
    guess=input("Who has more followers? Type 'A' or 'B' ").lower()
    #Check if the user has entered the value 'a'
    if guess=="a":
      #compare the follower_count values of both a and b and increment the value of score
      if comp_a["follower_count"]>comp_b["follower_count"]:
        score+=1
        print(f"You're Right! Currrent Score: {score}")
        name1=name2
        abt1=abt2
        cntry1=cntry2
        comp_a["follower_count"]=comp_b["follower_count"]
        #Clear the screen after every round
        clear()
      #The game ends if the user guess is wrong and the final score is displayed
      else:
        clear()
        print(f"Sorry that's wrong. Final score: {score}")
        final_result=False
    # Check if the user input is 'b'
    elif guess=="b":
      #Compare the follower count and increment the value of score if the user guess was correct
      if comp_b["follower_count"]>comp_a["follower_count"]:
        score+=1
        print(f"You're Right! Current Score: {score}")
        name1=name2
        abt1=abt2
        cntry1=cntry2
        comp_a["follower_count"]=comp_b["follower_count"]
        clear()
      #The game ends of the user guess was wrong and the final score is displayed
      else:
        clear()
        print(f"Sorry that's wrong. Final score: {score}")
        final_result=False