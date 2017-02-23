from pythonds.basic.stack import Stack

def parChecker(symbolString):

    s = Stack()

    balanced = True

    index = 0

while index < len(symbolString) and balanced:

    symbol = symbolString[index]

    if symbol == "(":

        s.push(symbol)

    else:

        if s.isEmpty():

            balanced = False

        else:

            s.pop()
