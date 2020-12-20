# EOPL 4.1
# Computing the parity of a word
# How would you compute the parity of a very large number of 64-bit words?

# Solution 1
def parity(x):
    result = 0
    while x:
        result ^= x & 1
        x >>= 1
    return result


# Time: O(k), where k is number of bits in x.
# Space: O(1)


# Solution 2

def parity(x):
    result = 0
    while x:
        result ^= 1
        x &= x -1
    return result


# Time: O(k), where k is the number of 1 bits in number x.
# Space: O(1)


