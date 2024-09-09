def check_if_array_contains_duplicate(nums):
    """
    Args:
     nums(list_int32)
    Returns:
     bool
    """
    # Write your code here.
    dup = 0 
    i = 0 
    j = len(nums) -1
    for i in range(len(nums)):
        while j > i:
            if nums[i] == nums[j]:
                dup +=1
            j-=1
            if dup:
                return True
        j = len(nums) -1
    return False

lst = [10, 30, 10, 20]
lst2 = [5, 10, 15, 20]
lst3 =  [250, 290, 230, 290, 245, 220, 263, 278]
print(check_if_array_contains_duplicate(lst))
print(check_if_array_contains_duplicate(lst2))
print(check_if_array_contains_duplicate(lst3))

# """
# Given a list of numbers in which each number appears exactly twice except one number that appears only once. Find the number that appears exactly once.
# (Try solving this in linear time complexity without using any extra space!)

# The best solution is to use XOR. XOR of all array elements gives us the number with a single occurrence. The idea is based on the following two facts. 
# XOR of a number with itself is 0. 
# XOR of a number with 0 is number itself.

# """
# lst4 = [2, 1, 2, 1]
# lst5 =[2, 3, 5, 4, 5, 3, 4]
# def single_number(arr):
#     """
#     Args:
#      arr(list_int32)
#     Returns:
#      int32
#     """
#     # Write your code here.
#     s_num = arr[0]
#     for i in range(1 ,len(arr)):
#         s_num = s_num^arr[i]
#     if s_num:    
#         # print(s_num)
#         return s_num
#     return 0
# print(single_number(lst4))
# print(single_number(lst5))


# # Removing duplicate elements from an array 
# # Here we have added an additional space
# nums = [0,0,1,1,1,2,2,3,3]
# nums1 = [0,0,1,1,1,2,2,3,3,4]
# """
# # Inplace assignment (Leetcode =26) create an list without duplicate elements using inplace assigment. Assumption the list given in ascending order.
    
#     # Steps : two pointer method to have linear complexity and without in-place assignments.. brute-force method
#     1.  l ptr will be used to keep track of the original elements positions
#     2.  r ptr will be used to keep track of the unique elements    
#     3.  Start with the setting l and r ptr to 2nd element 
#     4.  check if curr and prev elements are the same; if yes then incr r ptr (imp steps)
#     5.  else if curr and prev elements are not same ; then assign unique element at r   position to l position;and incr l and r ptr both.

#     # Complexity
#     time : O(n)
#     space : O(1)

# """
# def removeDuplicates(nums) :
#         expected_nums = []
#         r = 1
#         dup = 0
#         expected_nums.append(nums[0])
#         for i in range(len(nums)-1):
#             if nums[i] != nums[r]:
#                 expected_nums.append(nums[r])
#                 dup = 0 
#             else:
#                 dup +=1
#             r +=1
        
#         # This is the case if all the elements in array are equal
#         if dup and nums[0] != nums[i]:
#             expected_nums.append(nums[i])    

#         expected_nums.append('_')
#         print(expected_nums)
#         return  len(expected_nums)-1

# # print(removeDuplicates(nums1))
# """
# # Inplace assignment (Leetcode =26) create an list without duplicate elements using inplace assigment. Assumption the list given in ascending order.
    
#     # Steps : two pointer method to have linear complexity and in-place assignments
#     1.  l ptr will be used to keep track of the original elements positions
#     2.  r ptr will be used to keep track of the unique elements    
#     3.  Start with the setting l and r ptr to 2nd element 
#     4.  check if curr and prev elements are the same; if yes then incr r ptr (imp steps)
#     5.  else if curr and prev elements are not same ; then assign unique element at r   position to l position;and incr l and r ptr both.

#     # Complexity
#     time : O(n)
#     space : O(1)


# """

# def inplace_remove_dup(nums):
#     l ,r = 1,1
#     while r >= l and r <= len(nums)-1 :
#         if nums[r-1] == nums[r]:
#             r +=1
#         elif nums[r-1] < nums[r]:
#             nums[l] = nums[r]
#             l +=1
#             r +=1
    
#     # print(f"{nums[:l]} and l : {l}  r : {r}")

# # Can you rewrite using for loop (HW)
# def inplace_remove_dup_ver2(nums):
#     pass    
#     # print(f"{nums[:l]} and l : {l}  r : {r}")

# print(inplace_remove_dup(nums))

# """
# Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

# Input: nums = [1,1,1,2,2,3]
# Output: 5, nums = [1,1,2,2,3,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
# Example 2:

# Input: nums = [0,0,1,1,1,1,2,3,3]
# Output: 7, nums = [0,0,1,1,2,3,3,_,_]
# Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).


# """
# nums=[1,1,1,2,2,3]
# def inplace_rem_dup_II(nums):
#     l = 0
#     c = 0
#     for r in range(1, len(nums)):
#         if nums[l] == nums[r] and c < 2:
#             l += 1
#             c += 1
#         elif nums[l] != nums[r]:
#             nums[l] = nums[r]
#             r+=1
#             c = 0
#         else: 
#             c = 0
    
#     print(f"{nums[:l]} and l : {l}  r : {r}")

# print(inplace_rem_dup_II(nums))

