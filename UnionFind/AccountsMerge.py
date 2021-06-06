from typing import List
from collections import defaultdict

class UnionFind:
    def __init__(self, N):
        self.nodes = [i for i in range(N)]
        self.rank = [1 for i in range(N)]       

    def root(self, n):
        if n != self.nodes[n]:
            self.nodes[n] = self.root(self.nodes[n])
        return self.nodes[n]

    def union(self, n1, n2):
        r1 = self.root(n1)
        r2 = self.root(n2)
        if r1 != r2:
            if self.rank[r1] < self.rank[r2]:
                self.nodes[r1] = r2
            elif self.rank[r1] > self.rank[r2]:
                self.nodes[r2] = r1
            else:
                self.nodes[r2] = r1
                self.rank[r1] += 1

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        name_mapping = {}
        email_mapping = defaultdict(list)
        N = len(accounts)
        u = UnionFind(N)

        for i, account in enumerate(accounts):
            name_mapping[i] = account[0]
            for email in account[1:]:
                email_mapping[email].append(i)

        for email, indexes in email_mapping.items():
            for i in range(len(indexes)-1):
                u.union(indexes[i], indexes[i+1])

        user_emails = [[] for _ in range(N)]
        for i in range(N):
            r = u.root(i)
            emails = accounts[i][1:]
            user_emails[r].extend(emails)

        ans = []
        for i in range(N):
            if (len(user_emails[i]) > 0):
                tmp = []
                tmp.append(name_mapping[i])
                tmp.extend(sorted(list(set(user_emails[i]))))
                ans.append(tmp)

        return ans

s = Solution()
accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
print(s.accountsMerge(accounts))