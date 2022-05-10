from collections import defaultdict

# node: 1~V
class EulerianPath:

    def __init__(self):
        self.visited_e = set()
        self.stk = []
        self.e_cnt = []

    def dfs(self, node, edges):
        while(self.e_cnt[node] < len(edges[node])):
            v, i = edges[node][self.e_cnt[node]]
            self.e_cnt[node] += 1
            if (i not in self.visited_e):
                self.visited_e.add(i)
                self.dfs(v, edges)
        self.stk.append(node)

    def solve(self, V, E, graph):

        self.e_cnt = [0] * (V+1)
        edges = defaultdict(list)

        for i in range(len(graph)):
            u, v = graph[i]
            edges[u].append((v, i)) # 有向邊
            edges[v].append((u, i)) # 有向邊
        
        for v in range(1, V+1):
            edges[v].sort()

        odd_cnt = 0
        odd_one = -1
        odd_two = -1
        even_one = -1
        for i in range(1, V+1):
            if (len(edges[i]) >= 2):
                if (even_one == -1):
                    even_one = i

            if ((len(edges[i]) & 1)):
                if (odd_cnt == 0):
                    odd_one = i
                else:
                    odd_two = i
                odd_cnt += 1

        if (odd_cnt == 0):
            self.dfs(even_one, edges)
            # // dfs(1); if required to start from 1
            for e in range(E):
                if (e not in self.visited_e):
                    return []
            return self.stk
        elif (odd_cnt == 2):
            if (odd_one > odd_two):
                odd_one, odd_two = odd_two, odd_one
            
            self.dfs(odd_one, edges)
            # // dfs(1); // if required to start from 1
            for e in range(E):
                if (e not in self.visited_e):
                    return []
            return self.stk
        else:
            return []

# // link: https://tioj.ck.tp.edu.tw/problems/1084
# // 可處理雙向、多重邊、自連邊
# // 會輸出字典序最小的路徑

def main():
    V = 6
    E = 11
    graph = [
        [3, 1],
        [2, 3],
        [1, 5],
        [3, 5],
        [4, 3],
        [5, 4],
        [6, 5],
        [6, 1],
        [2, 1],
        [2, 1],
        [3, 3],
    ]
    s = EulerianPath()
    ans = s.solve(V, E, graph)
    print(ans)

main()
