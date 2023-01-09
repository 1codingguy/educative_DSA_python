from stack import Stack


def decimal_to_binary(input_decimal: int):

    stack = Stack()

    while input_decimal != 0:
        stack.push(input_decimal % 2)
        input_decimal //= 2

    # print(stack)

    binary = ''

    while not stack.is_empty():
        binary += str(stack.pop())

    # print(binary)
    return binary


test_decimal = 242

decimal_to_binary(test_decimal)
