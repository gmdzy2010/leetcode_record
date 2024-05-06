from typing import List


def main(numRows: int) -> List[List[int]]:
    """杨辉三角

    Args:
        - numRows (int): 行数

    Returns:
        - List[List[int]]: 生成的杨辉三角
    """
    ans: List[List[int]] = []
    for i in range(numRows):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(ans[i - 1][j - 1] + ans[i - 1][j])

        ans.append(row)

    return ans


if __name__ == "__main__":
    print(main(5))
