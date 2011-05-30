#!/usr/bin/python

''' Project Euler Problem 2'''

limit = 3999999

fibs = []

fibs.append(1)
fibs.append(2)

fib_1_index = 0
fib_2_index = 1

while fibs[fib_1_index] + fibs[fib_2_index] < limit:
    fibs.append(fibs[fib_1_index] + fibs[fib_2_index])
    fib_1_index += 1
    fib_2_index += 1

sum = 0
for fib in fibs:
    if (fib % 2 == 0):
        sum += fib

print sum