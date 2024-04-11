#!/usr/bin/python3
""" alx interview  N queens """
import sys


if len(sys.argv) > 2 or len(sys.argv) < 2:
    print("Usage: nqueens N")
    exit(1)

if not sys.argv[1].isdigit():
    print("N must be a number")
    exit(1)

if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    exit(1)

n = int(sys.argv[1])


def queens(n, i=0, x=[], y=[], z=[]):
    """ print every possible positions """
    if i < n:
        for j in range(n):
            if j not in x and i + j not in y and i - j not in z:
                yield from queens(n, i + 1, x + [j], y + [i + j], z + [i - j])
    else:
        yield x


def solve(n):
    """ solve for n """
    k = []
    i = 0
    for solution in queens(n, 0):
        for s in solution:
            k.append([i, s])
            i += 1
        print(k)
        k = []
        i = 0


solve(n)
