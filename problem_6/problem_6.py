#!/usr/bin/python

'''
 Project Euler Problem 6
'''

limit = 100

sum_of_squares = 0

sum = 0

for number in xrange(1, limit + 1):
    sum_of_squares += number ** 2
    sum += number

square_of_sum = sum ** 2

print square_of_sum - sum_of_squares