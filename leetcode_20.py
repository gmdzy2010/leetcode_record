def is_valid_standard_lib(string):
    while "()" in string or "{}" in string or "[]" in string:
        string = string.replace("()", "").replace("{}", "").replace("[]", "")
    return string == ''


def is_valid_stack(string):
    stack, length = [], len(string)
    for index in range(length):
        if string[index] == '(':
            stack.append(')')
        elif string[index] == '[':
            stack.append(']')
        elif string[index] == '{':
            stack.append('}')
        
        # The top element of stack must match the current character
        elif string[index] != stack[-1]:
            return False
        elif not stack:
            return False
        else:
            stack.pop()
    return stack == []


if __name__ == '__main__':
    test_string = "{}(({}))"
    print(is_valid_stack(test_string))
    print(is_valid_standard_lib(test_string))
