import random

words = ["python", "java", "apple", "guntur", "code"]
word = random.choice(words)
blank = ["_"] * len(word)
life = 6

print("Hangman Game - Guess the word")

while life > 0 and "_" in blank:
    print("Word:", " ".join(blank))
    print("Life:", life)
    letter = input("Enter letter: ")

    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                blank[i] = letter
        print("Correct!")
    else:
        life = life - 1
        print("Wrong!")

if "_" not in blank:
    print("You Won! Word was:", word)
else:
    print("You Lost! Word was:", word)
