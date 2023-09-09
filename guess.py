
from random import randint



print("Welcome to the Guess the Number game!")

print("I'm thinking of a number between 1 and 100. Can you guess what it is?")

guess = randint(1,100)

user_input = int(input())

if user_input > 100:
    print('no values superior than 100 are accepted')

while user_input != guess:
   if user_input < guess:
      print('your guess is too low, try again')
      user_input = int(input())
   elif user_input > guess:
      print('your guess is too high , try again')
      user_input = int(input())
   elif user_input == guess:
      print('You guessed it correct')
     











