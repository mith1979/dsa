"""
Bubble sort algorithm
Time complexity : O(N2)
Space complexity: O(1)
"""
def bubble_sort(arr):
    n = len(arr)
    # outer loop (i) we will traverse the loop from left to right:
    for i in range(0 , n):
    # inner loop (j) will run from right to left (As per IK)
        for j in range(n-1,i,-1):
            # we will compare elements at right(i) and right-1(j):
            if arr[j] < arr[j-1]:                
    # if small at right then swap
                arr[j-1] , arr[j] = arr[j], arr[j-1]
    
    print(arr)
    return arr

arr = [4,3,2,1] 
# arr =[1,2,3,4]
print(bubble_sort(arr))