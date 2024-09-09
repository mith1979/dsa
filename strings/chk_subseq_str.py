# Check if a string is a subsequence of other 
s1 = 'geekforgeeks'
s2 = 'grges'

def check_subseq(s1,s2):
    i = 0
    j = 0
    while(i< len(s1) and j < len(s2)):
        if s2[j] == s1[i]:
            j+=1
        i+=1 
    
    if j == len(s2):
        return True
    else:
        return False
        
print(check_subseq(s1,s2))