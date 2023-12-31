from typing import List


def main(path: str) -> str:
    """简化路径

    Args:
        - path (str): 待简化的路径

    Returns:
        - str: 简化后的路径
    """
    stack: List[str] = []
    for p in path.split("/"):
        # ! 分支顺序不能变，否则无法处理 /..这种情况
        if p == "..":
            if stack:
                stack.pop()

        elif p and p != ".":
            stack.append(p)

    return "/" + "/".join(stack)


if __name__ == "__main__":
    test_path = "/../"
    main(test_path)
