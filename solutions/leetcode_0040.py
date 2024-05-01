from typing import List


def main(candidates: List[int], target: int):
    """数字组合总和2，回溯法

    Args:
        - candidates (List[int]): 候选数字
        - target (int): 累加和目标
    """
    ans2: List[List[int]] = []
    res2: List[int] = []

    backtracking(sorted(candidates), target, 0, 0, res2, ans2)
    print(ans2)


def backtracking(
    candidates: List[int],
    target: int,
    curr_sum: int,
    start: int,
    res: List[int],
    ans: List[List[int]],
):
    """回溯递归函数，剪枝

    Args:
        - candidates (List[int]): 候选数字
        - target (int): 累加和目标
        - curr_sum (int): 当前累加和
        - start (int): 开始下标
        - res (List[int]): 累加和等于 target 的数字组合
        - ans (List[List[int]]): 结果
    """
    if curr_sum == target:
        ans.append(res[:])

    size = len(candidates)
    for i in range(start, size):
        # * 将累加和的判断放在递归之前，可以少一层递归调用，但是前提是原数组有序
        if curr_sum + candidates[i] > target:
            break

        # * 去除数组中的重复元素
        # ! 注意数组已经排序，否则重复元素不相邻
        if i > start and candidates[i] == candidates[i - 1]:
            continue

        # * 累加当前数字
        curr_sum += candidates[i]
        res.append(candidates[i])

        backtracking(candidates, target, curr_sum, i + 1, res, ans)

        # * 撤销当前轮次操作
        curr_sum -= candidates[i]
        res.pop()


if __name__ == "__main__":
    test_nums = [2, 3, 6, 7]
    main(test_nums, 7)
