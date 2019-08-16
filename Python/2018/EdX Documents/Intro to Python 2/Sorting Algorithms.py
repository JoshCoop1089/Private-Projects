# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 21:28:46 2018

@author: joshc

Sorting Algorithms (Complexity of calculation listed next to name)

1)  MergeSort O(nlog(n))

2)  SelectionSort O(n^2)
        Can guarantee first elements are sorted if you need to stop
        searching before end of list, which is why it is a better sort
        than BubbleSort

3)  BubbleSort O(n^2)

4)  MonkeySort O(?) why would you ever even consider this
"""

#MergeSort Algorithm
def merge(left,right):
    '''
    Take two sorted lists, left and right, and check the first positions
    against each other, append the smaller one to the output list, and 
    increase the index on the list the smaller number came from.
    
    At the end, one list will be empty, so append the other list onto result.
    '''
    result=[]
    i,j=0,0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    while i < len(left):
        result.append(left[i])
        i+=1
    while j < len(right):
        result.append(right[j])
        j+=1
    return result

def merge_sort(L):
    '''
    Take a list L, and split it in half.  If it is already length 0 or 1, it 
    is sorted.  Keep splitting the lists until you reach base case (recursive 
    calls) and then merge the split lists piece by piece until you've combined
    all the recursived lists and get back to the main level.
    '''
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L)//2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left,right)
 
    
#SelectionSort Algorithm    
def selection_sort(L):
    '''
    Take a list L, and look at the first element.  Run a comparison against the
    rest of the list, until you find a number smaller. Swap the two objects, 
    and then down the list comparing to the new 'first' element.  Repeat the 
    swap as needed until you reach the end of the list, thus leaving the first
    element as the smallest in the list.  Now increment your counter, and check
    the second element of the list against the rest, repeating the same pattern.
    '''
    suffixSt = 0
    while suffixSt != len(L):
        for i in range(suffixSt,len(L)):
            if L[i] < L[suffixSt]:
                L[suffixSt], L[i] = L[i], L[suffixSt]
            suffixSt += 1


#BubbleSort Algorithm            
def bubble_sort(L):
    '''
    Take a list L, and check the first pair of numbers, swap if out of order.
    Then check elements 2 and 3, then check 3 and 4, 4 and 5, so on and so on.
    Once through the loop, run through the sort again, until all numbers
    are in order (if statment will be false, thus not switching swap to True)
    '''
    swap = False
    while not swap:
        swap = True
        for j in range(1,len(L)):
            if L[j-1] > L[j]:
                swap = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp
    
    
#MonkeySort Algorithm
def monkey_sort(L):
    '''
    Given a list L, randomly shuffle the list.  Is it sorted? No? Try again.
    Assume is_sorted function is a linear check down the list.
    '''
    while not is_sorted(L):
        random.shuffle(L)