#!/usr/bin/python

'''
Project Euler Problem 9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

'''
target = 1000
found = False

for c in xrange(1, target - 1):
    for b in xrange(1, target - 2):
        a = target - c - b
        if 0 < a < b < c < target and \
           a**2 + b**2 == c**2:
            found = True
            break
    if found:
        break

if found:
    print "a, b, c =", a, b, c
    print "a x b x c =", a * b * c