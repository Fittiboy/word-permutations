#!/bin/python
from sys import argv
# Permutations.
# W, L, P, B, M, E

words = []

# Item must be comprised of 4 ingredients.  Repeat ingredients are acceptable.
letters = ['W', 'L', 'P', 'B', 'M', 'E']

def make_all_words(list, word_length, word=""):
    if len(word) == word_length:
        words.append(word)
    else:
        index = len(word)
        for letter in list:
            if index == len(word):
                word += letter
            else:
                word = word[:len(word) - 1] + letter
            make_all_words(list, word_length, word)

make_all_words(letters, int(argv[1]))

for item in words:
    print(item)
