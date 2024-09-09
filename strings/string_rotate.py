"""Input : s = "GeeksforGeeks"
        d = 2
Output : Left Rotation  : "eksforGeeksGe" 
         Right Rotation : "ksGeeksforGee"  
"""

# Naive Approach - String Slicing
# https://www.geeksforgeeks.org/left-rotation-right-rotation-string-2/
# Left Rotation

def left_rotate(s,d):
    len_str = len(s)
    tmp_str = s[d:len_str] + s[0:d]
    print(tmp_str)
    print(s)

def right_rotate(s,d):
    len_str = len(s)
    tmp_str = s[-d:len_str] + s[0:len_str-d]
    # tmp_str = s[d:len_str] + s[0:d]
    print(tmp_str)
    print(s)
s = "GeeksforGeeks"
d =3
# left_rotate(s, d)
right_rotate(s, d)

# IF two strings are rotation of each other
s1 = "ABAB"
s2 = "ABBA"

def isRotation(s1,s2):
    if len(s1)!= len(s2):
        return False
    tmp = ''
    tmp = s1 + s1
    return tmp.find(s2) != -1

print(isRotation(s1,s2))