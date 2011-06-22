#!/usr/bin/python

'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
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

upper_limit = 2000000

primes = [2,3,5,7,11,13]
number = 15

while number < upper_limit:
    if isPrime(number, primes):
        primes.append(number)
    number += 2

print sum(primes)