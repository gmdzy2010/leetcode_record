def main(queryIP: str) -> str:
    """判断IP有效性

    Args:
        - queryIP (str): 待验证的IP地址字符串

    Returns:
        - str: 结果
    """
    # * 判断是否是 IPv4
    if queryIP.find(".") != -1:
        return check_ipv4(queryIP)

    return check_ipv6(queryIP)


def check_ipv4(queryIP: str) -> str:
    """检查是否是合法的IPv4地址

    Args:
        - queryIP (str): 待验证的IP地址字符串

    Returns:
        - str: 结果
    """
    # * 区段搜索开始位置
    start = 0
    for i in range(4):
        # * 如果是最后一个区段，搜索结束位置在最后一个位置的下一个位置（字符串长度）
        if i == 3:
            end = len(queryIP)

        # * 如果不是最后一个区段，搜索结束位置在分隔符 . 处
        else:
            end = queryIP.find(".", start)

        # * 没有找到 . 号分隔符，无效
        if end == -1:
            return "Neither"

        # * 每个区段不是 1 ~ 3 位，无效
        if end - start not in range(1, 4):
            return "Neither"

        # * 处理一位或连续多位IP数字段
        addr = 0
        for j in range(start, end):
            # * 如果区段中的任意字符不是数字字符串，无效
            if not queryIP[j].isdigit():
                return "Neither"

            addr = addr * 10 + int(queryIP[j])

        # * 子网地址段大于 255，无效
        if addr > 255:
            return "Neither"

        # * 地址大于零，但区段有前导零，无效
        # ! 比如 "012.1.1.1"
        if addr > 0 and queryIP[start] == "0":
            return "Neither"

        # * 区段地址转化为数字零，但区段的长度大于1，无效
        # ! 比如 "00.0.0.0"
        if addr == 0 and end - start > 1:
            return "Neither"

        start = end + 1

    return "IPv4"


def check_ipv6(queryIP: str) -> str:
    """检查是否是合法的IPv6地址

    Args:
        - queryIP (str): 待验证的IP地址字符串

    Returns:
        - str: 结果
    """
    start = -1
    for i in range(8):
        if i == 7:
            end = len(queryIP)
        else:
            end = queryIP.find(":", start)

        # * 没找到分隔符，无效
        if end == -1:
            return "Neither"

        # * 每个区段长度不是 1～4 位，无效
        if end - start not in range(1, 5):
            return "Neither"

        for j in range(start, end):
            # * 每个位置不是十六进制字符串表示，无效
            if not queryIP[j].isdigit() and not (
                "a" <= queryIP[j].lower() <= "f"
            ):
                return "Neither"

        start = end + 1

    return "IPv6"


if __name__ == "__main__":
    test_str = "192.168.0.1"
    print(main(test_str))
