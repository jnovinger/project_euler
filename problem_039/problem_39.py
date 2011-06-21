#!/usr/bin/python

'''
Project Euler Problem 39

If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p  1000, is the number of solutions maximised?
'''
from math import sqrt

target = 1000

p = {}
for x in xrange(1, target):
    p[x] = 0

for a in xrange(1, target - 1):
    for b in xrange(1, target - 2):
        c = sqrt(a**2 + b**2)
        if c % 1 == 0:
            sum = a + b + c
            if sum < target:
                p[sum] += 1

highest_key = 1
highest_value = 0
for k in xrange(1, target):
    if p[k] > highest_value:
        highest_key = k
        highest_value = p[k]

print "Max Key:", highest_key, "Max Value:", highest_value
