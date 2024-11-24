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
######Classic Examples####

# Q: Find the length of the longest subarray with the same value in each position.


def longest_subarray(arr):
    L = 0
    length = 0
    for R in range(len(arr)):
        if arr[L] != arr[R]:
            L =R
        length = max(length, R-L+1) # rem here we are adding 1 since L starts at 0
    return length 

arr = [4,2,2,3,3,3]

# print(f"Longest Subarray : {longest_subarray(arr)}")

# -> Variation in the above code without using L or R pointers

def longest_subarray_wo_LR(arr):
    length = 0
    for i in range(len(arr)):
        if i == len(arr):
            break
        if arr[i] != arr[i+1]:
            length =1
        else:
            length+=1
    return length 

arr = [4,2,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,4]

print(f"Longest Subarray : {longest_subarray(arr)}")


# Q: Find the minimum length subarray, where the sum is greater than or equal to the target. Assume all values are positive.

"""
1. First we need to ensure our window has a sum greater than or equal to the target. We do this by expanding our window from the right.
2. Next we need to minimize the size of our window. We do this by shrinking our window from the left.


Time Complexity
Even though we have nested loops, the time complexity of this approach is O(n)

The inner loop won't necessarily run n times at every iteration. In fact, it may not run at all in some iterations when target sum >>> elements of the lists. This is what is referred to as amortized analysis. The total number of iterations of the inner loop is n, same as the outer loop.

Thus, both pointers move at most n times, making the time complexity O(n).
"""