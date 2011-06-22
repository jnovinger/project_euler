#!/usr/bin/python

'''
Project Euler Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
'''

from math import sqrt

def isPrime(number, primes):
    limit = int(sqrt(number))
    for prime in primes:
        if prime > limit:
            return True
        if number % prime == 0:
            return False
    return True

upper_limit = 10001

primes = [2,3,5,7,11,13]
number = 15

while len(primes) < upper_limit:
    if isPrime(number, primes):
        primes.append(number)
    number += 2

print primes[-1]