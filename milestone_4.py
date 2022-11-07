import random

lists = ['orange','mango','blueburry','papaya','apple']
word_list = lists
word = random.choices(word_list)
    #print(random.choices(mylist, weights = [10, 1, 1], k = 14))   weight = weigh the possibility , k = integer defining the length of the returned list
print(word[0])
word = word[0]
guessed = "_"*len(word)
print(guessed)
word_guessed = []
word_guessed[:0] = guessed
new_word_guessed =[]
new_word_guessed[:0] = guessed
print(word_guessed)
num_letters = len(word)
print(num_letters)
num_lives = 5
list_of_guesses = []


def check_guess(guess):
    guess = guess.lower()
    global num_letters , num_lives , word_guessed
    if guess in word:
        print(f"Good guess! {guess} is in the word")
        i = 0
        for i in range (len(word)):
            if guess == word[i]:
                word_guessed[i] = guess
                print(word_guessed)
        num_letters = num_letters-1


    elif guess in list_of_guesses :
        print ("You already guessed that letter! Here is what you've guessed:")
        print (' '.join(list_of_guesses))

    else:
        print(f'Sorry, {guess} is not in the word. Try again.')
        print(f'You have {num_lives} lives left.')
        num_lives = num_lives-1
        
        


def ask_for_input():
    while True :
        guess = input("Enter single letter: ")

        if len(guess) == 1 and guess.isalpha():
            print(f"Good guess!: {guess}")
            check_guess(guess)
            list_of_guesses.append(guess)
                

        elif guess in list_of_guesses:
            print ("You already guessed that letter! Here is what you've guessed:")
            print (' '.join(list_of_guesses))

        else:
            print('Invalid letter. Please, enter a single alphabetical character.')


ask_for_input()
