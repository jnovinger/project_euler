#!/usr/bin/python

'''
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

'''
from math import sqrt
from time import time

def sum_proper_divisors(number):
    if number == 0 or number == 1:
        return number
    factor = 2
    total = 1
    while factor <= sqrt(number):
        if number % factor == 0:
            other_factor = number / factor
            if other_factor != factor:
                total += other_factor + factor
            else:
                total += factor
        factor += 1
    return total

number = 3
total = 0
upper_limit = 28123

begin = time()
print "Calculating abundant numbers below %d." % upper_limit
abundant_numbers = []
while number <= upper_limit:
    if sum_proper_divisors(number) > number:
        abundant_numbers.append(number)
    number += 1
print "Done in %f seconds." % (time() - begin)

begin = time()
print "Calculating numbers that can be expressed as the sum of two abundant numbers."
non_candidates = set()
for x in abundant_numbers:
    for y in abundant_numbers:
        temp = x + y
        if temp <= upper_limit:
            non_candidates.add(temp)
    abundant_numbers = abundant_numbers[1:]
print "Done in %f seconds." % (time() - begin)

begin = time()
print "Summing up numbers not expressable as the sum of two abundant numbers."
for x in xrange(1, upper_limit + 1):
    if x not in non_candidates:
        total += x
print "Done in %f seconds." % (time() - begin)

print total