from collections import deque 
import re

__operators__ = "+-/*"
__paranthesis__ = "()"
__priority__ = {
    '+': 0,
    '-': 0,
    '*': 1,
    '/': 1,
}

def test(operator1,operator2):
    return __priority__[operator1] >= __priority__[operator2]

print(test('*','-'))
