'''
Reverse a string.

Input:
    rose
Output:
    esor
'''

def reverse_1(s):
    return s[::-1]

def reverse_2(s):
    rev = '' 
    for i in range(len(s)):
        index = len(s) - i - 1
        rev += s[index]
    return rev

print reverse_1('rose')
print reverse_2('rose')

