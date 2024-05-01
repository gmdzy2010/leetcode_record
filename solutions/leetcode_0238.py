from typing import List


def main(nums: List[int]) -> List[int]:
    """除自身以外的乘积

    当前位置结果：左部分乘积 * 右部分乘积
    ans[i] = num[:i] * nums[i+1:]
               L     *     R

    nums  ->  [    1           2           3          4    ]
    ans   ->  (1)*(2*3*4)  (1)*(3*4)    (1*2)*(4)  (1*2*3)*(1)
               L *   R      L *  R        L  * R      L  * R

    第一轮循环计算每个数字左部分乘积
    第二轮循环计算每个数字右部分乘积

    Args:
        - nums (List[int]): 原数组

    Returns:
        - List[int]: 乘积列表
    """
    size = len(nums)
    ans, tmp = [1] * size, 1

    # * 先计算左侧乘积
    for i in range(1, size):
        ans[i] = ans[i - 1] * nums[i - 1]

    # * 再计算右侧乘积
    for i in reversed(range(size - 1)):
        tmp *= nums[i + 1]
        ans[i] *= tmp

    return ans


if __name__ == "__main__":
    test_nums = [1, 2, 3, 4, 5, 6]
    print(main(test_nums))
