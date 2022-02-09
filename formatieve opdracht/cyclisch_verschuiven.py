def shift_bits(ch, n):
    """
    takes a string with bits (ch) and a number (n) as input. shifts the characters in the string according to n. If
    n > 0 the shift is to the left, if n < 0 the shift is to the right. The lost bits are appended to the other side.
    returns the shifted string.
    args:
        :param ch: (str) string consisting of only 0's and 1's
        :param n: (int) shift value
    returns:
        :return: shifted copy of ch
    """
    if n == 0:
        return ch
    if n < 0:
        return shift_bits(ch[-1] + ch[:-1], n + 1)
    # n > 0
    return shift_bits(ch[1:] + ch[0], n - 1)


for i in range(-4, 4):
    print(shift_bits('1011000', i))
