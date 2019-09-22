# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 22:26:09 2018

@author: joshc
"""

from ps4a import *
import time

WORDZLIST_FILENAME = "words.txt"
def loadWordz():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDZLIST_FILENAME, 'r')
    # wordList: list of strings
    wordzList = []
    for line in inFile:
        wordzList.append(line.strip().lower())
    print("  ", len(wordzList), "words loaded.")
    return wordzList


def isValidWordz(word, hand, wordz):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordz: dictionary (string -> int)
    """
    if word in wordz:
        wordDict=getFrequencyDict(word)
        handCopy=hand.copy()
        for i in wordDict:
            if (i in handCopy and handCopy[i]<wordDict[i]) or i not in handCopy:
                return False
        return True
    else:
        return False
    
def compChooseWordz(hand,wordz,n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: dictionary (string -> int)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    # Create a new variable to store the maximum score seen so far (initially 0)
    bestScore = 0
    # Create a new variable to store the best word seen so far (initially None)  
    bestWord = None
    # For each word in the wordList
    for word in wordz:
        # If you can construct the word from your hand
        if isValidWordz(word, hand, wordz):
            # find out how much making that word is worth
            score = wordz[word]
            # If the score for that word is higher than your best score
            if (score > bestScore):
                # update your best score, and best word accordingly
                bestScore = score
                bestWord = word
    # return the best word you found.
    return bestWord
#
def compPlayHandz(hand, wordz, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: dictionary (string -> int)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    # Keep track of the total score
    totalScore = 0
    # As long as there are still letters left in the hand:
    while (calculateHandlen(hand) > 0) :
        # Display the hand
        print("Current Hand: ", end=' ')
        displayHand(hand)
        # computer's word
        word = compChooseWordz(hand, wordz, n)
        # If the input is a single period:
        if word == None:
            # End the game (break out of the loop)
            break
            
        # Otherwise (the input is not a single period):
        else :
            # If the word is not valid:
            if (not isValidWordz(word, hand, wordz)) :
                print('This is a terrible error! I need to check my own code!')
                break
            # Otherwise (the word is valid):
            else :
                # Tell the user how many points the word earned, and the updated total score 
                score = wordz[word]
                if len(word)== n:
                    score+=50
                totalScore += score
                print('"' + word + '" earned ' + str(score) + ' points. Total: ' + str(totalScore) + ' points')              
                # Update hand and show the updated hand to the user
                hand = updateHand(hand, word)
                print()
    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    print('Total score: ' + str(totalScore) + ' points.')

def playGame(wordz, hand={}):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordz: dictionary (string -> int)
    """
    while True:
        start=input('Enter n to deal a new hand, r to replay the last hand, or e to end game:')
        if start == 'r' and hand == {}:
            print('You have not played a hand yet. Please play a new hand first!')
        elif start =='e':
            break
        elif start == 'n':
            hand=dealHand(HAND_SIZE)
        elif start != 'e' and start != 'r' and start !='n':
            print('Invalid command')
        while (start !='e') and (start =='n' or start =='r') and (hand != {}):
            comp=input('Enter u to have yourself play, c to have the computer play:')
            if comp == 'u':
                playHand(hand,wordList,HAND_SIZE)
                start=''
            elif comp == 'c':
                compPlayHandz(hand, wordz, HAND_SIZE)
                start=''
            elif comp != 'u' and comp !='c':
                print('Invalid command')
#                
wordzList = loadWordz()
wordz=getFrequencyDict(wordzList)

for i in wordz:
    valu=[]
    for j in i:
        valu.append(SCRABBLE_LETTER_VALUES[j])
    valu=sum(valu)*len(valu)
    wordz[i]=valu
    
if __name__ == '__main__':
    playGame(wordz, hand={})