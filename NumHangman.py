import random

#first function implementation that generates a random 10 digit number
def generate_random_number(length):
    return ''.join(random.choices('0123456789', k=length))

#second function implementation that shows the numbers in a cetain format
def display_word(word, guessed_letters):
    return ''.join(char if char in guessed_letters else '_' for char in word)

#main game function
def hangman_game():

    #primary initializations
    random_number = generate_random_number(10)
    guessed_digits = set()
    max_attempts = 5
    attempts = 0
    game_won = False

    print("Welcome to Number Hangman!")
    print("Guess the random number. It contains 10 digits.")

    while attempts < max_attempts:
        print("\nNumber:", display_word(random_number, guessed_digits))

        if set(guessed_digits) == random_number:
            game_won = True
            break

        guess = input("Guess a digit: ")

        if guess.isdigit() and len(guess) == 1:
            if guess in guessed_digits:
                print("You've already guessed that digit.")
            else:
                guessed_digits.add(guess)
                if guess not in random_number:
                    attempts += 1
                    print("Incorrect guess! Attempts left:", max_attempts - attempts)
                else:
                    print("Correct guess!")

        else:
            print("Please enter a single digit.")

    if game_won:
        print("Congratulations! You guessed the number:")

    if attempts >= max_attempts:
        print("Sorry, you've run out of attempts. The number was:", random_number)

#main game function call
hangman_game()
