
from random import randint



print("Welcome to the Guess the Number game!")

print("I'm thinking of a number between 1 and 100. Can you guess what it is?")

guess = randint(1,100)

your_guess = int(input())

if your_guess < guess:
    print('your guess is too low, try again')
elif your_guess > guess:
    print('your guess is too high , try again')
elif your_guess == guess:
    print('you guessed it right, it s {guess}!')







