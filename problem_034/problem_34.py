#!/usr/bin/python

'''
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.

'''

from math import factorial

factorials = {}

for number in range(0,10):
    factorials[number] = factorial(number)

found = False
number = 3
numbers = []
limit = len(str(number)) * factorials[9]

while number < limit:
    total = 0
    for digit in str(number):
        total += factorials[int(digit)]
    if total == number:
        numbers.append(number)
    number += 1
    if len(str(number)) > limit:
        limit = len(str(number))

print sum(numbers)