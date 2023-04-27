import random
 
# Randomly choose winning number
winning_number = random.randint(1,10)
 
# Limits user to four guesses
guesses_remaining = 4
 
print("You have four attempts to guess the correct number. Give it a shot!")
 
keep_playing = "true"
while keep_playing == "true":   
    guess = int(input("\nGuess a number between 1 and 10: "))
    # Decrease guess counter by one each time to limit to four guesses.
    guesses_remaining = guesses_remaining - 1
    if guess == winning_number:
        print ("Winner! Winner! Chicken Dinner! You guessed the correct number. ")
        # End game after correct guess.
        keep_playing = "false"
    else:
    # Counter to determine amount of guesses left
        if guesses_remaining == 0:
            print ("\nYou are out of tries! The winning number was:",winning_number, "\n\nBetter luck next time!")
        # End game after max attempts.
            keep_playing = "false"
        elif guess != winning_number:
            print("\nSorry, that is not the correct number. Try again!")