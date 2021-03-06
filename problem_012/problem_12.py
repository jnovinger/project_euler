#!/usr/bin/python

'''
Project Euler Problem 12

The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

     1: 1
     3: 1,3
     6: 1,2,3,6
    10: 1,2,5,10
    15: 1,3,5,15
    21: 1,3,7,21
    28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?

'''

from math import sqrt

def prime_factorize(number):
    factors = [1]
    factor = 2
    while number > 1:
        while factor <= number:
            if number % factor == 0:
                factors.append(factor)
                number /= factor
            else:
                factor += 1
    return factors

def factorize(number):
    if number == 1:
        return [1]
    factors = [1, number]
    factor = 2
    while factor < number:
        if factor > sqrt(number):
            break
        if number % factor == 0:
            factors.append(factor)
            factors.append(number / factor)
        factor += 1
    factors.sort()
    return factors

number = 1
triangle = 0
high_factors = 0
length = 0

while length <= 500:
    triangle += number
    number += 1
    factors = factorize(triangle)
    length = len(factors)
    if length > high_factors:
        high_factors = length
        print "Triangle:", triangle, "Number:", number, "Factors:", length, factors
