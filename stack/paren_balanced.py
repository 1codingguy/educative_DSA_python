from stack import Stack

def is_match(p1, p2):
    """
    check if the input are matching parenthesis pair
    """
    if p1 == '(' and p2 == ')':
        return True
    if p1 == '[' and p2 == ']':
        return True
    if p1 == '{' and p2 == '}':
        return True
    else:
        return False


all_opening_parens = '({['
# dummy_parens = '([])'
# len == 9
# last index == 8

# current implementation only includes parenthesis as input, not other characters


def is_paren_balanced(paren_string):
    s = Stack()
    is_balanced = True
    index = 0

    while index < len(paren_string) and is_balanced:
        current_paren = paren_string[index]
        if current_paren in all_opening_parens:
            s.push(current_paren)
        else:
            # if there's a closing bracket, and the stack is empty, since there's no opening parenthesis in the stack (because the stack is empty), then it's imbalanced
            # handles special case?
            if s.is_empty():
                is_balanced = False
                break
            else:
                # if the stack is not empty, and the current parenthesis is not an opening one (implies it's a closing bracket?)
                top = s.pop()
                if not is_match(top, current_paren):
                    is_balanced = False
                    break
        index += 1

    # after the while loop is broken out
    if is_balanced and s.is_empty():
        return True
    else:
        return False


print("String : (((({})))) Balanced or not?")
print(is_paren_balanced("(((({}))))"))

print("String : [][]]] Balanced or not?")
print(is_paren_balanced("[][]]]"))

print("String : [][] Balanced or not?")
print(is_paren_balanced("[][]"))

