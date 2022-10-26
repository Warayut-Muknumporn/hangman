import random
from re import L



list = ['orange','mango','blueburry','papaya','apple']
word_list = list
word = random.choices(word_list)
#print(random.choices(mylist, weights = [10, 1, 1], k = 14))   weight = weigh the possibility , k = integer defining the length of the returned list
print(word)

guess = input("Enter single letter ")
if len(guess) == 1 and guess.isalpha():
    print("Good guess")
else:
    print("Oops! That is not a valid input")
