#!/usr/bin/python

'''
Project Euler Problem 48

The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

'''

target = 1000
sum = 0

for number in xrange(1, target + 1):
    sum += number ** number

print str(sum)[-10:]