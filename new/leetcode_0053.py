from typing import List


def main(nums: List[int]) -> int:
    """_summary_

    Args:
        nums (List[int]): _description_

    Returns:
        int: _description_
    """
    ans = 0
    size = len(nums)
    if size < 2:
        return nums[0]

    return ans


if __name__ == "__main__":
    input_arr = []
    print(main(input_arr))
