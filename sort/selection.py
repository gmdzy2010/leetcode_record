"""
_summary_
"""
from typing import List


def main(arr: List[int | float]) -> List[int | float]:
    """_summary_

    Args:
        arr (List[int | float]): _description_

    Returns:
        List[int | float]: _description_
    """
    if len(arr) == 1:
        return arr

    for i, _ in enumerate(arr):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


if __name__ == "__main__":
    input_arr = [4, 1, 3, 5, 6, 8, 9, 2, 7]
    print(main(input_arr))
