import random

"""A number-guessing game."""

# Put your code here
# greet player
print("Howdy, what's your name?")

#get player name
name = raw_input("Type in your name: ")
#choose random number between 1 and 100
random_num = random.randint(1,100)
print("%s, I'm thinking of a number between 1 and 100" %name)
print("Try to guess my number")

#repeat forever:
guess = 0
num_guesses = 0
while guess != random_num:    
#    get guess
    guess = raw_input("Your guess? ")
#    if guess is incorrect:
    if guess != random_num:
#        give hint
        if guess > random_num:
            print ("Your guess is too high, try again")
        elif guess < random_num
            print ("Your guess is too low, try again")
#        increase number of guesses
        num_guesses += 1
#    else:
    else:
#        congratulate player"""
        print("Well done, %s! You found my number in %i tries!" % (name, num_guesses))

