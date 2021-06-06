from typing import List
from collections import defaultdict, deque
from math import inf

class Solution:
    def __init__(self):
        self.ans = []
    
    def dfs(self, node, edges, beginWord, path):
        if (node == beginWord):
            self.ans.append(path[::-1])
        
        for n in edges[node]:
            path.append(n)
            self.dfs(n, edges, beginWord, path)
            path.pop()

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        N = len(wordList)
        M = len(wordList[0])
        graph = defaultdict(list)
        wordSet = set(wordList)
        wordSet.add(beginWord)
        for word in wordSet:
            for i in range(M):
                graph[word[:i] + '_' + word[i+1:]].append(word)

        que = deque()
        visited = defaultdict(int)
        fromWords = defaultdict(list)
        que.append((beginWord, 1))
        visited[beginWord] = 1
        min_distance = inf

        while que:
            w, d = que.popleft()
            if d > min_distance:
                break
            if (w == endWord):
                min_distance = d

            for i in range(M):
                for nw in graph[w[:i] + '_' + w[i+1:]]:
                    if nw != w:
                        if nw not in visited:
                            visited[nw] = d
                            fromWords[nw].append(w)
                        else:
                            if d == visited[nw]:
                                fromWords[nw].append(w)
                            continue
                        que.append((nw, d + 1))

        self.ans = []
        self.dfs(endWord, fromWords, beginWord, [endWord])
        return self.ans

s = Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

print(s.ladderLength(beginWord, endWord, wordList))