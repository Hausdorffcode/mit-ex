# 6.00 Problem Set 6
#
# The 6.00 Word Game
#

import random
import string
import time
import itertools

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

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

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    The score for a word is the sum of the points for letters
    in the word, plus 50 points if all n letters are used on
    the first go.

    Letters are scored as in Scrabble; A is worth 1, B is
    worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string (lowercase letters)
    returns: int >= 0
    """
    score = 0
    for letter in word:
        score += SCRABBLE_LETTER_VALUES[letter.lower()]
    if len(word) == n:
        score += 50
    return score

#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print letter,              # print all on the same line
    print                              # print an empty line

#
# Make sure you understand how this function works and what it does!
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    num_vowels = n / 3
    
    for i in range(num_vowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(num_vowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    freq = get_frequency_dict(word)
    newhand = {}
    for char in hand:
        newhand[char] = hand[char]-freq.get(char,0)
    return newhand
    #return dict( ( c, hand[c] - freq.get(c,0) ) for c in hand )
        

#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, points_dict):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
    
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    """
    freq = get_frequency_dict(word)
    for letter in word:
        if freq[letter] > hand.get(letter, 0):
            return False
    return points_dict.get(word, 0) != 0

#
# Problem #4: Playing a hand
#
def play_hand(hand, points_dict):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * When a valid word is entered, it uses up letters from the hand.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing a single
      period (the string '.') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
    """    
    total = 0
    initial_handlen = sum(hand.values())
    #time_limit = float(raw_input('Enter time limit, in seconds, for players: '))
    time_limit = get_time_limit(points_dict, 1)
    while sum(hand.values()) > 0:
        print 'Current Hand:',
        display_hand(hand)
        start_time = time.time()
        #userWord = raw_input('Enter word, or a . to indicate that you are finished: ')
        #userWord = pick_best_word(hand, points_dict)
        userWord = pick_best_word_faster(hand, rearrange_dict)
        end_time = time.time()
        total_time = end_time - start_time
        if total_time == 0:
            total_time = 0.01 ##void the total_time become 0
        print "it took %.2f seconds to provide an answer." % total_time
        time_left = time_limit - total_time
        if time_left < 0:
            print 'Total time exceed %f seconds.' % time_limit
            break;
        print "You have %.2f seconds remaining" % time_left
        if userWord == '.':
             break
        else:
            isValid = is_valid_word(userWord, hand, points_dict)
            if not isValid:
                print 'Invalid word, please try again.'
            else:
                points = get_word_score(userWord, initial_handlen)
                total += points
                print '%s earned %d points. Total: %d points' % (userWord, points, total)
                hand = update_hand(hand, userWord)
    print 'Total score: %d points.' % total


#
# Problem #5: Playing a game
# Make sure you understand how this code works!
# 
def play_game(points_dict):
    """
    Allow the user to play an arbitrary number of hands.

    * Asks the user to input 'n' or 'r' or 'e'.

    * If the user inputs 'n', let the user play a new (random) hand.
      When done playing the hand, ask the 'n' or 'e' question again.

    * If the user inputs 'r', let the user play the last hand again.

    * If the user inputs 'e', exit the game.

    * If the user inputs anything else, ask them again.
    """

    hand = deal_hand(HAND_SIZE) # random init
    
    while True:
        cmd = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if cmd == 'n':
            hand = deal_hand(HAND_SIZE)
            play_hand(hand.copy(), points_dict)
            print
        elif cmd == 'r':
            play_hand(hand.copy(), points_dict)
            print
        elif cmd == 'e':
            break
        else:
            print "Invalid command."

def get_words_to_points(word_list):
    """
    Return a dict that maps every word in word_list to its point value
    """
    points_dict = {}
    for word in word_list:
        points_dict[word]= get_word_score(word, len(word)+1)
    return points_dict

def get_word_rearrangement(word_list):
    d = {}
    for word in word_list:
        d[''.join((lambda x : (x.sort(), x)[1])(list(word)))] = word
    return d

def pick_best_word(hand, points_dict):
    """
    Return the highest scoring word form points_dict that can be made with the given hand.

    Return '.' if no words can be made with the given hand.
    """
    highest_score = 0
    highest_word = '.'
    for word in points_dict.keys():
        if is_valid_word(word, hand, points_dict) and points_dict[word] > highest_score:
            highest_word = word
            highest_score = points_dict[word]
    return highest_word

def pick_best_word_faster(hand, rearrange_dict):
    highest_score = 0
    highest_word = '.'
    subsets = []
    listhand = []
    for key in hand.keys():
        for i in range(0, hand[key]):
            listhand.append(key)
    for i in range(1, sum(hand.values())+1):
        subsets.extend(list(itertools.combinations(listhand, i)))
    #print subsets
    for subset in subsets:
        w = ''.join((lambda x: (x.sort(), x)[1])(list(subset)))
        #print w
        if (w in rearrange_dict) and points_dict.get(rearrange_dict[w], 0) > highest_score :
            highest_word = rearrange_dict[w]
            highest_score = points_dict[rearrange_dict[w]]
    #print highest_word
    return highest_word

def get_time_limit(points_dict, k):
    """
     Return the time limit for the computer player as a function of the
     multiplier k.
     points_dict should be the same dictionary that is created by
     get_words_to_points.
    """
    start_time = time.time()
    # Do some computation. The only purpose of the computation is so we can
    # figure out how long your computer takes to perform a known task.
    for word in points_dict:
        get_frequency_dict(word)
        get_word_score(word, HAND_SIZE)
    end_time = time.time()
    return (end_time - start_time) * k 

#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    points_dict = get_words_to_points(word_list)
    rearrange_dict = get_word_rearrangement(word_list)
    play_game(points_dict)
