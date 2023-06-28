#!/usr/bin/env python3
"""This is a confused Iteration."""
def confIteration(n):
    result = 0
    i = 1
    while n != 0:
        remainder = n % 2
        n = n // 2
        result = result + (remainder * i)
        i = i * 10
    return result
print(confIteration(25))

