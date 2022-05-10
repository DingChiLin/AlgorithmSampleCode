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
        in_cnt = [0] * (V+1)
        out_cnt = [0] * (V+1)

        for i in range(len(graph)):
            u, v = graph[i]
            in_cnt[v] += 1
            out_cnt[u] += 1
            edges[u].append((v, i)) # 有向邊
        
        for v in range(1, V+1):
            edges[v].sort()

        start = None
        end = None
        for i in range(1, V+1):
            diff = out_cnt[i] - in_cnt[i]
            if diff == 1:
                if start == None:
                    start = i
                else:
                    return []
            elif diff == -1:
                if end == None:
                    end = i
                else:
                    return []          
            elif diff == 0:
                continue
            else:
                return []

        if start == None:
            start = graph[0][0] # 任意點都行

        self.dfs(start, edges)
        for e in range(E):
            if (e not in self.visited_e):
                return []
        return self.stk[::-1]

# // link: https://tioj.ck.tp.edu.tw/problems/1084
# // 可處理雙向、多重邊、自連邊
# // 會輸出字典序最小的路徑

def main():
    V = 6
    E = 10
    graph = [
        [3, 1],
        [3, 2],
        [1, 5],
        [5, 3],
        [4, 3],
        [5, 4],
        [6, 5],
        [2, 1],
        [3, 3],
        [1, 6]
    ]
    s = EulerianPath()
    ans = s.solve(V, E, graph)
    print(ans)

def main():
    V = 6
    E = 9
    graph = [
        [3, 1],
        [3, 2],
        [1, 5],
        [5, 3],
        [4, 3],
        [5, 4],
        [6, 5],
        [2, 1],
        [3, 3],
    ]
    s = EulerianPath()
    ans = s.solve(V, E, graph)
    print(ans)

main()
