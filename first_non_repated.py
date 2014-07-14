'''
Find the first non-repeated character in a string.

Input:
    'rose perrone'
Output:
    s
'''

from collections import OrderedDict 

def find_first_non_repeated_char(string):
    d =  OrderedDict()
    for char in string:
        if char in d:
            d[char] += 1
        else:
            d[char] = 1
    while len(d) > 0:
        char, count = d.popitem(last=False)
        if count == 1:
            return char
    return None

print(find_first_non_repeated_char('rose perrone'))
