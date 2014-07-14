'''
Find all alphabetical combinations that could represent a 
phone number. For the numbers 0 and 1, don't replace them with
their alphabetical equivalent.
'''

def get_char_key(num): 
   result = ['0', '1', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PRS', 'TUV', 'WXY']
   return result[num]

def all_alpha(nums):
    if len(nums) == 0:
        return set()

    retval = set()
    all_endings = all_alpha(nums[1:])
    for char in get_char_key(int(nums[0])):
        if len(all_endings) == 0:
           retval.add(char) 
        for ending in all_endings:
            retval.add(char + ending)
    return retval

print str(all_alpha('5033671845'))
