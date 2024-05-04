from collections import deque
from typing import Deque, List


def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    """课程表

    Args:
        - numCourses (int): 课程表
        - prerequisites (List[List[int]]): 课程依赖关系

    Returns:
        - bool: 是否可以完成所有课程
    """
    in_cnts = [0] * (numCourses)
    adjacency = [[] for _ in range(numCourses)]
    queue: Deque[int] = deque()

    # * 计算每个课程的入度，构建邻接表
    for curr, depend in prerequisites:
        in_cnts[curr] += 1
        adjacency[depend].append(curr)

    # * 获取所有入度为 0 的课程，进入队列
    for i in range(numCourses):
        if not in_cnts[i]:
            queue.appendleft(i)

    # * 将课程中来自于入度为 0 的课程的入度去掉
    while queue:
        numCourses -= 1
        depend = queue.pop()
        for curr in adjacency[depend]:
            in_cnts[curr] -= 1
            if not in_cnts[curr]:
                queue.appendleft(curr)

    return not numCourses
