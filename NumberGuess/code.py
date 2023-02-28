from random import randint
from art import logo
def play():
  """Its whole game code"""
  
  easy_level_turns=10
  hard_level_turns=5
  
# Function to check user's guess against actual answer.
  def check_answer(guess, answer, turns):
    if guess > answer:
      print("Too high.")
      return turns - 1
    elif guess < answer:
      print("Too low.")
      return turns - 1
    else:
      print(f"You got it {answer}, You Win!")
      
# function set the difficulty of the game    
  def set_difficulty():
    level=input("Set the Difficulty of the game Type 'easy' or 'hard': ").lower()
    if level=='easy':
      return easy_level_turns
    else:
      return hard_level_turns
      
# runs the game
  def game():
    
    print(logo)
    
    print("Welcome to the Number Guessing Game!! ")
    print("I'm thinking of a number between 1 and 100: ")
    answer = randint(1,100)

    turns = set_difficulty()
    
    guess=0
    while guess != answer:
      print(f"You have {turns} attempts remaining to guess the number.")
      guess=int(input("Make a guess: "))
      turns=check_answer(guess, answer, turns)
      if turns==0:
        print(f"You ran out of turns, You lose, The {answer}was the answer")
      elif guess != answer:
        # clear()
        print("Guess again")
  game()