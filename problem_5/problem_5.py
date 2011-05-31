#!/usr/bin/python

'''
 Project Euler Problem 5
'''

number = 1
target = 20
found_number = False

while not found_number:
    number += 1
#    print "Number", number, "Target", target

    for divisor in xrange(2, target + 1):
        if number % divisor == 0 and divisor == target:
#            print "Divisor:", divisor
            found_number = True
            break
        if number % divisor == 0:
#            print "Divisor:", divisor
            continue
        else:
            break

print number