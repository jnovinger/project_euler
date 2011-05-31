#!/usr/bin/python

'''
 Project Euler Problem 5

 Answer: 232792560
'''

number = 0
target = 20
found_number = False

while not found_number:
    number += target
#    print "Number", number, "Target", target

    for divisor in xrange(target, 1, -1):
        if number % divisor == 0 and divisor == 2:
#            print "Divisor:", divisor
            found_number = True
            break
        if number % divisor == 0:
#            print "Divisor:", divisor
            continue
        else:
            break

print "Answer", number