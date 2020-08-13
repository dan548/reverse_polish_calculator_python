# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import tokenizer
import notationchanger
import evaluator


def token(text):
    # Use a breakpoint in the code line below to debug your script.
    expression = notationchanger.convert(tokenizer.tokenize(text))  # Press Ctrl+8 to toggle the breakpoint.
    return evaluator.evaluate(expression)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(token('-54   * 3-47 =1eq  2=3'))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
