def main(x: int) -> bool:
    """判断回文数

    Args:
        - x (int): 待判断数字

    Returns:
        - bool: 判断结果
    """
    stack = []
    str_x = str(x)
    for c in str_x:
        stack.append(c)

    for c in str_x:
        if c != stack.pop():
            return False

    return True


if __name__ == "__main__":
    test_nums = -1223
    print(main(test_nums))
