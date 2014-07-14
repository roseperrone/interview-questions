'''
Implement a hashtable.
'''

import unittest

class KeyValue(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashTable(object):
    def __init__(self, size):
        self.size = size
        self.list = []
        for i in range(self.size):
            self.list.append([])

    def get(self, key):
        arr = self.list[self.hash(key)]
        for elem in arr: 
            if elem.key == key:
                return elem.value 

    def set(self, key, value):
        arr = self.list[self.hash(key)]
        for elem in arr: 
            if elem.key == key:
                elem.value = value 
                return
        self.list[self.hash(key)].append(KeyValue(key, value)) 

    def hash(self, key):
        total = 0
        for ch in key:
            total += ord(ch)
        return total % (self.size - 1)


h = HashTable(10)
h.set('rose perrone', '503.367.1845')
h.set('ed sheeran', '1')
h.get('rose perrone') 
h.get('harry potter')

ROSE = '503.367.1845'
ED = '332.121.9872'

class TestHashTable(unittest.TestCase):
    def testIt(self):
        h.set('rose perrone', ROSE)
        h.set('ed sheeran', ED)
        self.assertEqual(h.get('rose perrone'), ROSE) 
        self.assertEqual(h.get('ed sheeran'), ED) 
