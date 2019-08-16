# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 18:44:12 2018

@author: joshc
"""

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print("  ", len(wordList), "words loaded.")
    return wordList

def getFrequencyDict(sequence):
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
	
def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    if word in wordList:
        wordDict=getFrequencyDict(word)
        handCopy=hand.copy()
        for i in wordDict:
            if (i in handCopy and handCopy[i]<wordDict[i]) or i not in handCopy:
                return False
        return True
    else:
        return False


wordList=loadWords()
hand = {'r': 1, 'a': 3, 'p': 2, 't': 1, 'u':2}
word = "honey"
print(isValidWord(word,hand,wordList))