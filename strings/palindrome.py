s = 'ABGBA'
t = 'ABCCBA'
u= 'ABZAB'
v= 'a'
w ='abA'
def checkPalindrome(s):
    lptr = 0
    rptr = len(s)-1
    while lptr < rptr:
        if s[lptr] == s[rptr]:
            print(f"left:{s[lptr]} right:{s[rptr]}")
            lptr +=1
            rptr -= 1
        else:
            return False

    return True    

# print(checkPalindrome(s))
# print(checkPalindrome(t))
# print(checkPalindrome(u))
# print(checkPalindrome(v))
# print(checkPalindrome(w))

print(checkPalindrome(s))
print(checkPalindrome(t))
h = "A man, a plan, a canal: Panama"
# def clean_str(s:str) -> str:
#     return s.lower().replace(" ", "").replace(":","").replace(",","")

# print(clean_str(h))

# Time Complexity : O(n)
def alph_chk_palindrome(s):
    l , r = 0 , len(s)-1
    while l < r:
        if not s[l].isalnum():
            l +=1
        elif not s[r].isalnum():
            r -= 1
        elif s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True

print(alph_chk_palindrome(h))

def alph_chk_palindrome2(s):
    l , r = 0 , len(s)-1
    while l < r:
        if not s[l].isalnum():
            l +=1
        elif not s[r].isalnum():
            r -= 1
        elif s[l].lower() == s[r].lower():
            l += 1
            r -= 1
        else:
            return False
    return True

print(alph_chk_palindrome2(h))