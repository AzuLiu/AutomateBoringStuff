import random
secretNumber =  random.randint(1,20)
print('I am thinking about a number between 1 and 20.')
for guessTaken in range(1,7):
    print('Take a guess.')
    guess = int(input())
    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high')
    else:
        break
if guess == secretNumber:
    print('Great job!You guesses my numbers in '+ str(guessTaken)+' guesses')
else:
    print('Nope.The number I was thinking of was '+ str(secretNumber))
