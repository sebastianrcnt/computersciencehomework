import stack

# Init
# Get Input
ans = input('Enter parentheses and/or braces:')

# Set Variables
openingParenthesis = ['(', '{', '[']
closingParenthesis = [')', '}', ']']
mainStack = stack.getStack()
isNestedProperly = True

# Iterate ans
for x in ans:
    # If x is a opening parenthesis, push x to mainStack
    if x in openingParenthesis:
        stack.push(mainStack, x)
    # If x is a closing parenthesis, pop one character from mainStack and assign it to poppedItem.
    elif x in closingParenthesis:
        # if stack is empty so that there is no left-pair left, assign isNestedProperly to False
        if stack.isEmpty(mainStack):
            isNestedProperly = False
        # if stack is not empty, pop one item from mainStack and assign it to poppedItem
        else:
            poppedItem = stack.pop(mainStack)
            # If the poppedItem is not a pair of x, assign isNestedProperly to False
            if closingParenthesis.index(x) != openingParenthesis.index(poppedItem):
                isNestedProperly = False

# if ans is nested properly, check if any unpaired opening(left) parenthesis left
if isNestedProperly and mainStack == []:
    isNestedProperly = True

# print the result
if isNestedProperly:
    print('Nested properly.')
else:
    print('Not properly nested.')
