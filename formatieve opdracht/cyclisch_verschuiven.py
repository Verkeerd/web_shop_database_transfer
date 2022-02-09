def shift_bits(ch, n):
    """
    Takes a string with bits (ch) and a number (n) as input. Shifts the characters in the string according to n. If
    n > 0 the shift is to the left, if n < 0 the shift is to the right. The lost bits are appended to the other side.
    Returns the shifted string.
    """
    if n == 0:
        return ch
    if n < 0:
        return shift_bits(ch[-1] + ch[:-1], n + 1)
    # only option left is:  n > 0
    return shift_bits(ch[1:] + ch[0], n - 1)


for i in range(-4, 4):
    print(shift_bits('1011000', i))
