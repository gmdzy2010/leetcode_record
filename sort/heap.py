from typing import List


def main(arr: List[int]):
    """堆排序
    - 时间复杂度：O(N * logN)
    - 空间复杂度：O(1)

    使用大根堆组织数组数据，再依次让数组最大值出堆即可得到排序后的数组
    - 让数组元素依次用入堆方法入堆，则第一个元素一定是最大
    - 交换第一个和最后一个元素，减小堆大小
    - 重复上一步，直至堆大小变为0

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

    大根堆，假设数组元素位置为 i，则有
    - 对于每个子树而言，其根节点都是整棵树最大
    - 大根堆构造的时候都是从左节点开始处理，然后右节点
    - 左节点位置：2 * i + 1
    - 右节点位置：2 * i + 2

    将待插入数据 arr[ix] 插入大根堆，并调整至合适的堆数组的位置
    待插入数据 arr[ix] 与其父节点位置元素 arr[parent(ix)] 比较
    - arr[ix] > arr[parent(ix)] -> 交换父子节点元素
    - 重复上述过程至满足大根堆要求

    Args:
        - arr (List[int]): 堆数组
        - ptr (int): 当前元素的下标，一般是堆尾（堆数组最后的元素）
    """
    while arr[ix] > arr[parent(ix)]:
        arr[ix], arr[parent(ix)] = arr[parent(ix)], arr[ix]
        ix = parent(ix)


def heapify(arr: List[int], ix: int, size: int):
    """调整堆

    - 先比较当前元素的左右孩子哪个大，再比较孩子和父节点哪个大，将较大的和小的交换
    - 当较大元素位置已经是当前的位置，停止循环

    Args:
        arr (List[int]): 堆数组
        ix (int): 当前位置
        size (int): 堆大小（非数组大小）
    """
    # * 从当前节点一直向下处理
    while left(ix) < size:
        # * 两个孩子中谁的值大，largest就记下谁的位置
        if right(ix) < size and arr[left(ix)] < arr[right(ix)]:
            ix_largest = right(ix)
        else:
            ix_largest = left(ix)

        # * 父和孩子中谁的值大，largest就记下谁的位置
        if arr[ix_largest] < arr[ix]:
            ix_largest = ix

        # * 最大已经到当前位置，可以停止调整了
        if ix_largest == ix:
            break

        # * 交换最大和当前元素位置
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
