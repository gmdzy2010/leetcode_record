from typing import List


def main(g: List[int], s: List[int]) -> int:
    """分饼干

    Args:
        - g (List[int]): 孩子胃口
        - s (List[int]): 饼干尺寸

    Returns:
        - int: 能养活的最多孩子数量
    """
    # * 现将孩子胃口和饼干大小整体排序
    # * 局部最优：大饼干给胃口大的孩子，全剧最优就是喂饱最多的孩子
    g, s = sorted(g), sorted(s)
    g_size, s_size = len(g), len(s)

    ans = 0

    # * 从饼干尺寸最大和胃口最大开始倒着往回走，直到不能分为止
    s_i, g_i = s_size - 1, g_size - 1
    while g_i >= 0:
        # * 孩子胃口比饼干小或者刚好相等就分配
        if s_i >= 0 and g[g_i] <= s[s_i]:
            ans += 1
            s_i -= 1

        g_i -= 1

    return ans


if __name__ == "__main__":
    test_g, test_s = [1, 2, 3], [1, 1]
    print(main(test_g, test_s))
