from typing import List
from collections import defaultdict, deque

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        N = len(recipes)
        indegree = defaultdict(int)
        edges = defaultdict(list)
        for i in range(N):
            r = recipes[i]
            ings = ingredients[i]
            for ing in ings:
                edges[ing].append(r)
                indegree[r] += 1
 
        recipesSet = set(recipes)
        ans = []
        
        que = deque(supplies)
        while que:
            n = que.popleft()
            if n in recipesSet:
                ans.append(n)
            for nx in edges[n]:
                indegree[nx] -= 1
                if indegree[nx] == 0:
                    que.append(nx)
        return ans