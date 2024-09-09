#Find the majority element in a given list. For a list of size n, the majority element is the element that appears more than floor(n/2) times.

# {
# "nums": [3, 3, 3, 2, 2, 2, 3]
# }
# 3
# 3 occurs 4 times which is greater than ⌊7/2⌋ = 3 times
from math import floor
# Time complexity : O(n)
# Soace complexity : O()

def majority_element(nums):
    """
    Args:
     nums(list_int32)
    Returns:
     int32
    """
    # Write your code here.
    count = {}
    l = len(nums)
    fl = floor(l/2)
    for ele in nums:
        count[ele] = count.get(ele, 0) + 1
    
    if count.get(max(count,key=count.get)) > fl:
        return max(count,key=count.get)
    return 0

lst = [3, 3, 3, 2, 2, 2, 3]
print(majority_element(lst))