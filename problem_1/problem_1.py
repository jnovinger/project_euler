#!/usr/bin/python

''' Project Euler Problem 1'''
from math import floor

if __name__ == '__main__':
    sum = 0
    target = 999999

    sum3 = 0
    sum5 = 0
    sum15 = 0

    index3 = int(floor(target / 3))
    index5 = int(floor(target / 5))
    index15 = int(floor(target / 15))

    sum3 = 0
    sum5 = 0
    sum15 = 0

    for number in xrange(index3):
        sum3 += number + 1

    for number in xrange(index5):
        sum5 += number + 1

    for number in xrange(index15):
        sum15 += number + 1

    sum = 3 * sum3 + 5 * sum5 - 15 * sum15

    print sum
