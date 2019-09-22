# -*- coding: utf-8 -*-

        
def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """
#    partitions = get_partitions(L)
    partitions = []
    for i in range(len(L)):
        for j in range(1, len(L)-i+1):
            partitions.append(L[i:i+j])
    maxVal = sum(partitions[0])
    for chunk in partitions:
        maxTemp = sum(chunk)
        if maxVal < maxTemp:
            maxVal = maxTemp
    return maxVal
    
"""
in the list [3, 4, -1, 5, -4], the maximum sum is 3+4-1+5 = 11
in the list [3, 4, -8, 15, -1, 2], the maximum sum is 15-1+2 = 16
"""
numList = [3, 4, -1, 5, -4]
ans = 11
print(max_contig_sum(numList))
print("Should be: " + str(ans))


numList = [3, 4, -8, 15, -1, 2]
ans = 16
print(max_contig_sum(numList))
print("Should be: " + str(ans))

numList = [-4, -5, 1]
ans = 1
print(max_contig_sum(numList))
print("Should be: " + str(ans))

numList = [1]
ans = 1
print(max_contig_sum(numList))
print("Should be: " + str(ans))