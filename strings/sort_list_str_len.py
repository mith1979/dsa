# Input : list = ["rohan", "amy", "sapna", "muhammad",
#                 "aakash", "raunak", "chinmoy"]
# Output : ['amy', 'rohan', 'sapna', 'aakash', 'raunak', 
#          'chinmoy', 'muhammad']

# Input : list = [["ram", "mohan", "aman"], ["gaurav"], 
#                  ["amy", "sima", "ankita", "rinku"]]
# Output : [['gaurav'], ['ram', 'mohan', 'aman'], 
#           ['amy', 'sima', 'ankita', 'rinku']]

# Write a Python program to sort a list of strings based on the length of each string. Define a custom sort function that takes a list of strings and returns a sorted list.
# Approach:
# 1. Using the build in sort method in a list to do a inplace 

# Time Complexity: O(n log n)
# Auxiliary Space: O(1)
s = ["rohan", "amy", "sapna", "muhammad","aakash", "raunak", "chinmoy"]
t=  [["ram", "mohan", "aman"], ["gaurav"], ["amy", "sima", "ankita", "rinku"]]

def sort_list(l) -> list:
    l.sort(key=len)
    print(l)
    return l

sort_list(s)
sort_list(t)

