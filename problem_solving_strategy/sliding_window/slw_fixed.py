"""
Note: The idea behind having a fixed sliding window is to maintain two pointers that are k apart from each other and fit a certain constraint.

Problem Statement: Q: Given an array, return true if there are two elements within a window of size k that are equal.

"""

# Brute force approach
def slw_fixed_brute_force(arr, k):
    for L in range(len(arr)):
        for R in range (L+1, min(len(arr), L+k)):
            if arr[L] == arr[R]:
                return True
    return False


# Linear complexity approach
"""
Hash sets allow us to store unique elements and have an 
O(1) lookup, removal and add complexity. If we needed more than just two occurrences, we could use a hash map to store the count of each element, but in this case a set is sufficient.

We can use a set to store elements currently in our window. When our set's size goes beyond k, we can remove elements shift the left pointer and remove the element that is no longer in our window.

Since we are adding from the right, if we encounter a number that has already been added, we can return true. Our set's size should never exceed k.


"""
def slw_fixed_linear_time(arr, k):
    window = set()
    L = 0 
    for R in range(len(arr)):
        # breakpoint()
        if R-L+1> k:
            window.remove(arr[L])
            L +=1

        if arr[R] in window:
            return True 

        window.add(arr[R])
    return False

# Test

arr = [1,2,3,4,5,6,7,1]
print(slw_fixed_brute_force(arr, 2))

# arr2 = [1,2,2,1]
arr2 = [1,2,3,4]
print(f"Brute Force sol : {slw_fixed_brute_force(arr2, 3)}")
print(f"linear time sol : {slw_fixed_linear_time(arr2, 2)}")