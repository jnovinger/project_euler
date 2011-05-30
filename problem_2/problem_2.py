#!/usr/bin/python

''' Project Euler Problem 2'''

limit = 3999999

fib_1 = 1
fib_2 = 2

sum = 2  # preload
while fib_1 + fib_2 < limit:
    if (fib_1 + fib_2) % 2 == 0:
        sum += fib_1 + fib_2

    # update fibs
    if fib_1 < fib_2:
        fib_1 = fib_1 + fib_2
    else:
        fib_2 = fib_1 + fib_2

print sum