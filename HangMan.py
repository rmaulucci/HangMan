#!/usr/bin/env python3
import random

def read_word_list(filename):
    with open(filename) as file:
        return [line for line in file]

def choose_word(word_list):
    return word_list[random.randint(0, len(word_list) - 1)].strip().lower()

class HangMan(object):
    def __init__(self, word):
        self.word = word
        self.guesses = set()

    @property
    def guessed_correctly(self):
        return all(letter in self.guesses for letter in self.word) or self.word in self.guesses

    @property
    def incorrect_guesses(self):
        return sum(1 for guess in self.guesses if guess not in self.word)

    @property
    def masked_word(self):
        return " ".join(letter if letter in self.guesses else "_" for letter in self.word)

    def get_guess(self):
        while True:
            guess = input("Guess a letter or the word: ")
            if len(guess) not in (1, len(self.word)):
                print("Try again. Just a single character or a word of the same length.")
                continue
            if not guess.isalpha():
                print("Oh jeez, try that again. Just alphabetic characters please.")
                continue
            if guess in self.guesses:
                print("You've already guessed that! Try again.")
                continue
            return guess

    def get_taunt(self):
        taunts = [
            "That was a terrible idea.",
            "Uh, no.",
            "I don't think you're actually trying. I hope you're not.",
            "Something about monkeys and typewriters."
        ]
        return taunts[random.randint(0, len(taunts) - 1)]

    def run(self):
        MAX_INCORRECT_GUESSES = 5

        while True:
            guesses_str = ", ".join(sorted(self.guesses)) if self.guesses else "nothing"
            incorrect_guesses_left = MAX_INCORRECT_GUESSES - self.incorrect_guesses
            print("Your word is {}, you've guessed {} and you have {} incorrect guess(es) left.".format(self.masked_word, guesses_str, incorrect_guesses_left))

            guess = self.get_guess()
            self.guesses.add(guess)

            if guess in self.word:
                if self.guessed_correctly:
                    break
            else:
                if self.incorrect_guesses == MAX_INCORRECT_GUESSES:
                    break
                print(self.get_taunt())

        print("You {}! The word was {}.".format("won" if self.guessed_correctly else "lost", self.word))

def main():
    word = choose_word(read_word_list("pocket.txt"))
    game = HangMan(word)
    game.run()

if __name__ == '__main__':
    main()
