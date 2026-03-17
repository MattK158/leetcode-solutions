def hammingWeight(n):
    count = 0
    while n:
        count += n & 1    # is last bit a 1?
        n >>= 1           # shift right
    return count

# Why n & (n-1) works:
# n   = ...1 0 1 1 0 0  (some number)
# n-1 = ...1 0 1 0 1 1  (borrows from lowest 1-bit)
# AND = ...1 0 1 0 0 0  (lowest 1-bit is cleared)