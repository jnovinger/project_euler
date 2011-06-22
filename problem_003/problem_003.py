#!/usr/bin/python

'''
Project Euler Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

def factorize(number):
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

print factorize(600851475143)