from typing import List


def main(n: int, k: int) -> List[List[int]]:
    """数字组合

    - 回溯法 + 减枝

    Args:
        - n (int): 组合数字的和
        - k (int): 组合包含数字个数

    Returns:
        - List[List[int]]: 所有组合结果列表
    """
    ans: List[List[int]] = []

    # * 保留每个组合的结果
    path: List[int] = []

    # backtracking(n, k, 1, path, ans)
    backtracking(n, k, 0, 1, path, ans)

    return ans


def backtracking(
    n: int,
    k: int,
    curr_sum: int,
    start: int,
    path: List[int],
    ans: List[List[int]],
):
    """回溯函数，剪枝版

    Args:
        - n (int): 组合数字的和
        - k (int): 组合包含数字个数
        - curr_sum (int): 组合包含数字累加和
        - start (int): 组合开始的数字
        - path (List[int]): 满足条件的组合
        - ans (List[List[int]]): 结果
    """
    size = len(path)
    if k == size:
        if curr_sum == n:
            ans.append(path[:])

        # * 无论是和不满足条件还是已经达到了 k 值，都得结束回溯
        return

    # * 如果 可选数字个数 已经少于 待选数字个数，就不需要再回溯了
    end = 9 - (k - size) + 1

    for i in range(start, end + 1):
        # * 每轮循环累加当前选择的数字
        curr_sum += i

        # * 本轮回溯的数字填进去
        path.append(i)

        # * 下一轮回溯将下一个位置的数填进去
        backtracking(n, k, curr_sum, i + 1, path, ans)

        # * 回溯完再减掉
        curr_sum -= i

        # * 数字填进去呢要记得再弹出来，否则下一轮循环将会多一个数字在结果中
        path.pop()


if __name__ == "__main__":
    print(main(5, 2))
