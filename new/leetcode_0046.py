from typing import List


def main(nums: List[int]) -> List[List[int]]:
    """排列问题，回溯法

    Args:
        - nums (List[int]): 原数组

    Returns:
        - List[List[int]]: 所有可能的排列
    """
    visited: List[int] = [0] * len(nums)
    res: List[int] = []
    ans: List[List[int]] = []

    backtracking(nums, visited, res, ans)

    return ans


def backtracking(
    nums: List[int],
    visited: List[int],
    res: List[int],
    ans: List[List[int]],
):
    """回溯函数

    Args:
        - nums (List[int]): 原数组
        - visited (List[int]): 标记元素是否被访问过
        - res (List[int]): 可能的排列
        - ans (List[List[int]]): 所有可能的排列
    """
    if len(res) == len(nums):
        ans.append(res[:])
        return

    for i, n in enumerate(nums):
        # * 跳过所有已经使用过的元素
        if visited[i] == 1:
            continue

        # * 用过一个标记元素就标记为已访问
        res.append(n)
        visited[i] = 1

        # ! 全排列问题中，所有元素都可以全部选择，所以每次回溯都必须从0开始找
        backtracking(nums, visited, res, ans)

        # * 回撤
        res.pop()
        visited[i] = 0


if __name__ == "__main__":
    input_arr = [1, 2, 3, 4]
    print(main(input_arr))
