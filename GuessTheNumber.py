# This is a guess the number game.
import random
import sys

guessesTaken = 0


#    import subprocess32 as subprocess


print('Hello! What is your name?')
if sys.version_info[0] < 3:
    myName = raw_input()   #In Python 2.x always don't use input() because until Python 3.x input() was broken by bugs
else:
    myName = input()  # For Python 3.X

number = random.randint(1, 20)
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')

while guessesTaken < 6:
    print('Take a guess.') # There are four spaces in front of print.
    if sys.version_info[0] < 3:
        guess = raw_input()   # Python2.7
    else:
        guess = input()        #Python on 3.X
    guess = int(guess)
    guessesTaken = guessesTaken + 1
    if guess < number:
        print('Your guess is too low.') # There are eight spaces in front of print.
    if guess > number:
        print('Your guess is too high.')
    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number)