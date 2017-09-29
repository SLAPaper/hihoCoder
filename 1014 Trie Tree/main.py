from __future__ import print_function, division, absolute_import, unicode_literals


class TrieTreeNode:
    def __init__(self, count=0):
        self.children = {}
        self.count = count


class TrieTree:
    def __init__(self):
        self.root = TrieTreeNode()

    def insert(self, word):
        current = self.root

        for c in word:
            if c not in current.children:
                current.children[c] = TrieTreeNode()
            current = current.children[c]
            current.count += 1

    def query(self, word):
        current = self.root
        for c in word:
            if c not in current.children:
                return 0
            current = current.children[c]
        return current.count


if __name__ == '__main__':
    trie = TrieTree()

    m = int(raw_input())
    for _ in range(m):
        trie.insert(raw_input())

    n = int(raw_input())
    for _ in range(n):
        print(trie.query(raw_input()))
