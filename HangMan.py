import string
import os
import random
wrong_guess = 0

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

def game(word):
    picked=[]
    input("Enter your name: ")
    sec_n = '**Sandskrup**'
    print("Welcome {}! You are allotted only 5 incorrect guesses, so good luck.".format(sec_n))
    print("Your word is {}".format(word_mask(word,picked), word))

    while wrong_guess < 5:
        guess(word, picked)
        if all(letter in picked for letter in word):
            print('You won {}! The word was {}.'.format(sec_n, word))
            return
    print('You lose {}! The word was {}'.format(sec_n, word))
    

def guess(word, picked):
    global wrong_guess
    print('Picks made thus far: {}'.format(picked))
    print('{} Incorrect guesses'.format(wrong_guess))
    print('{}'.format(word_mask(word,picked)))
    letter = input("Guess a letter: ")

    if verify(letter) == True:
        if letter in picked:
            print("You've already picked that letter! Pick again")
        elif letter in word:
            word_mask(word,picked)
            picked.append(letter.lower())
        else:
            wrong_guess+=1
            picked.append(letter.lower())
        return word, wrong_guess
    elif verify(letter) == False:
        print("Letters only, try again")

def word_mask(word, picked):
    for letter in word:
        if letter in picked:
          word = word.replace(letter, "{} ".format(letter))
        else:
          word = word.replace(letter, "_ ")
    return word

def verify(letter):
    if len(letter) == 1 and letter.__class__ == str:
        return True
    elif len(letter) == 1:
        return False
    

if __name__ == '__main__':
    inp_file = "pocket.txt"
    game(choose_word(read_pocket(inp_file)))

