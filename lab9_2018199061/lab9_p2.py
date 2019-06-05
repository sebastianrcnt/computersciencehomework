# Import modules
import stack
import sys

# Define functions


def terminate():
    """
    prints 'Evaluation error' and terminates the program
    :return: None
    """
    print('Evaluation error')
    sys.exit()


# Repeat Infinitely
while True:
    # Init
    # get user input
    ans = input('Enter an RPN expression:')

    # terminate if ans is 'q'
    if ans == 'q':
        sys.exit()

    # split ans into list and assign itself
    ans = ans.split()

    # generate mainStack
    mainStack = stack.getStack()

    # Pre Malformed Detection
    # there should exist a unique '=' at the right-most position of the statement
    if ans.count('=') != 1:  # not having one or having more than one
        # "=" not in right-most position
        terminate()
    if ans[-1] != '=':  # has one but not at the right-most position
        # "=" not in right-most position
        terminate()

    # iterate ans
    for item in ans:
        # when item is an operator(excluding '=')
        if item in ['+', '-', '*', '/']:
            # detect stack underflow: need at least two operands for an operator.
            if len(mainStack) < 2:
                # stack underflow
                terminate()

            # if there is at least two numbers, pop them
            num1 = stack.pop(mainStack)
            num2 = stack.pop(mainStack)

            # do the given operation and push it to mainStack
            if item == '+':
                stack.push(mainStack, num2 + num1)
            elif item == '-':
                stack.push(mainStack, num2 - num1)
            elif item == '*':
                stack.push(mainStack, num2 * num1)
            elif item == '/':
                stack.push(mainStack, num2 / num1)

        # when item is '='
        elif item == '=':
            if stack.isEmpty(mainStack):
                # stack underflow
                terminate()
            num = stack.pop(mainStack)
            if not stack.isEmpty(mainStack):
                # stack not empty after "="
                terminate()

            # print value of expression
            if float.is_integer(num):
                # when num is an integer(ex: 1.0)
                print('Value of expression: {:}'.format(int(num)))
            else:
                # when num is non-integer float(ex:5.5)
                print('Value of expression: {:.2f}'.format(num))

        # if item is an operand
        else:
            # push item to mainStack
            stack.push(mainStack, float(item))
