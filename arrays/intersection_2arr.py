a= [4,2,2,3,1]
b = [2,2,2,3,3]
a= [6, 2, 4]
b = [1, 5, 3, 7]
#The order of elements in the output list does not matter.
#The frequency of any number in the intersection must be equal to the minimum 
#of the frequency of that number in both the given lists.

a_dict = {}
b_dict = {}
result = []
for i in a:
    a_dict[i] = a_dict.get(i,0) +1
for j in b:
    b_dict[j] = b_dict.get(j,0) +1

for val in b_dict:
    if val in a_dict:
        min_val = min(a_dict.get(val), b_dict.get(val))
        result.extend([val]*min_val)

print(result)

