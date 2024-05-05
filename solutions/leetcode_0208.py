from typing import Dict, Self


class Trie:
    """前缀树简单实现
    - children: 所有子节点，一般由数组或哈希表构成
    - is_end: 表示是否搜索到了字符串结尾

    """

    def __init__(self):
        self.children: Dict[str, Self] = {}
        self.is_end = False

    def insert(self, word: str) -> None:
        """前缀树插入节点

        Args:
            - word (str): 待插入字符串
        """
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = Trie()  # type: ignore
            curr = curr.children[c]

        curr.is_end = True

    def search(self, word: str) -> bool:
        """搜索单词是否匹配

        Args:
            - word (str): 待搜索单词

        Returns:
            - bool: 是否能够在当前前缀树中搜索到目标单词
        """
        curr = self
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]

        return curr.is_end

    def startsWith(self, prefix: str) -> bool:
        """判断是否以前缀开头，只要能遍历完前缀树就是合法前缀

        Args:
            - prefix (str): 前缀

        Returns:
            - bool: 判断 prefix 是否是前缀树的一个合法前缀
        """
        curr = self
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]

        return True

    def __repr__(self) -> str:
        return f"{self.children}"


if __name__ == "__main__":
    test_trie = Trie()
    test_trie.insert("apple")
    test_trie.search("apple")
    test_trie.search("app")
    test_trie.startsWith("app")

    test_trie.insert("app")
    test_trie.search("app")
