import random
from re import L

list = ['orange','mango','blueburry','papaya','apple']
word_list = list
word = random.choices(word_list)
#print(random.choices(mylist, weights = [10, 1, 1], k = 14))   weight = weigh the possibility , k = integer defining the length of the returned list
print(word)


def check_guess(guess):
    while True :
        if len(guess) == 1 and guess.isalpha():
            print(f"Good guess!: {guess}")
            guess = guess.lower()
            break
        print("Invalid letter. Please, enter a single alphabetical character.")
        guess = input("Enter single letter ")

    if guess in word[0]:
        print(f"Good guess! {guess} is in the word")
    else:
        print(f'Sorry, {guess} is not in the word. Try again.')
        
    return guess


def ask_for_input():
    guess = input("Enter single letter ")

    check_guess(guess)

ask_for_input()