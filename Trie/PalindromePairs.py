from typing import List
from collections import defaultdict

''' 
Basic
'''
from typing import List
from collections import defaultdict

class Node:
    def __init__(self):
        self.idx = None
        self.nodes = defaultdict(list)
        self.palindrome_childs = []

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word, word_idx):
        curr = self.root
        for i, c in enumerate(word):
            if word[i:] == word[i:][::-1]:
                curr.palindrome_childs.append(word_idx)
            if not curr.nodes[c]:
                curr.nodes[c] = Node()
            curr = curr.nodes[c]
        curr.idx = word_idx

    def find(self, word, word_idx, ans):
        curr = self.root
        N = len(word)
        for i, c in enumerate(word):
            if curr.nodes[c]:
                curr = curr.nodes[c]
            else:
                break
                
            if i == N-1:
                # case 1: reversed word only
                if curr.idx != None and word_idx != curr.idx:
                    ans.append([word_idx, curr.idx])

                # case 2: reversed word + palindrome
                for child_idx in curr.palindrome_childs:
                    if word_idx != child_idx:
                        ans.append([word_idx, child_idx])
            else:
                # case 3: reversed first part of word and second part of word is palindrome
                if curr.idx != None and word[i+1:] == word[i+1:][::-1] and word_idx != curr.idx:
                    print([word_idx, curr.idx])
                    ans.append([word_idx, curr.idx])

        # self palindrome & empty word
        if word and word == word[::-1] and self.root.idx != None and word_idx != self.root.idx:
            ans.append([word_idx, self.root.idx])

        # empty word & self.palindrome
        if not word:
            for child_idx in self.root.palindrome_childs:
                if word_idx != child_idx:
                    ans.append([word_idx, child_idx])           

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        trie = Trie()
        for i, word in enumerate(words):
            trie.insert(word[::-1], i)
        ans = []
        for i, word in enumerate(words):
            trie.find(word, i, ans)
        return ans

S = Solution()
words = ["abcd","dcba","lls","s","sssll"]
words = ["bat","tab","cat"]
words = ["a",""]
words = ["a","abc","aba",""]
print(S.palindromePairs(words))


'''
More elegantly
'''

# from typing import List
# from collections import defaultdict

# class Node:
#     def __init__(self):
#         self.idx = None
#         self.nodes = defaultdict(Node)
#         self.palindrome_childs = []

# class Trie:
#     def __init__(self):
#         self.root = Node()

#     def insert(self, word, word_idx):
#         curr = self.root
#         for i, c in enumerate(word):
#             if word[i:] == word[i:][::-1]:
#                 curr.palindrome_childs.append(word_idx)
#             curr = curr.nodes[c]
#         curr.idx = word_idx

#     def find(self, word, word_idx, ans):
#         curr = self.root
#         for i, c in enumerate(word):
#             if curr.idx != None and word[i:] == word[i:][::-1] and word_idx != curr.idx:
#                 ans.append([word_idx, curr.idx])
#             if curr.nodes[c]:
#                 curr = curr.nodes[c]
#             else:
#                 break
#         # case 1: reversed word only
#         if curr.idx != None and word_idx != curr.idx:
#             ans.append([word_idx, curr.idx])

#         # case 2: reversed word + palindrome
#         for child_idx in curr.palindrome_childs:
#             if word_idx != child_idx:
#                 ans.append([word_idx, child_idx])

# class Solution:
#     def palindromePairs(self, words: List[str]) -> List[List[int]]:
#         trie = Trie()
#         for i, word in enumerate(words):
#             trie.insert(word[::-1], i)
#         ans = []
#         for i, word in enumerate(words):
#             trie.find(word, i, ans)
#         return ans
