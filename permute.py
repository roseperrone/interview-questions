'''
Find all permutations of a string.

Input:
  'hat'
Output:
  set(['tha', 'aht', 'tah', 'hta', 'hat', 'ath'])
'''

def permute(string):
    if len(string) == 1:
        return [string]
    perms = []
    for i in range(len(string)):
        endings = permute(string[:i] + string[(i+1):])
        for ending in endings:
            perms.append(string[i] + ending)
    return perms


print str(permute('hat'))
assert len(set(permute('hat')).intersection(set(['tha', 'aht', 'tah', 'hta', 'hat', 'ath']))) == 6
