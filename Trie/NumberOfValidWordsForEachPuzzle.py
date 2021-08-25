from typing import List

class TrieNode:
    def __init__(self):
        self.cnt = 0
        self.links = {}
        self.word = []
        self.word_cnt = 0

class Trie:
    def __init__(self):
        self.cnt = 0
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for c in word:
            if c in curr.links:
                curr = curr.links[c]
            else:
                curr.links[c] = TrieNode()
                curr = curr.links[c]
            curr.cnt += 1
        curr.word = word
        curr.word_cnt += 1

    def _count(self, node, need, valid, word_set):
        if valid and node.word_cnt > 0:
            self.cnt += node.word_cnt

        for c, nxt in node.links.items():
            if c in word_set:
                self._count(nxt, need, valid or (c == need), word_set)

    def count(self, need, words):
        self.cnt = 0
        self._count(self.root, need, False, set(words))
        return self.cnt

class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        trie = Trie()
        for word in words:
            trie.insert(sorted(set(word)))

        ans = [0] * len(puzzles)
        for i, puzzle in enumerate(puzzles):
            ans[i] = trie.count(puzzle[0], puzzle)

        return ans

s = Solution()
words = ["aa","aaaa","asas","able","ability","actt","actor","access","actre"]
puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]
print(s.findNumOfValidWords(words, puzzles))