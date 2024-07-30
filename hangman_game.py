import random

name = input("Enter name: ")
print("Hello " + name + ", play hangman!")


secret_words = ["Madrid", "İstanbul", "Barcelona", "Berlin", "London", "Washington", "Rome"]

secret_word = random.choice(secret_words).lower()

guess_string = ""

lives = 10 

while lives > 0:
    character_left = 0 
    displayed_word = ""
    for character in secret_word:
        if character in guess_string:
            displayed_word += character
        else:
            displayed_word += "-"
            character_left += 1
    
    print(displayed_word)

    if character_left == 0:
        print("You Won!")
        break

    guess = input("Guess a letter: ").lower()

    
    if len(guess) != 1:
        print("Please enter only one letter.")
        continue
    
    if guess in guess_string:
        print("You already guessed that letter. Try another one.")
        continue
    
    guess_string += guess

    if guess not in secret_word:
        lives -= 1 
        print("Wrong!")
        print(f"You have {lives} lives left")

    if lives == 0:
        print("You Lost :( The secret word was " + secret_word)