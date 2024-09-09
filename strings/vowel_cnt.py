s = "whhgbmnrpyroojdvjzhhrfcaubhjjtoqetiwfaqsouhvmseazwdgewfnz"


def countVowels(s):
    count = {}
    for ch in s:
       if ch in 'aeiou':
            count[ch]=count.get(ch, 0)+1
    
    print(count)
    
    for val in count.values():
        return val
    

#print(countVowels(s))

# O(n)
def distinctCountVowels(s):
    count = {}
    key_cnt = 0
    for ch in s:
       if ch in 'aeiou':
            count[ch]=count.get(ch, 0)+1
    
    for key in count.keys():
        key_cnt +=1

    print(key_cnt)
    
    
#print(countVowels(s))
distinctCountVowels(s)
#print(distinctCountVowels(s))

# O(1) -- using set
def distinctCountVowelsSet(s):
    count = set()
    for ch in s:
       if ch in 'aeiou':
            count.add(ch)
    
    print(len(count))

distinctCountVowelsSet(s)