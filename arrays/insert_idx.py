arr = [10,20,30,50]
l = 0 
r = len(arr)
for j in range(r):
    print(arr[j])

print(f"List in reverses")
for i in range(r-1,-1 , -1):
    print(arr[i])


def insert_element_at_position(nums, element, position):
    """
    Args:
     nums(list_int32)
     element(int32)
     position(int32)
    Returns:
     list_int32
    """
    # Write your code here.
    print(f"Orginal arr :{nums}")
    # if position < 0 or position > len(nums)-1:
    #     print("Invalid index")
    #     return
    
    # nums.append(0)
    
    r = len(nums)-1
    for i in range(r, position-1 , -1):
        nums[i]= nums[i-1] 
        # print(i)
    

    nums[position-1] = element

    print(f"Coverted arr :{nums}")

insert_element_at_position(arr,40,1)
arr2 = [2, 4, 5, 6, -1]
insert_element_at_position(arr2,3,2)
arr3 = [70, 60, 50, -1]
insert_element_at_position(arr3,40,4)