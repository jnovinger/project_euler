#!/usr/bin/python

'''
 Project Euler Problem 4

 Answer: 906609
'''

def is_palindrome(x):
    z = str(x)
    l = len(z) / 2
    if z[:l] == z[-l:][::-1]:
        return True
    return False


upper_limit = 999
lower_limit = 100
found = False
palindrome = 0

for x in xrange(upper_limit, lower_limit - 1, -1):
    for y in xrange(upper_limit, lower_limit - 1, -1):
        if x != y:
            num = x * y
            if num > palindrome and is_palindrome(num):
                palindrome = num

print palindrome