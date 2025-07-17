import random

HANGMANPICS = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    ========="""
]

words = ['cat', 'dog', 'pig']
choice = random.choice(words)
final = ['_' for _ in choice]
wrong_guesses = 0
max_attempts = len(HANGMANPICS) - 1  # 6 attempts

print("Welcome to Hangman!")
print("Word:", ' '.join(final))

while wrong_guesses < max_attempts:
    user = input("Guess a letter: ").lower()

    if len(user) != 1 or not user.isalpha():
        print("Please enter a single valid letter.")
        continue

    if user in final:
        print("You already guessed that letter.")
        continue

    found = False
    for idx, char in enumerate(choice):
        if char == user:
            final[idx] = user
            found = True

    if not found:
        wrong_guesses += 1
        print("Wrong guess!")

    print(HANGMANPICS[wrong_guesses])
    print("Word:", ' '.join(final))

    if ''.join(final) == choice:
        print("🎉 You won! The word was:", choice)
        break
else:
    print("😞 Game over! The word was:", choice)
