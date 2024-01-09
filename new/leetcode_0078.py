from typing import List


def main(nums: List[int]) -> List[List[int]]:
    """数组所有子集，回溯法

    Args:
        - nums (List[int]): 原数组

    Returns:
        - List[List[int]]: 所有子集合
    """
    res: List[int] = []
    ans: List[List[int]] = []
    backtracking(nums, 0, res, ans)

    return ans


def backtracking(
    nums: List[int],
    start: int,
    res: List[int],
    ans: List[List[int]],
):
    """回溯函数

    Args:
        - nums (List[int]): 原数组
        - start (int): 开始位置
        - res (List[int]): 当前枚举的子集合
        - ans (List[List[int]]): 所有子集合
    """
    # * 每层递归都把当前的尝试加入到结果中
    ans.append(res[:])

    size = len(nums)

    # * 这里条件不加也行，但是加上更合理
    # ! 这里能取到 size，因为上一层的 start 进来本层递归的时候是 i + 1
    if start >= size:
        return

    for i in range(start, size):
        res.append(nums[i])

        # * 子集是集合，即每一个元素都不会重复取，下一轮 start 为 i + 1
        backtracking(nums, i + 1, res, ans)

        res.pop()


if __name__ == "__main__":
    test_nums = [1, 2, 3, 4, 5]
    print(main(test_nums))
