# Author: Thomas Wunz
# GitHub username: wunzt
# Date: 4/19/2022
# Description: Function takes a positive integer and returns how many steps it takes to reach 1 in a hailstone sequence
# for the first time.

def hailstone(x):
    """Takes a positive integer and returns how many steps it takes to reach 1 in a hailstone sequence for the
    first time."""
    step = 0
    while int(x) > 1:
        if x % 2 == 0:
            x /= 2
        else:
            x = x * 3 + 1
        step += 1
    return step