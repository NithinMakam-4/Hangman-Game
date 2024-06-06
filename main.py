from hangman_logo_stages import logo, stages, logo1, won, lost
from hangman_words import word_list
import random
from collections import Counter
from replit import clear

total_plays = 0
total_score = 0

play_again = True


while play_again:
    total_plays += 1
    print(f"GAME NO: {total_plays}")
    

    choosen_word = random.choice(word_list)
    word_length = len(choosen_word)
    for i in range(word_length):
        print("_",end = ' ')
    

    print(logo)
    print(logo1)
    print(choosen_word)
    print("At Max, You can Guess Six Times Wrong")


    lives = 6
    end_of_game = False
    letterguessed = ''
    guessed_word = ''

    while not end_of_game:
        print()
        guess = input('Enter the letter to guess the Word:').lower()

        if not guess.isalpha():
            print('Guess only a ALPHABETIC Letter')
            continue
        elif len(guess) > 1:
            print('Enter only a SINGLE Letter')
            continue
        elif guess in  letterguessed:
            print("You've already guessed this Letter")
            continue
        elif guess not in letterguessed:
            letterguessed += guess

        if guess in choosen_word:
            number_of_times_guess_in_word = choosen_word.count(guess) 
            guessed_word += guess * number_of_times_guess_in_word 
            print(f"Yeah!, Letter {guess} is a right Guess.")
            if not Counter(choosen_word) == Counter(guessed_word):
                print(f"Your are left with {lives} chances")

        
        else:
            lives -= 1
            print(f"It's a Wrong Guess, You'r left with {lives} chances")
        

        for ch in choosen_word:
            if ch in guessed_word:
                print(ch,end = ' ')
            else:
                print('_',end = ' ')
        print()
        
        if Counter(choosen_word) == Counter(guessed_word):
            end_of_game = True
            total_score += 1
            print(won)
            print(f"You'r Score is {total_score} out of {total_plays} ")
            pa = input('Do You Want to Play Game again? Enter "y" for YES, anything else for NO.').lower()
            if  pa != 'y':
                play_again = False
            lives = 0
            clear()

        elif lives == 0:
            print(lost)
            print(stages[0])
            end_of_game = True
            print(f"You'r Score is {total_score} out of {total_plays} ")
            print(f"The Correct Word is : {choosen_word}")
            pa = input('Do You Want to Play Game again? Enter "y" for YES, anything else for NO.').lower()
            if  pa != 'y':
                play_again = False
            clear()

        if lives != 0 :
            print(stages[lives])
        
