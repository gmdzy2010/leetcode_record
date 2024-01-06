from typing import List


def main(n: int, k: int) -> List[List[int]]:
    """数字组合

    - 回溯法
    - 回溯法 + 减枝

    Args:
        - n (int): 不同数字个数
        - k (int): 组合包含数字个数

    Returns:
        - List[List[int]]: 所有组合结果列表
    """
    ans: List[List[int]] = []

    # * 保留每个组合的结果
    path: List[int] = []

    # backtracking(n, k, 1, path, ans)
    backtracking_cut(n, k, 1, path, ans)

    return ans


def backtracking(
    n: int,
    k: int,
    start: int,
    path: List[int],
    ans: List[List[int]],
):
    """回溯函数

    Args:
        - n (int): 不同数字个数
        - k (int): 组合包含数字个数
        - start (int): 组合开始的数字
        - path (List[int]): 满足条件的组合
        - ans (List[List[int]]): 结果
    """
    if len(path) == k:
        # * 组合中的数字个数达到 k 返回即可
        # ! 注意这里是切片复制
        ans.append(path[:])

        return

    for i in range(start, n + 1):
        # * 本轮回溯的数字填进去
        path.append(i)

        # * 下一轮回溯将下一个位置的数填进去
        backtracking(n, k, i + 1, path, ans)

        # * 数字填进去呢要记得再弹出来，否则下一轮循环将会多一个数字在结果中
        path.pop()


def backtracking_cut(
    n: int,
    k: int,
    start: int,
    path: List[int],
    ans: List[List[int]],
):
    """回溯函数，剪枝版

    Args:
        - n (int): 不同数字个数
        - k (int): 组合包含数字个数
        - start (int): 组合开始的数字
        - path (List[int]): 满足条件的组合
        - ans (List[List[int]]): 结果
    """
    size = len(path)
    if k == size:
        # * 组合中的数字个数达到 k 返回即可
        # ! 注意这里是切片复制
        ans.append(path[:])

        return

    # * 如果 可选数字个数 已经少于 待选数字个数，就不需要再回溯了
    end = n - (k - size) + 1

    for i in range(start, end + 1):
        # * 本轮回溯的数字填进去
        path.append(i)

        # * 下一轮回溯将下一个位置的数填进去
        backtracking_cut(n, k, i + 1, path, ans)

        # * 数字填进去呢要记得再弹出来，否则下一轮循环将会多一个数字在结果中
        path.pop()


if __name__ == "__main__":
    print(main(5, 2))
