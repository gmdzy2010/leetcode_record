from typing import List


def main(arr: List[int | float]) -> List[int | float]:
    """冒泡排序
    - 时间复杂度：O(N * N)
    - 空间复杂度：O(1)

    每轮循环对比相邻两个元素的大小，较大的换到右侧，直到全部有序
    - 第一轮把最大值放到最右侧，缩小循环边界
    - 第二轮把次最大交换到次最右侧，缩小循环边界
    - ...
    - 循环结束，得到有序数组

    Args:
        arr (List[int | float]): 未排序数组

    Returns:
        List[int | float]: 已排序数组
    """
    for i, _ in enumerate(arr):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


if __name__ == "__main__":
    input_arr = [4, 1, 3, 5, 6, 8, 9, 2, 7]
    print(main(input_arr))
