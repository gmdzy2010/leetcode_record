def main(s: str) -> int:
    """最长回文串，集合法

    Args:
        - s (str): 原字符串

    Returns:
        - int: 最长回文串长度
    """
    ans, visited = 0, set()
    for c in s:
        if c in visited:
            ans += 2
            visited.remove(c)
        else:
            visited.add(c)

    return ans + 1 if visited else ans
