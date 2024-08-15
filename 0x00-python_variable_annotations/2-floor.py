#!/usr/bin/env python3
"""
Returns the floor of any float its given
"""


def floor(n: float) -> int:
    floored = 0
    for i in range(int(n)):
        floored = i
    return i + 1

if __name__ == '__main__':
    print(floor(3.54))
    print(floor(4.333))
    print(floor(5.322))
    print(floor(35.33))
