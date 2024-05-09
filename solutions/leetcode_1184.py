from typing import List


def main(distance: List[int], start: int, destination: int) -> int:
    """_summary_

    Args:
        distance (List[int]): _description_
        start (int): _description_
        destination (int): _description_

    Returns:
        int: _description_
    """
    if start > destination:
        start, destination = destination, start

    a = sum(distance[start:destination])
    b = sum(distance[:start] + distance[destination:])

    return min(a, b)
