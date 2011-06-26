#!/usr/bin/python

'''
The palindromic number 595 is interesting because it can be written as the sum of consecutive squares:
6^2 + 7^2 + 8^2 + 9^2 + 10^2 + 11^2 + 12^2.

There are exactly eleven palindromes below one-thousand that can be written as consecutive square sums, and the sum of
these palindromes is 4164. Note that 1 = 0^2 + 1^2 has not been included as this problem is concerned with the squares
of positive integers.

Find the sum of all the numbers less than 108 that are both palindromic and can be written as the sum of consecutive
squares.
'''

def is_palindrome(x):
    if x >= 0 and x < 10:
        return True
    z = str(x)
    l = len(z) / 2
    if z[:l] == z[-l:][::-1]:
        return True
    return False

limit = 10 ** 8
numbers = set()

for outer in xrange(1, limit):
    if (outer ** 2 + (outer + 1) ** 2) > limit:
        break
    indices = []
    number = 0
    for index in xrange(outer, limit):
        number += index ** 2
        indices.append(index)
        if number < limit:
            if is_palindrome(number) and len(indices) > 1:
                numbers.add(number)
        else:
            break

print sum(numbers)