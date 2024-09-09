# Given a sorted input array, return the two indices of two elements which sums up to the target value. Assume there's exactly one solution.


def target_sum(arr, target):
    l , r = 0 , len(arr)-1
    while l < r :
        if arr[l] + arr[r] > target:
            r -= 1
        elif arr[l] + arr[r] < target:
            l += 1
        else:
            return [l,r]

arr = [-1,2,3,5,7,9]
print(target_sum(arr, 7))