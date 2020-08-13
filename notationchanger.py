from collections import deque

from tokenizer import TokenType

opStack = deque()

priority = {'m': 0, 'floor': 0, 'ceil': 0, 'round': 0, '^': 1,
            '*': 2, '/': 2, '+': 3, '-': 3, '<': 4,
            '<=': 4, '>': 4, '>=': 4, '=': 4, '!=': 4,
            '!': 5, '&': 6, '|': 7, 'eq': 8, 'xor': 8}

left_associativity = [True, False, False, False, False, True, False, False, False]


def convert(tokens):
    output = []
    last_token = None
    temp_token = None
    temp_priority = 127
    for t in tokens:
        temp_token = t
        if t.type == TokenType.NUMBER or t.type == TokenType.BOOL:
            output.append(temp_token)
        elif t.type == TokenType.L_BRACKET:
            opStack.append(temp_token)
        elif t.type == TokenType.R_BRACKET:
            while opStack[-1].type != TokenType.L_BRACKET:
                output.append(opStack.pop())
            opStack.pop()
        else:
            if t.str == '-' and not last_token or last_token.type != TokenType.NUMBER:
                temp_token.str = 'm'
                temp_priority = priority.get('m')
            else:
                temp_priority = priority.get(t.str)
            while True:
                if opStack:
                    top_priority = priority[opStack[-1].str]
                    if temp_priority > top_priority or \
                            temp_priority == top_priority and left_associativity[temp_priority]:
                        output.append(opStack.pop())
                    else:
                        opStack.append(temp_token)
                        break
                else:
                    opStack.append(temp_token)
                    break

        last_token = temp_token
    while opStack:
        output.append(opStack.pop())
    return output
