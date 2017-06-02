import string
import os
import random
inc_guess = 0

def read_pocket(filename):
    pocket = []
    with open(filename, "r") as read:
        for line in read:
            pocket.append(line)
        return pocket
            
def choose_word(pocket):
    word = pocket[random.randint(0,len(pocket))]
    word = word.lower()
    word = word.strip()
    return word

def game_intro(word):
    picked=[]
    input("Enter your name: ")
    sec_n = '**Sandskrup**'
    print("Welcome {}! You are allotted only 5 incorrect guesses, so good luck.".format(sec_n))
    print("Your word is {}".format(word_mask(word,picked), word))

    while inc_guess < 5:
        guess(word, picked)
        if word == word_mask(word,picked):
            print('You won {}! The word was {}.'.format(sec_n, word))
            return
    print('You lose {}! The word was {}'.format(sec_n, word))
    

def guess(word, picked):
    global inc_guess
    print('Picks made thus far: {}'.format(picked))
    print('{} Incorrect guesses'.format(inc_guess))
    print('{}'.format(word_mask(word,picked)))
    letter = input("Guess a letter: ")

    if verify(letter) == 0:
        if letter in picked:
            print("You've already picked that letter! Pick again")
        elif letter in word:
            word_mask(word,picked)
            picked.append(letter.lower())
        else:
            inc_guess+=1
            picked.append(letter.lower())
        return word, inc_guess
    elif verify(letter) == 1:
        print("Letters only, try again")

def word_mask(word, picked):
    for letter in word:
        if letter in picked:
          word = word.replace(letter, "{}".format(letter))
        else:
          word = word.replace(letter, "_ ")
    return word

def verify(letter):
    if len(letter) == 1 and letter.__class__ == str:
        return 0
    elif len(letter) == 1:
        return 1
    

if __name__ == '__main__':
    inp_file = os.getcwd() + r"\pocket.txt"
    game_intro(choose_word(read_pocket(inp_file)))

