import random

def get_random_word():
    word_list = [
        'python', 'hangman', 'programming', 'computer', 'developer', 'challenge',
        'algorithm', 'function', 'variable', 'condition', 'loop', 'iteration',
        'syntax', 'debug', 'compile', 'binary', 'integer', 'string', 'array',
        'dictionary', 'boolean', 'exception', 'class', 'object', 'inheritance'
    ]
    return random.choice(word_list)

random_word = get_random_word()

def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def play_hangman():
    word = get_random_word()
    guessed_letters = set()
    attempts = 10

    print("Welcome to Hangman Game!")

    while attempts > 0:
        print("\nWord:", display_word(word, guessed_letters))
        print(f"Remaining attempts: {attempts}")
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print("You've already guessed that letter. Try another one.")

        guessed_letters.add(guess)

        if guess in word:
            print("Good guess!")
            if all(letter in guessed_letters for letter in word):
                print(f"Congratulations! You have gussed the word: {word}")
                break
        else:
            attempts -= 1
            print("Wrong guess.")
            if attempts == 0:
                print(f"Game over! The word was: {word}")

if __name__ == "__main__":
    play_hangman()