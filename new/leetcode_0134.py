from typing import List


def main(gas: List[int], cost: List[int]):
    """加油站，
    - 暴力解法
    - 贪心解法

    Args:
        - gas (List[int]): 每个加油站油量
        - cost (List[int]): 行驶到每个点的耗油量
    """
    ans1 = can_complete_circuit_normal(gas, cost)
    print(ans1)

    ans2 = can_complete_circuit_greedy(gas, cost)
    print(ans2)


def can_complete_circuit_normal(gas: List[int], cost: List[int]) -> int:
    """加油站，暴力解法

    Args:
        - gas (List[int]): 每个加油站油量
        - cost (List[int]): 行驶到每个点的耗油量

    Returns:
        - int: 可以绕一圈的出发点
    """
    size = len(cost)
    # * 看看从每个位置出发能不能回到起点
    for i in range(size):
        # * 剩余油量
        rest = gas[i] - cost[i]

        # * 汽车转圈圈的位置
        # ? 这里为啥是 i + 1 ？
        pos = (i + 1) % size

        # * 剩余油量大于零，说明此时可以模拟转圈了
        # * 假设从当前这个位置出发，康康最后到哪里了
        while rest > 0 and pos != i:
            rest += gas[pos] - cost[pos]
            pos = (pos + 1) % size

        # * 如果可以转一圈，且最终油量大于0，符合题意
        if rest >= 0 and pos == i:
            return i

    return -1


def can_complete_circuit_greedy(gas: List[int], cost: List[int]) -> int:
    """加油站，贪心法

    Args:
        - gas (List[int]): 每个加油站油量
        - cost (List[int]): 行驶到每个点的耗油量

    Returns:
        - int: 可以绕一圈的出发点
    """
    size = len(gas)

    # * 假设从 start 出发可以回到 start
    start = 0

    # * 当前剩余油量和总剩余油量
    curr_rest = 0
    total_rest = 0

    for i in range(size):
        # * 每过一个加油站就累加当前剩余油量和总剩余油量
        curr_rest += gas[i] - cost[i]
        total_rest += gas[i] - cost[i]

        # * 如果当前油量小于0，说明无法出发，让下一个位置成为起点
        if curr_rest < 0:
            # ! 如果下个位置也无法出发，下一轮循环得到的剩余油量也是负数，就到下下个位置
            start = i + 1

            # * 一旦累加油量小于零，起点重新计算，剩余油量也置0
            curr_rest = 0

    # * 如果遍历完加油站发现剩余总油量小于0，永远不可能回到起点
    if total_rest < 0:
        return -1

    return start


if __name__ == "__main__":
    test_gas, test_cost = [1, 2, 3, 4, 5], [3, 4, 5, 1, 2]
    main(test_gas, test_cost)
