'''
Convert a base-10 RGB value of the form [0-255], [0-255], [0-255] to a hex string.
'''

def toHex(a,b,c):
    result = hex(a).upper()
    result += hex(b)[2:].upper()
    result += hex(c)[2:].upper()
    return result

print(toHex(255, 32, 222))