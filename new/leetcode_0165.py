def main(version1: str, version2: str):
    """比较版本号

    Args:
        - version1 (str): 版本号1
        - version2 (str): 版本号2
    """
    ans1 = compare_version_split(version1, version2)
    print(ans1)

    ans2 = compare_version_2pointers(version1, version2)
    print(ans2)


def compare_version_split(version1: str, version2: str) -> int:
    """比较版本号，分割法

    Args:
        - version1 (str): 版本号1
        - version2 (str): 版本号2

    Returns:
        - int: 比较结果
    """
    v1, v2 = version1.split("."), version2.split(".")
    size_1, size_2 = len(v1), len(v2)

    i, j = 0, 0
    while i < size_1 or j < size_2:
        # * 从两个字符串中分别解析出来数字
        n1, n2 = 0, 0
        if i < size_1:
            n1 = int(v1[i])
            i += 1
        if j < size_2:
            n2 = int(v2[j])
            j += 1

        # * 两个版本号不相等，时比较两个版本号
        if n1 != n2:
            return 1 if n1 > n2 else -1

    return 0


def compare_version_2pointers(version1: str, version2: str) -> int:
    """比较版本号，双指针法

    Args:
        - version1 (str): 版本号1
        - version2 (str): 版本号2

    Returns:
        - int: 比较结果
    """

    size_1, size_2 = len(version1), len(version2)
    i, j = 0, 0
    while i < size_1 or j < size_2:
        # * 将用点号分隔的每部分版本号数字解析出来，数字有一位或者连续多位
        num1 = 0
        # ! 每遇到点号就结算一下每个版本号
        while i < size_1 and version1[i] != ".":
            num1 = num1 * 10 + int(version1[i])
            i += 1

        # ! 要跳过点号，否则下一轮循环无法开始，后续的子版本号都会丢失
        i += 1

        # * 解析版本号2的版本号数字
        num2 = 0
        while j < size_2 and version2[j] != ".":
            num2 = num2 * 10 + int(version2[j])
            j += 1

        # * 同样跳过点
        j += 1

        # * 两个版本号不相等时比较两个版本号
        if num1 != num2:
            return 1 if num1 > num2 else -1

    return 0


if __name__ == "__main__":
    test_str1, test_str2 = "1.01", "1.003"
    main(test_str1, test_str2)
