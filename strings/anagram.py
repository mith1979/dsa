s1 = 'listen'
s2 = 'silent'
s3='geeksforgeeks'
s4='forgeeksgeeks'
s5='aabaa'
s6='baaaaa'
# Time Complexity: O(n), where n is the size of string
# Space Complexity: O(c) (where c is constant), because we are using a list of constant size

# def anagram(s1,s2):
#     s1_d = {}
#     s2_d = {}

#     for i in s1:
#         s1_d[i] = s1_d.get(i,0)+1

#     for j in s2:
#         s2_d[j] = s2_d.get(j,0)+1
    
#     if s1_d == s2_d:
#         print("Both strings are Anagram")
#     else:
#         print("Both strings are not Anagram")

def isAnagram(a,b):
    s1_d = {}
    for i in a:
        s1_d[i] = s1_d.get(i,0)+1

    for j in b:
        if s1_d.get(j):
            s1_d[j] -= 1
        else:
            return False
    
    for count in s1_d.values():
        if count != 0:
            return False
    return True
    
print(isAnagram(s1,s2))

print(isAnagram(s3,s4))

print(isAnagram(s5,s6))

# Alternative Approch
# Time Complexity: O(n), where n is the size of string
# Space Complexity: O(c) (where c is constant), because we are using a list of constant size
def areAnagram2(s1,s2):
    if len(s1) != len(s2):
        return False
    count=[0]*256
    for i in range(len(s1)):
        count[ord(s1[i])]+=1
        count[ord(s2[i])]-=1
    for x in count:
        if x!=0:
            return False
    return True