"""
_summary_
"""
from typing import List


def insertion(arr: List[int | float]) -> List[int | float]:
    """_summary_

    Args:
        arr (List[int | float]): _description_

    Returns:
        List[int|float]: _description_
    """
    for i, _ in enumerate(arr):
        for _ in range(i, len(arr) - 1):
            pass


if __name__ == "__main__":
    input_arr = [4, 1, 3, 5, 6, 8, 9, 2, 7]
    print(insertion(input_arr))
