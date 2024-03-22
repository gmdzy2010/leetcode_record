from typing import List, Self


class Trie:
    """前缀树简单实现"""

    def __init__(self):
        self.children: List[Self | None] = [None] * 26
        self.is_end = False

    def search_prefix(self, prefix: str) -> Self | None:
        """搜索前缀

        Args:
            - prefix (str): _description_

        Returns:
            - Self | None: 匹配的前缀树节点
        """
        curr = self
        for c in prefix:
            c = ord(c) - ord("a")
            if curr and not curr.children[c]:
                return None

            if curr:
                curr = curr.children[c]

        return curr

    def insert(self, word: str) -> None:
        """前缀树插入节点

        Args:
            - word (str): 待插入字符串
        """
        curr = self
        for c in word:
            c = ord(c) - ord("a")
            if curr and curr.children and not curr.children[c]:
                # ? 这里的类型mismatch很奇怪
                curr.children[c] = Trie()  # type: ignore

            if curr:
                curr = curr.children[c]

        if curr:
            curr.is_end = True

    def search(self, word: str) -> bool:
        """搜索单词是否匹配

        Args:
            - word (str): _description_

        Returns:
            - bool: _description_
        """
        node = self.search_prefix(word)

        return node is not None and node.is_end

    def startsWith(self, prefix: str) -> bool:
        """判断是否以前缀开头

        Args:
            - prefix (str): 前缀

        Returns:
            - bool: 判断结果
        """
        return self.search_prefix(prefix) is not None


if __name__ == "__main__":
    test_trie = Trie()
