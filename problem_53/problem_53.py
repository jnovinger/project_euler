#!/usr/bin/python

'''
There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3 = 10.

In general,

nCr = (n!)/r!(n-r)!,where r <= n, n! = nx(n-1)x...x3x2x1, and 0! = 1.

It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

How many, not necessarily distinct, values of  nCr, for 1 <= n <= 100, are greater than one-million?
'''

def factorial(number):
    if number == 1 or number == 0:
        return 1
    else:
        return number * factorial(number - 1)

def C(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))

n_limit = 100
cent_count = 0

for n in xrange(2, n_limit + 1):
    for r in xrange(1, n + 1):
#        print "n:", n, "r:", r, "C(n,r)", C(n,r)
        if C(n,r) > 1000000:
            cent_count += 1

print cent_count