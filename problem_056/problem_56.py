#!/usr/bin/python

'''
Project Euler Problem 56

A googol (10^100) is a massive number: one followed by one-hundred zeros; 100^100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?
'''

max_int = 100

max_digital_sum = 0


def make_digits(number):
    digits = []
    while number:
        digit = number % 10
        digits.append(digit)
        number /= 10
    return digits

def digital_sum(number):
    digits = make_digits(number)
    sum = 0
    for digit in digits:
        sum += digit
    return sum

for a in xrange(1, max_int + 1):
    for b in xrange(1, max_int + 1):
        tmp_digital_sum = digital_sum(a ** b)
        if tmp_digital_sum > max_digital_sum:
            max_digital_sum = tmp_digital_sum

print max_digital_sum