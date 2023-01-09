from stack import Stack


def reverse_string(stack: Stack, input_string: str):
    # push every char into the stack
    for char in input_string:
        stack.push(char)

    # init the rev_string variable
    rev_string = ''

    while not stack.is_empty():
        rev_string += stack.pop()

    return rev_string


s = Stack()
test_string = 'abcde'

print(
    reverse_string(stack=s, input_string=test_string)
)
