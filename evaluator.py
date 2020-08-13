import math

from collections import deque

from tokenizer import TokenType

evalStack = deque()
result = None
operations = {
    'm': lambda x: -x,
    'floor': lambda x: math.floor(x),
    'ceil': lambda x: math.ceil(x),
    'round': lambda x: round(x),
    '^': lambda x, y: x ** y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '<': lambda x, y: x < y,
    '<=': lambda x, y: x <= y,
    '>': lambda x, y: x > y,
    '>=': lambda x, y: x >= y,
    '=': lambda x, y: x == y,
    '!=': lambda x, y: x != y,
    '!': lambda x: not x,
    '&': lambda x, y: x and y,
    '|': lambda x, y: x or y,
    'eq': lambda x, y: x == y,
    'xor': lambda x, y: x != y
}


def evaluate(expression):
    for token in expression:
        if token.type == TokenType.NUMBER:
            evalStack.append(token.str)
        elif token.type == TokenType.BOOL:
            if token.str == 'true':
                evalStack.append(True)
            else:
                evalStack.append(False)
        else:
            op = operations[token.str]
            args = []
            for i in range(op.__code__.co_argcount):
                args.insert(0, evalStack.pop())
            evalStack.append(op(*args))
    if len(evalStack) == 1:
        return evalStack.pop()
    else:
        return None
