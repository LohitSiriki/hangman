import random

def choose_word():
    # words = ["python", "hangman", "programming", "challenge", "coding"]
    with open('words.txt', 'r') as f:
        words = f.read().splitlines()
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def display_hangman(incorrect_attempts):
    hangman_art = [
        '''
        ------
        |    |
        |
        |
        |
        |
        -
        '''
        ,
        '''
        ------
        |    |
        |    O
        |
        |
        |
        -
        '''
        ,
        '''
        ------
        |    |
        |    O
        |    |
        |
        |
        -
        '''
        ,
        '''
        ------
        |    |
        |    O
        |   /|
        |
        |
        -
        '''
        ,
        '''
        ------
        |    |
        |    O
        |   /|\\
        |
        |
        -
        '''
        ,
        '''
        ------
        |    |
        |    O
        |   /|\\
        |   /
        |
        -
        '''
        ,
        '''
        ------
        |    |
        |    O
        |   /|\\
        |   / \\
        |
        -
        '''
    ]

    return hangman_art[incorrect_attempts]

def hangman():
    word_to_guess = choose_word()
    guessed_letters = []
    incorrect_attempts = 0
    max_attempts = 6

    print("Welcome to Hangman!")

    while True:
        print("\nAttempts left:", max_attempts - incorrect_attempts)
        print(display_hangman(incorrect_attempts))
        print(display_word(word_to_guess, guessed_letters))

        guess = input("Guess a letter: ").lower()

        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print("You already guessed that letter. Try again.")
            elif guess in word_to_guess:
                print("Good guess!")
                guessed_letters.append(guess)
            else:
                print("Incorrect guess.")
                guessed_letters.append(guess)
                incorrect_attempts += 1

            if "_" not in display_word(word_to_guess, guessed_letters):
                print("Congratulations! You guessed the word:", word_to_guess)
                break

            if incorrect_attempts == max_attempts:
                print("Sorry, you ran out of attempts. The word was:", word_to_guess)
                break
        else:
            print("Invalid input. Please enter a single letter.")

if __name__ == "__main__":
    hangman()
