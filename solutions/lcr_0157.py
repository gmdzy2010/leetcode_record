from typing import List


def main(goods: str) -> List[str]:
    """有重复的全排列，回溯法

    和47题一样

    Args:
        - goods (str): 原字符串

    Returns:
        - List[str]: 所有的排列组合
    """
    visited: List[int] = [0] * len(goods)
    res: List[str] = []
    ans: List[str] = []

    splitted_goods = sorted(c for c in goods)
    backtracking(splitted_goods, visited, res, ans)

    return ans


def backtracking(
    goods: List[str],
    visited: List[int],
    res: List[str],
    ans: List[str],
):
    """回溯函数

    Args:
        goods (List[str]): 原字符串拆分成的数组
        visited (List[int]): 标记字符是否已访问过
        res (List[str]): 可能的排列
        ans (List[str]): 所有可能的排列
    """
    if len(res) == len(goods):
        ans.append("".join(res))
        return

    for i, c in enumerate(goods):
        # ! 注意这里的访问判断为上个重复元素位置是否被访问过
        if i > 0 and c == goods[i - 1] and visited[i - 1] == 1:
            continue

        if visited[i] == 1:
            continue

        res.append(c)
        visited[i] = 1

        backtracking(goods, visited, res, ans)

        res.pop()
        visited[i] = 0


if __name__ == "__main__":
    test_str = "agwb"
    print(main(test_str))
