from code import play
play()


# >>> using only file programming whole program without importing

# import random 
# from art import logo 
# print(logo)
# print("Welcome to the Number Guessing Game")
# print("I'm thinking of a number between 1 and 100")
# computer_guess=random.randint(1,100)
# # print(computer_guess)
# choose_level=input("Choose diffculty, Type 'Easy' or 'Difficult' ").lower()
# # n is the no of chances player get for gessing
# if choose_level=='easy':
#   n=10
#   # print(f"You have {n} attemps to guess the number")
  
# elif choose_level=='difficult':
#   n=5
#   # print(f"You have {n} attemps to guess the number")
  
# else:
#   print("Invalid command")
# print(f"You have {n} attemps to guess the number")

# # next_guess=True
# no_guessed=False
# # while n>0 or next_guess:
# while n>0:
#   guess = int(input("Make a guess :"))
#   n=n-1
#   if n !=0 :
#     if guess < computer_guess:
#       print("Too Low")
#       print("Guess again")
#       print(f"You have {n} attempts remaining to guess the number.")
#     elif guess > computer_guess:
#       print("Too high")
#       print("Guess again")
#       print(f"You have {n} attempts remaining to guess the number.")
#     elif guess == computer_guess:
#       print(f"You got it! The answer was {guess}.")
#       no_guessed=True

# if n==0 and no_guessed==False:
#   print("You have run out of guesses, you lose")
