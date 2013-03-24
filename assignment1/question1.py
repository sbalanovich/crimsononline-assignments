import re
import collections
import sys

def common_words(filename):
    """question 1a

    Write a function that takes a path to a text file as input. The function
    should open the file, count the number of occurrences of each word, and
    return a sorted list of the most common words.
    """
    return map(lambda x: x[0], common_words_tuple(filename, sys.maxint))

def common_words_min(filename, min_chars):
    """question 1b

    Modify this function to take a second argument that specifies the
    minimum number of characters long a word can be to be counted.
    """ 
    return [word for word in common_words(filename) if len(word) >= min_chars]

def common_words_tuple(filename, min_chars):
    """question 1c

    Modify this function to return a list of tuples rather than just a list
    of strings. Each tuple should be of the format
        (word, number of occurrences)
    Of course, the list of tuples should still be sorted as in part a.
    """
    words = re.findall('\w+', open(filename).read())
    return collections.Counter(words).most_common()

def common_words_safe(filename, min_chars):
    """question 1d

    Modify your function so that it catches the IOError exception and prints
    a friendly error message.
    """
    try:
        common_words_tuple(filename, min_chars)
    except IOError:
        return "File address not found. Try again"
    pass
