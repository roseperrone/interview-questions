'''
Sum integers in a file.

Input:
  filename
Output:
  a number
'''

def sum_file(filename):
    with open(filename) as f:
        total = 0
        line = f.readline()
        try: 
            total += int(line)
        except ValueError as e:
            print str(e)
        return total

print int(sum_file('/Users/rose/Desktop/ints.txt'))
