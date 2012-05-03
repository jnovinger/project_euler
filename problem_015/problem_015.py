#!/usr/bin/env python
"""
Project Euler - Problem #15
Starting in the top left corner of a 2x2 grid, there are 6 routes (without
backtracking) to the bottom right corner.

How many routes are there through a 20x20 grid?
"""
import sys


def populate_world(width=1, height=1):
    """
    Populates the grid of vertices with the number of possible paths to
    the bottom right and returns the annotated grid.
    """
    width += 1  # we're really talking about corners, not blocks
    height += 1  # same
    world = {}

    for x in reversed(range(width)):
        for y in reversed(range(height)):
            # note: uses negative indexing for y-coord to better map to problem

            # special case for end vertex
            if x == width - 1 and y == height - 1:
                world[(x, -y)] = 1
                continue

            paths = 0
            # if we're not max width, we can move one to right
            if y < height - 1:
                paths += world[(x, -(y + 1))]

            # if we're not max height (depth), we can move down one
            if x < width - 1:
                paths += world[(x + 1, -y)]

            world[(x, -y)] = paths

    return world

if __name__ == "__main__":

    # check for cli args, width first
    if len(sys.argv) > 2:
        width = int(sys.argv[1])
        height = int(sys.argv[2])
    else:
        print >> sys.stderr, "Useage: python problem_015.py 10 10 # to run with a 10x10 grid\n"
        print "Running with the default 20x20 grid.\n"
        width = height = 20
    world = populate_world(width, height)

    # print the result
    print "There %s %d path%s through a %sx%s grid." % ('are' if world[(0, 0)] != 1 else 'is',
        world[(0, 0)], 's' if world[(0, 0)] != 1 else '', width, height)
