#!/usr/bin/python

''' Project Euler Problem 1'''

def SumDivisibleBy(n):
    p = target / n
    return n * (p * (p + 1)) / 2

if __name__ == '__main__':
    sum = 0
    target = 999

    print SumDivisibleBy(3) + SumDivisibleBy(5) - SumDivisibleBy(15)
