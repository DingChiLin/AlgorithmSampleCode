from typing import List
from collections import defaultdict

class Node:
    def __init__(self):
        self.word = None
        self.nexts = defaultdict(Node)
        self.cnt = 0
        self.leafs = set()
        
class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, word, cnt):
        cur = self.root 
        for c in word:
            cur = cur.nexts[c]
        cur.word = word
        cur.cnt += cnt
        leaf = cur
        cur = self.root
        for c in word:
            cur.leafs.add(leaf)
            cur = cur.nexts[c]
        cur.leafs.add(leaf)
        
class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        self.trie = Trie()
        for i in range(len(sentences)):
            self.trie.insert(sentences[i], times[i])

        self.word = ""
        self.node = self.trie.root

    def input(self, c: str) -> List[str]:
        if c == '#':
            self.trie.insert(self.word, 1)
            self.word = ""
            self.node = self.trie.root
            return []
        else:
            self.word += c
            self.node = self.node.nexts[c]
            words = sorted([(-n.cnt, n.word) for n in self.node.leafs])[:3]
            return [w[1] for w in words]

obj = AutocompleteSystem(["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2])
print(obj.input("i"))
print(obj.input(" "))
print(obj.input("a"))
print(obj.input("#"))