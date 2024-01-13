from typing import List


def main(ratings: List[int]) -> int:
    """分糖果

    总体需要两次遍历来分配糖果
    - 从左向右遍历，处理右边评分高的情况
    - 从右向左遍历，处理左边评分高的孩子，此时，因为第一次已经分过一次糖果
        - 如果左侧的孩子已经拿到了比右侧孩子糖果数量+1还多的糖果，就直接取这个数值
          比如 ..., 2, 3, 1, ...
          经过第一次分配后，中间的孩子已经拿到了3个糖果，逆序二次分配的时候，3 > 1+1，取 3
        - 如果 ..., 1, 2, 1, ...
          经过第一次分配后，中间的孩子拿到了2个糖果，逆序二次分配的时候，2 = 1+1，取 2

    Args:
        - ratings (List[int]): 每个孩子的评分

    Returns:
        - int: 最终总共分出去的糖果
    """
    size = len(ratings)
    divided = [1] * size

    # * 从左向右遍历，处理右边评分高的情况
    for i in range(1, size):
        if ratings[i - 1] < ratings[i]:
            divided[i] = divided[i - 1] + 1

    # * 处理左边评分高的孩子，倒着从倒数第二个孩子开始向左遍历
    for i in range(size - 1 - 1, -1, -1):
        if ratings[i] > ratings[i + 1]:
            # ! 注意这里需要保证评分高的孩子比两侧相邻的孩子分得的糖果都要多，所以要从
            # ! divided[i + 1] + 1 和 divided[i] 当中取最大值
            divided[i] = max(divided[i + 1] + 1, divided[i])

    return sum(divided)


if __name__ == "__main__":
    test_nums = [1, 2, 2]
    print(main(test_nums))
