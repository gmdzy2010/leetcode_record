def remove_duplicate_stack(string):
    stack = []
    for character in string:
        if stack and character == stack[-1]:
            stack.pop()
        else:
            stack.append(character)
    return ''.join(stack)


if __name__ == '__main__':
    print(remove_duplicate_stack('aaaabbaa'))
