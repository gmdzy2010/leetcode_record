from typing import List


def main(flowerbed: List[int], n: int) -> bool:
    """种花问题

    Args:
        - flowerbed (List[int]): 原数组
        - n (int): 待种花的数量

    Returns:
        - bool: 花圃能否种下 n 朵花
    """
    # * 处理边界问题方便，比如 "00101..." 或者 "...0100"，首尾位置均合法
    fb = [0] + flowerbed + [0]
    size = len(fb)

    # * 连续三个位置为 0 即可在中间位置种花
    for i in range(1, size - 1):
        if fb[i - 1] + fb[i] + fb[i + 1] == 0:
            fb[i] = 1
            n -= 1

    return n <= 0
