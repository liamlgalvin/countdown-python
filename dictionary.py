text_file =  open("words.txt", "r")
dictionary = text_file.readlines()

''' 
function that checks whether a given word is in the dictionary or not

It calls the auxilary function recursively returning either TRUE or FALSE.

It uses recursive binary search to find the word.
'''

def in_dictionary(word):
    pos = int(len(dictionary) / 2)
    left = 0
    right = len(dictionary) - 1

    if word == str(dictionary[pos]):
        return True
    elif word < str(dictionary[pos]):
        right = pos
        pos = int((pos / 2))
        return in_dictionary_aux(word, right , left, pos)
    elif word > str(dictionary[pos]):
        left = pos
        pos = int(((right + pos) / 2))
        return in_dictionary_aux(word, right , left, pos)
    return False

def in_dictionary_aux(word, right , left, pos):
    new_word = str(dictionary[pos]).strip()
    if word.strip() == new_word:
        return True
    elif left >= pos or right <= pos:
        return False
    elif word < str(dictionary[pos]):
        right = pos
        pos = int((left + pos) / 2)
        return in_dictionary_aux(word, right , left, pos)
    elif word > str(dictionary[pos]):
        left = pos
        pos = int(((right + pos) / 2))
        return in_dictionary_aux(word, right , left, pos)
    return False

''' 
function that checks whether the there is at least one word in the dictionary that starts with the 
given string.

It calls the auxilary function recursively returning either TRUE or FALSE.

It uses recursive binary search to find the word.
'''

def starts_with(first):
    left = 0
    right = len(dictionary)
    pos = int(len(dictionary)/2)
    return starts_with_aux(left, right, pos, first)

def starts_with_aux(left, right, pos, first):
    word_length = len(first)
    # word_starts takes the first n number of letters from the current dictionary element
    word_starts = ((str(dictionary[pos]))[:word_length]).strip()

    if str(first.strip()) == str(word_starts):
        return True
    elif left >= pos or right <= pos:
        return False
    elif first < word_starts:
        right = pos
        pos = int((left + pos) / 2)
        return starts_with_aux(left, right, pos, first)
    elif first > word_starts:
        left = pos
        pos = int(((right + pos) / 2))
        return starts_with_aux(left, right, pos, first)
