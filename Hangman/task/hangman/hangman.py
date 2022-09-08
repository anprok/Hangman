import random

print('H A N G M A N')
words = ['python', 'java', 'swift', 'javascript']
wins = 0
loses = 0
while True:
    print()
    print('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
    command = input()
    if command == 'play':
        word_to_guess = random.choice(words)
        hidden_word = '-' * int(len(word_to_guess))
        i = 1
        letters = []
        while i <= 8:
            print()
            print(hidden_word)
            input_letter = input("Input a letter: ")
            if len(input_letter) != 1:
                print("Please, input a single letter.")
                continue
            if not input_letter.islower() or not input_letter.isalpha():
                print("Please, enter a lowercase letter from the English alphabet.")
                continue
            if input_letter in letters:
                print("You've already guessed this letter.")
                continue
            guessed = False
            if hidden_word.find(input_letter) >= 0:
                i += 1
                print("No improvements.")
                continue
            for pos, char in enumerate(word_to_guess):
                if char == input_letter:
                    hidden_word = hidden_word[:pos] + char + hidden_word[pos + 1:]
                    guessed = True

            if not guessed:
                i += 1
                print("That letter doesn't appear in the word.")
            if hidden_word.find('-') == -1:
                break
            letters.append(input_letter)
        print()
        if hidden_word.find('-') == -1:
            print(f"You guessed the word {hidden_word}!\nYou survived!")
            wins += 1
        else:
            print("You lost!")
            loses += 1
    elif command == 'results':
        print(f'You won: {wins} times')
        print(f'You lost: {loses} times')
    elif command == 'exit':
        break
    else:
        print("Incorrect input")

