'''
Print all combinatiosn of a string.

Input:
    'ros'
Output:
    set(['', 'rs', 'ors', 'o', 's', 'r', 'os', 'or'])
'''


def combinations(string):
    if len(string) == 1:
        return set([string, ''])
    result = set() 
    for i in range(len(string)):
        for comb in combinations(string[:i] + string[(i+1):]):
            result.add(''.join(sorted(comb)))
            result.add(''.join(sorted(comb + string[i])))
    return result

print str(combinations('ros'))