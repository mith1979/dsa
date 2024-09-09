# Find the index of the first occurance in a string

haystack = "sadbutsad"
needle = "sad"

haystack = "leetcode"
needle = "leeto"

index = []

if needle in haystack:
# Alternatively we can have 
#if len(haystack) < len(needle): return -1
    # This is the sliding window method to traverse a string
    for i in range(len(haystack)- len(needle)+1):

        substring = haystack[i:i+len(needle)]
        if substring == needle:
            index.append(i)
else:
    # return -1 
    print("Needle is not in the haystack")
    # return -1
# return index[0] -- for first occurance  
print(index)
    

