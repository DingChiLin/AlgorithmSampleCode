from typing import List
from collections import defaultdict

class Node:
	def __init__(self):
		self.sentence = ""
		self.cnt = 0
		self.children = defaultdict(Node)
		self.leafs = []

class Trie:
    def __init__(self):
        self.root = Node()

    def add_leafs(self, node, leaf):
        exist = False
        for cur_leaf in node.leafs:
            if cur_leaf.sentence == leaf.sentence:
                exist = True
                cur_leaf.cnt = leaf.cnt
        if exist:
            node.leafs.sort(key = lambda n: (-n.cnt, n.sentence))
        else:
            node.leafs.append(leaf)
            node.leafs.sort(key = lambda n: (-n.cnt, n.sentence))
            node.leafs = node.leafs[:3]

    def add(self, sentence, cnt):
        cur = self.root
        for c in sentence:
            cur = cur.children[c]

        cur.sentence = sentence
        cur.cnt += cnt
        leaf = cur
        cur = self.root
        for c in sentence:
            cur = cur.children[c]
            self.add_leafs(cur, leaf)

class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        self.trie = Trie()
        self.sentence = ""
        self.cur_node = self.trie.root
        for i in range(len(sentences)):
            sentence = sentences[i]
            time = times[i]
            self.trie.add(sentence, time)

    def input(self, c: str) -> List[str]:
        if c == '#':
            self.trie.add(self.sentence, 1)
            self.cur_node = self.trie.root
            self.sentence = ""
            return []
        else:
            self.sentence += c
            self.cur_node = self.cur_node.children[c]
            return [n.sentence for n in self.cur_node.leafs]