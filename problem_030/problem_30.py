#!/usr/bin/python

'''
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

    1634 = 14 + 64 + 34 + 44
    8208 = 84 + 24 + 04 + 84
    9474 = 94 + 44 + 74 + 44

As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
'''


number = 1
sum = 0
digits = 1
limit = digits * (9 ** 5)

while number < limit + 1:
    length = len(str(number))
    if length > digits:
        digits = length
        limit = digits * (9 ** 5)
    number += 1
    sum_of_digits = 0
    for digit in str(number):
        sum_of_digits += int(digit)**5
    if number == sum_of_digits:
        sum += number

print sum