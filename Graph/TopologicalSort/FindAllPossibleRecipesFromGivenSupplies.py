from typing import List
from collections import defaultdict, deque

class Solution:
    def dfs(self, node, edges, dp, cur_visited):
        if node in dp:
            return dp[node]
        
        if not edges[node]:
            dp[node] = False
            return dp[node]
        
        for nxt in edges[node]:
            if nxt not in dp:
                if nxt in cur_visited:
                    dp[nxt] = False
                    continue

                cur_visited.add(nxt)
                self.dfs(nxt, edges, dp, cur_visited)
                cur_visited.remove(nxt)
                
        dp[node] = all(dp[nxt] for nxt in edges[node])
        return dp[node]

    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        edges = defaultdict(list)
        dp = {}
        N = len(recipes)

        materials = set()
        for i in range(N):
            ingredient = ingredients[i]
            recipe = recipes[i]
            materials.add(recipe)
            for material in ingredient:
                materials.add(material)
                edges[recipe].append(material)
        
        for supply in supplies:
            dp[supply] = True
            
        cur_visited = set()
        for material in list(materials):
            if material not in dp:
                cur_visited.add(material)
                self.dfs(material, edges, dp, cur_visited)
                cur_visited.remove(material)
        ans = []
        for recipe in recipes:
            if dp[recipe]:
                ans.append(recipe)
        return ans


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