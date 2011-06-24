#!/usr/bin/python

'''
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 x 7
15 = 3 x 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2^2 x 7 x 23
645 = 3 x 5 x 43
646 = 2 x 17 x 19.

Find the first four consecutive integers to have four distinct primes factors. What is the first of these numbers?
'''

def prime_factorize(number):
    factors = []
    factor = 2
    while number > 1:
        while factor <= number:
            if number % factor == 0:
                factors.append(factor)
                number /= factor
            else:
                factor += 1
    return factors

length = 4
found = False
number = 1
streak = []

while not found:

    factors = list(set(prime_factorize(number)))
    if len(factors) == length:
        streak.append(number)
    else:
        streak = []
    number += 1

    if len(streak) == length:
        found = True

print streak