import random
class Hangman:
# Parameter


    def __init__(self, word):
        print(word)
        global num_letters, word_guessed, num_lives
        num_lives = 5
        num_letters = len(word)
        guessed = "_"*len(word)
        word_guessed = []
        word_guessed[:0] = guessed
        print("_________")
        print ("|	 |")
        print ("|")
        print ("|")
        print ("|")
        print ("|")
        print ("|________")
        print(f'The mistery word has {num_letters} characters')
        print(f'{word_guessed}')
        pass
    
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
                    if guess in list_of_guesses:
                        num_letters = num_letters
                    else:
                        num_letters = num_letters-1
            print(f'You have: {num_letters} letter left')
        #elif num_letters = 0:
            
        elif guess in list_of_guesses :
            print ("You already guessed that letter! Here is what you've guessed:")
            print (' '.join(list_of_guesses))

        else:
            print(f'Sorry, {guess} is not in the word. Try again.')
            num_lives = num_lives - 1
            if num_lives == 4:
                    print("_________")
                    print ("|    |")
                    print ("|    O")
                    print ("|    |")
                    print ("|    |")
                    print ("|")
                    print ("|________")
            elif num_lives == 3:
                    print("_________")
                    print ("|    |")
                    print ("|    O")
                    print ("|   \|/")
                    print ("|    |")
                    print ("|")
                    print ("|________")
            elif num_lives == 2:
                    print("_________")
                    print ("|	 |")
                    print ("|    O")
                    print ("|   \|/")
                    print ("|    |")
                    print ("|   /")
                    print ("|________")
            elif num_lives == 1:
                    print("_________")
                    print ("|	 |")
                    print ("|    O")
                    print ("|   \|/")
                    print ("|    |")
                    print ("|   / \ ")
                    print ("|________")

            print(f'You have {num_lives} lives left.')
            
            

        
        pass    
            


    def ask_for_input():
        global  num_letters, num_lives
        while True :
            guess = input("Enter single letter: ")

            if len(guess) == 1 and guess.isalpha():
                print(f"Good guess!: {guess}")
                Hangman.check_guess(guess)
                list_of_guesses.append(guess)
                if num_letters == 0:
                    break 
                elif num_lives <= 0:
                    break

            elif guess in list_of_guesses:
                print ("You already guessed that letter! Here is what you've guessed:")
                print (' '.join(list_of_guesses))

            else:
                print('Invalid letter. Please, enter a single alphabetical character.')
        pass

def play_game(word):
    game = Hangman(word)
    while True:
        if num_letters == 0:
            print("Congratulations! You won!")
            break
        elif num_lives == 0:
            print(f'You lost! The word was {word}')
            break
        else:
            Hangman.ask_for_input()
    pass


if __name__=='__main__':
    word_list = ['apple', 'banana', 'orange', 'pear'] #, 'strawberry', 'watermelon'
    word = random.choices(word_list)
    word = word[0]
    list_of_guesses = []
    
    play_game(word)
#%%