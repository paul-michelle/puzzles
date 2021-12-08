"""Reverse a number.

Given a number, write a function to output its reverse digits. (e.g. given 123 the answer is 321)
Numbers should preserve their sign; i.e. a negative number should still be negative when reversed.

Imagine you can work with integers only.

123 ->  321
-456 -> -654
1000 ->    1
"""


def reverse_digits(num: int) -> int:
    if num == 0:
        return num
    sign, num = (+1, +num) if num > 0 else (-1, -num)
    num_rev = 0
    while num:
        last_digit = num % 10
        num_rev = num_rev*10 + last_digit
        num = num // 10

    return sign * num_rev


def reverse_digits_rec(num: int) -> int:
    if num == 0:
        return num
    if num < 0:
        return -reverse_digits_rec(-num)
    num_rev = 0
    while num:
        last_digit = num % 10
        num_rev = num_rev * 10 + last_digit
        num = num // 10
    return num_rev


def reverse_digits_str_rec(num: int) -> int:
    if num < 0:
        return -reverse_digits_str_rec(-num)
    return int(str(num)[::-1])
