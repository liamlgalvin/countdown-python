from random import shuffle, randint
from dictionary import dictionary, in_dictionary,starts_with
import timeit
import sys

# ------------------ VARIABLES ----------------
consonants = ['b','c','d','f','g','h','j','k','l','m', 'n','p','q','r','s','t','v','w','x','y','z']
vowels = ['a', 'e', 'i', 'o', 'u']

# global to hold letters users selected
letters = []
# word list is a global where we will store the words we discover
wordlist = []

# -------------- FUNCTIONS --------------------

def get_word_list():
    return 1

def add_consonant():
    shuffle(consonants)
    letters.append(consonants[0])

def add_vowel():
    shuffle(vowels)
    letters.append(vowels[0])

def add_random():
    options = randint(0,2)
    if options in [0,1] :
        add_consonant()
    else:
        add_vowel()

def get_words(letters, length):
    global wordlist
    for i,letter in enumerate(letters):
        rem_letters = letters.copy()
        rem_letters.pop(i)
        get_words_aux(letter, rem_letters, length)

def get_words_aux(current, rem_letters, length):
    global wordlist
    for i, letter in enumerate(rem_letters):
        new_current = current + letter
        # prevent searching down dead ends (ramificacion y poda). only continues if there is  word tht starts with those letters
        if starts_with(new_current): 
            if new_current not in wordlist:
                if len(new_current) == length:  
                    if in_dictionary(new_current):
                        wordlist.append(new_current)
                else:
                    list2 = rem_letters.copy()
                    list2.pop(i)
                    get_words_aux(new_current, list2, length)
    

#------------------- START GAME -----------------------

def letter_game(wordlist):
   # show the menu to the player
    while True:
        print("Welcome to the word game!")
        print("1. Normal")
        print("2. Random")
        print("3. Solve")
        print("4. Exit")
        selection = input("pick 1, 2 or 3: ")
        if int(selection) in range(1,4):
            break
        elif int(selection) == 4:
            sys.exit()
            
    if int(selection) == 1:
        for i in range (0,9):
            num = input("enter c (consonant) or v (vowel)")
            if num == "c":
                add_consonant()
            elif num == "v":
                add_vowel()
            else:
                add_random()
            print(letters[-1])
    elif int(selection) == 2:
        for x in range(0,9):
            add_random()
    elif int(selection) == 3:
        print("input your letters 1 by one:")
        for i in range (0,9):
            letter = input("enter letter and press enter: ")
            letters.append(str(letter))
    print(letters)
    input("press enter when ready")
    #iterate through possible words starting with 9 down to 1. 
    for i in range(9, 0, -1):
        get_words(letters, i)
        if len(wordlist) > 0:
            print("highest possible word has %i letters"%i)
            #if at least 1 word has been found break
            break 
    return wordlist

# ------------------ MAIN --------------------------
def play_game():
    word_list = letter_game(wordlist)
    print(word_list)