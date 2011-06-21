#!/usr/bin/python

'''
 Project Euler Problem 2

This version relies on the fact that:

next_even_fib = 4 * fib_(-2) + fib_(-1)
'''

limit = 3999999

# unroll first two loop iterations
a = 2
b = 8
c = 4 * b + a # 34

sum  = a + b

while c < limit:
    sum += c

    a = b
    b = c
    c = 4 * b + a

print sum