import random

name = input("- What is your name?\n")
tries = 15
print(f"Hello, {name}! Welcome to the word guessing game!")
print(f"You have a total of {tries} tries to win the game!")

word_list = [    'elephant', 'giraffe', 'kangaroo', 'pineapple', 'avocado', 'volcano', 'jazz',
    'whisper', 'galaxy', 'dinosaur', 'parachute', 'python', 'robot', 'puzzle',
    'unicorn', 'mystery', 'lighthouse', 'ocean', 'strawberry', 'butterfly',
    'blizzard', 'astronaut', 'firefly', 'tsunami', 'whirlpool', 'rainbow',
    'sapphire', 'emerald', 'chocolate', 'horizon', 'cosmos', 'nebula',
    'labyrinth', 'echo', 'crystal', 'lightning', 'echo', 'tornado', 'phantom',
    'cascade', 'phoenix', 'serendipity', 'eclipse', 'quicksilver', 'aurora',
    'midnight', 'solstice', 'reverie', 'epiphany', 'zephyr', 'glacier', 'breeze',
    'tempest', 'whimsy', 'sonata', 'nebula', 'stardust', 'mirage', 'echo'
                 ]

def random_word():
    return random.choice(word_list)

word_to_guess = random_word().lower()
display = ["_"] * len(word_to_guess)

while tries > 0:
    print("\n" + " ".join(display))
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter only.")
        continue
    if guess in word_to_guess:
        for index, letter in enumerate(word_to_guess):
            if letter == guess:
                display[index] = guess
        print(f"Good guess! '{guess}' is in the word.")
    else:
        tries -= 1
        print(f"Sorry, '{guess}' is not in the word. You have {tries} tries left!")

    if "_" not in display:
        print(f"\nCongrats, you guessed the word: {word_to_guess}")
        break
if "_" in display:
    print(f"\nYou are out of tries! The word was: {word_to_guess}")