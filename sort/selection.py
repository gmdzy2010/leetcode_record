from typing import List


def main(arr: List[int | float]) -> List[int | float]:
    """选择排序
    - 时间复杂度：O(N * N)
    - 空间复杂度：O(1)

    不断地从右侧选出最小的值放到左侧，每轮循环区域向右缩小，最终完成排序

    Args:
        arr (List[int | float]): 未排序数组

    Returns:
        List[int | float]: 已排序数组
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
