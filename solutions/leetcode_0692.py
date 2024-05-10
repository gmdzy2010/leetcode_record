import heapq
from typing import Dict, List, Self


class Element:
    def __init__(self, word: str, cnt: int):
        self.word = word
        self.cnt = cnt

    def __lt__(self, other: Self) -> bool:
        return self.cnt < other.cnt


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt: Dict[str, int] = {}
        for w in words:
            if w in cnt:
                cnt[w] += 1
            else:
                cnt[w] = 1

        pq: List[Element] = []
        for w, c in cnt.items():
            heapq.heappush(pq, Element(w, c))
            if len(pq) > k:
                heapq.heappop(pq)

        pq.sort(reverse=True)

        return [e.word for e in pq]
