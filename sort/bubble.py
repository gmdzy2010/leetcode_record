"""
Bubble sort
"""
from typing import List


def bubble(arr: List[int | float]) -> List[int | float]:
    """_summary_

    Args:
        arr (List[int | float]): _description_

    Returns:
        List[int | float]: _description_
    """
    for i, _ in enumerate(arr):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


if __name__ == "__main__":
    input_arr = [4, 1, 3, 5, 6, 8, 9, 2, 7]
    print(bubble(input_arr))
