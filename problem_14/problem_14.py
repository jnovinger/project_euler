#!/usr/bin/python

'''
The following iterative sequence is defined for the set of positive integers:

n -> n/2 (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

numbers = [0]

limit = 1000000

def chain(number):
    chain = [number]
    while number != 1:
        if (number % 2 == 0):
            number = number / 2
            chain.append(number)
        else:
            number = 3 * number + 1
    return chain

longest_chain = 1
longest_chain_index = 1
for number in xrange(1, limit):
    new_chain = chain(number)
    if len(new_chain) > longest_chain:
        longest_chain = len(new_chain)
        longest_chain_index = number
    numbers.append(new_chain)


print longest_chain, longest_chain_index
print numbers[longest_chain_index]