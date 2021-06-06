from typing import List
from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        N = len(wordList)
        M = len(wordList[0])
        graph = defaultdict(list)
        wordSet = set(wordList)
        wordSet.add(beginWord)
        for word in wordSet:
            for i in range(M):
                graph[word[:i] + '_' + word[i+1:]].append(word)

        # print(graph)
        que = deque()
        visited = set([beginWord])
        que.append((beginWord, 1))
        while que:
            w, d = que.popleft()
            if (w == endWord):
                return d
            
            for i in range(M):
                for nw in graph[w[:i] + '_' + w[i+1:]]:
                    if nw != w and nw not in visited:
                        visited.add(nw)
                        que.append((nw, d + 1))

        return 0


s = Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]


print(s.ladderLength(beginWord, endWord, wordList))