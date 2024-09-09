s = 'interview'
to_find = 'e'

print(to_find in s)
i = 0 
for ch in s:
    if ch == to_find:
        print(i)  
    else:
        i+=1
l = [i ]