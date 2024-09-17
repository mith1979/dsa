"""
Selection sort algorithm

"""
# def swap(arr, p1, p2):
#     arr[p1] , arr[p2] = arr[p2] , arr[p1]
#     return arr
# def find_min(arr):
#     L = 0 
#     for L in range(len(arr)):
#         if arr[L] < arr[L+1]:
#             arr[L] , arr[L+1] = arr[L+1], arr[L]

def selection_sort(arr):
    
    for i in range(0, len(arr)):
        minvalue = arr[i]
        minindex = i 
        for j in range(i+1,len(arr)):
            if arr[j] < minvalue:
                minvalue = arr[j]
                minindex = j
        arr[i] , arr[minindex] = arr[minindex], arr[i] 
    
    print(arr)

arr = [4,3,2,1] 
selection_sort(arr)
