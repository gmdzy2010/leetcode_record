from typing import List


def main(arr: List[int]):
    """堆排序
    - 时间复杂度：O(N * logN)
    - 空间复杂度：O(N)

    Args:
        - arr (List[int]): 未排序数组

    Returns:
        - List[int|float]: 已排序数组
    """
    if len(arr) < 2:
        return arr

    for i, _ in enumerate(arr):
        insert(arr, i)

    heap_size = len(arr)
    while heap_size > 0:
        heap_size -= 1
        arr[0], arr[heap_size] = arr[heap_size], arr[0]
        heapify(arr, 0, heap_size)

    return arr


def insert(arr: List[int], ix: int):
    """入堆

    将待插入数据 arr[ix] 插入大根堆，并调整至合适的堆数组的位置
    待插入数据 arr[ix] 与其父节点位置元素 arr[parent(ix)] 比较
    - arr[ix] > arr[parent(ix)] -> 交换父子节点元素
    - 重复上述过程至满足大根堆要求

    Args:
        - arr (List[int]): 堆数组
        - ptr (int): 当前插入元素的下标
    """
    while arr[ix] > arr[parent(ix)]:
        arr[ix], arr[parent(ix)] = arr[parent(ix)], arr[ix]
        ix = parent(ix)


def heapify(arr: List[int], ix: int, size: int):
    """调整堆

    Args:
        arr (List[int]): 堆数组
        ix (int): 当前位置
        size (int): 堆大小（非数组大小）
    """
    while left(ix) < size:
        # * 两个孩子中谁的值大，largest就记下谁的位置
        if right(ix) < size and arr[left(ix)] < arr[right(ix)]:
            ix_largest = right(ix)
        else:
            ix_largest = left(ix)

        # * 父和孩子中谁的值大，largest就记下谁的位置
        if arr[ix_largest] < arr[ix]:
            ix_largest = ix

        if ix_largest == ix:
            break

        arr[ix_largest], arr[ix] = arr[ix], arr[ix_largest]

        ix = ix_largest


def parent(index: int) -> int:
    """父节点位置

    Args:
        - index (int): 子节点位置

    Returns:
        - int: 父节点位置
    """
    return int((index - 1) / 2)


def left(index: int) -> int:
    """左孩子节点位置

    Args:
        - index (int): 当前位置

    Returns:
        - int: 左孩子节点位置
    """
    return index * 2 + 1


def right(index: int) -> int:
    """右孩子节点位置

    Args:
        - index (int): 当前位置

    Returns:
        - int: 右孩子节点位置
    """
    return index * 2 + 2


if __name__ == "__main__":
    input_arr = [2, 1, 3, 5, 4, 7, 9, 8, 6, 6, 6]
    print(main(input_arr))
