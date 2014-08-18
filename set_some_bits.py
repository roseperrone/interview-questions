
def set_some_bits(m, n, i, j):
  mask = 0;
  for d in range(j - i + 1):
    mask |= 1
    mask <<= 1
  for d in range(i):
    mask <<= 1
  return (~mask & n) | (mask & m)

def set_some_bits_2(m, n, i, j):
  all_ones = ~0
  left_mask = all_ones - ((1 << j) - 1)
  right_mask = (1 << i) - 1
  mask = left_mask | right_mask
  return (n & mask) | (m & ~mask)
