import random

"""A number-guessing game."""

# Put your code here
# greet player
print("Howdy, what's your name?")

#get player name
name = raw_input("Type in your name: ")
#choose random number between 1 and 100
random_num = random.randint(1, 100)
print("%s, I'm thinking of a number between 1 and 100" % name)
print("Try to guess my number")

#repeat forever:
guess = 0
num_guesses = 0
best_score = 0

while guess != random_num:
#    get guess
    # try-except statement to check for invalid things
    try:
        print("You have %i guesses left" %(7 - num_guesses))
        guess = float(raw_input("Your guess? "))
    except ValueError:
        print ("Hey dummy, type a number! Guess again.")
        continue

#    check if guess is int or float
    if not guess.is_integer():
        print ("Your guess is being rounded down to an integer.")
    guess = int(guess)
#    increase number of tries
    num_guesses += 1

#    Check for valid guess
    if guess < 1 or guess > 100:
        print ("You git! Guess is out of range 1-100, guess again!")
        num_guesses -= 1
#    if guess is incorrect:
    elif guess != random_num and num_guesses >= 7:
        print("That was the wrong number! You ran out of guesses :(")
        print("Your best score is %i!" % (best_score))
        play_again = raw_input("Press 'y' to play again, anything else to quit: ")

        if play_again.lower() == 'y':
            guess = 0
            num_guesses = 0
            random_num = random.randint(1, 100)
            print("\n\nNEW GAME! I'm thinking of a new number between 1 and 100")
            print("Try to guess my number")
        else:
            break
    elif guess > random_num:
        print ("Your guess is too high, try again")
    elif guess < random_num:
        print ("Your guess is too low, try again")
    else:
#        congratulate player
        print("Well done, %s! You found my number in %i tries!" % (name, num_guesses))

        if best_score == 0:
            best_score = num_guesses
        elif best_score > num_guesses:
            best_score = num_guesses
        print("Your best score is %i!" % (best_score))
        play_again = raw_input("Press 'y' to play again, anything else to quit: ")

        if play_again.lower() == 'y':
            guess = 0
            num_guesses = 0
            random_num = random.randint(1, 100)
            print("\n\nNEW GAME! I'm thinking of a new number between 1 and 100")
            print("Try to guess my number")
