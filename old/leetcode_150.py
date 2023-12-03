def eval_reverse_polish_notation(tokens):
    operation_map = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: int(x / y),
    }
    stack = []
    for token in tokens:
        if token in operation_map:
            y, x = stack.pop(), stack.pop()
            stack.append(operation_map[token](x, y))
        else:
            stack.append(int(token))
    return stack[-1]


if __name__ == '__main__':
    test_tokens = ["4", "13", "5", "/", "+"]
    print(eval_reverse_polish_notation(test_tokens))
