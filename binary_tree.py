'''
Implement binary search.

Input:
    Find the index of 4 in [1, 4, 7, 8]
Output:
    1
'''

def binary_search(lst, lo, hi, target):
    if hi - lo <= 1:
        return lst[lo] == target or lst[hi] == target
    mid = (hi + lo)/2 
    if target < lst[mid]:
        return binary_search(lst, lo, mid, target)
    if target > lst[mid]:
        return binary_search(lst, mid, hi, target)
    return mid

print(binary_search([1, 4, 7, 8], 0, 3, 4))
print(binary_search([1, 4, 7, 8], 0, 3, 5))
