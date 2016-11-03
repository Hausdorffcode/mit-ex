# Problem Set 5: Ghost
# Name: 
# Collaborators: 
# Time: 
#

import random
import string

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print "  ", len(wordlist), "words loaded."
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq


# (end of helper code)
# -----------------------------------

# Actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program.
wordlist = load_words()

# TO DO: your code begins here!

def display_fragment(fragment):
    print "Current word fragment: '" + fragment + "'"

def is_vaild_letter(letter):
    return letter in string.ascii_letters

def player_number(player):
    if player:
        return '2'
    else:
        return '1'

def find_str(fragment, wordlist):
    isIn = False
    for word in wordlist:
        if  fragment in word:
            isIn = True
    return isIn

def who_wins(fragment, player, wordlist):
    if len(fragment) > 3 and fragment in wordlist:
        print "Player " + player_number(player) + " loses because '" + fragment + "' is a word!"
        print "Player " + player_number(not player) + " wins!"
        return True
    elif not find_str(fragment, wordlist):
        print "Player " + player_number(player) + " loses because no word begins with '" + fragment + "'!"
        print "Player " + player_number(not player) + " wins!"
        return True
    else:
        return False
                
def input_letter(player, fragment):
    letter = "1"
    while not is_vaild_letter(letter):
        if player:
            letter = raw_input("Player 2 says letter: ")
        else:
            letter = raw_input("Player 1 says letter: ")
    fragment += string.lower(letter)
    return fragment

def whosTurn(player):
    if player:
        print "Player 2's turn."
    else:
        print "Player 1's turn."

def play_game(wordlist):
    print "Welcome to Ghost!"
    player = False
    print "Player 1 goes first."
    fragment = ''
    display_fragment(fragment)
    
    while True:
        fragment = input_letter(player, fragment)
        print
        display_fragment(fragment)
        if who_wins(fragment, player, wordlist):
            break
        else:
            player = not player
            whosTurn(player)

play_game(wordlist)

