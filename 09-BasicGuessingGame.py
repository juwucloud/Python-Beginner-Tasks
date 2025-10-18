import random

number = random.randint(1, 10)

guess = 0

guess = int(input("\n\nGuess my number between 1 and 100\n\n"))
while guess != number:
    if guess == number:
        break
    else:
        guess = int(input(f"\nYou guessed {guess}. That's not my number. Try again!\n\n"))

print(f"\nYou guesses {guess}. That's correct!\n")