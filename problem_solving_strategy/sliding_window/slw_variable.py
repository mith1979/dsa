##### Sliding Window (Variable Size)##
"""
Another variation of the sliding window technique is the variable size sliding window. This is useful when we don't have a fixed window size and we need to keep expanding our window as long as our window meets a certain constraint.

"""
##### Steps to implement simple slinding window (varible size) alogorithm ####

"""
We can make use of two pointers, L and R. Our constraint is that we cannot have multiple distinct values in our window. We need to find the longest subarray so we should try to maximize our window while it is valid.

1. We can start at the beginning and keep expanding our window from the right.
2. Once we encounter a new value, we stop expanding our window.
3. We then shrink our window by bringing our L pointer to our R pointer. We don't need to increment L because if we encountered a new value, it must be the case that every value before was a duplicate.
4. We then repeatedly calculate the length of our window by taking the maximum of the current length and the maximum length.
5. The length can be calculated by taking the difference between R and L and adding 1.

"""

# Q: Find the length of the longest subarray with the same value in each position.
arr = [4,2,2,3,3,3]

def longest_subarray(arr):
    L = 0
    length = 0
    for R in range(len(arr)):
        if arr[L] != arr[R]:
            L =R
        length = max(length, R-L) 