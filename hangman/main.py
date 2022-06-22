# Hangman
import random
import os
import hangman_art
import hangman_words

word_list = hangman_words.word_list
stages = hangman_art.stages

# Choose some random word from the list above
chosen_word = random.choice(word_list)
# Set the number of lives
lives = 6

print(hangman_art.logo)

# Create a list with empty blanks
display = []
for i in chosen_word:
    display.append("_")
print(' '.join(display))

while "_" in display and lives > 0:
    # Ask the user to make a guess
    guess = input("Guess a letter: ").lower()
    os.system('clear')

    if guess not in display:
        # Check if the guess is correct
        if guess in chosen_word:
            # Fill the blanks
            for i in range(0, len(chosen_word)):
                if guess == chosen_word[i]:
                    display[i] = guess
        else:
            lives -= 1
            print(
                f"You guessed {guess}, that's not in the word, you loss a life"
                )
            print(stages[lives])
    else:
        print(
            f"You've already guessed the letter {guess}: {' '.join(display)}")

    # Print the status
    print(' '.join(display))

# Print the result of the game
if "_" in display:
    print("Loss")
else:
    print("Win!!")
