from enum import Enum


class TokenType(Enum):
    NUMBER = 1
    BOOL = 2
    OPERATOR = 3
    L_BRACKET = 4
    R_BRACKET = 5


token_to_type = {
    '(': TokenType.L_BRACKET,
    ')': TokenType.R_BRACKET,
    'true': TokenType.BOOL,
    'false': TokenType.BOOL
}


class Token:
    def __init__(self, token_type, input_string):
        self.type = token_type
        self.str = input_string

    def __str__(self):
        return f"{self.str}"


def type_define(token_string):
    if token_string.isnumeric():
        return Token(TokenType.NUMBER, int(token_string))
    else:
        token_str = token_string.lower()
        token_type = token_to_type.get(token_str, TokenType.OPERATOR)
        return Token(token_type, token_str)


def split_string(input_str):
    s = ''
    tokens = []
    for char in input_str:
        if char == ' ':
            if s != '':
                tokens.append(s)
                s = ''
            continue
        if char == '(' or char == ')':
            if s != '':
                tokens.append(s)
                s = ''
            tokens.append(char)
            continue
        if char.isdigit():
            if s.isdigit():
                s = s + char
            else:
                if s != '':
                    tokens.append(s)
                s = char
            continue
        if char.isalpha():
            if s.isalpha():
                s = s + char
            else:
                if s != '':
                    tokens.append(s)
                s = char
            continue
        elif s.isdigit() or s.isalpha():
            tokens.append(s)
            s = char
        else:
            s = s + char
    if s != '':
        tokens.append(s)
    return tokens


def tokenize(input_string):
    return map(type_define, split_string(input_string))
