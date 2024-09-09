# Define two pointers in an array (left and right)
# Traverse the list from both the sides
# Check if a list is a palindrome or not




def two_ptr_ops(arr) -> bool:# type: ignore
    l ,r = 0 , len(arr)-1
    while l < r:
         if arr[l] != arr[r]:
              return False
         l+=1
         r-=1
    
    return True


arr = [1,2,3,3,1]
print(two_ptr_ops(arr))
 