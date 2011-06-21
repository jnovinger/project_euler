#!/usr/bin/python

'''
Project Euler Problem 52

It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
'''

def make_digits(number):
    digits = []
    while number:
        digit = number % 10
        digits.append(digit)
        number /= 10
    digits.sort()
    return digits

found = False
number = 0
highest_multiple = 6

while not found:
    number += 1
    orig_digits = make_digits(number)

    for index in xrange(2, highest_multiple + 1):
        if orig_digits != make_digits(index * number):
            break
        if index == highest_multiple:
            found = True

print number