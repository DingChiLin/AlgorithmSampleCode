# traveling salesman
from re import I
from typing import List
from collections import defaultdict
from math import inf

class Solution:
    def distance(self, s1, s2):
        N = min(len(s1), len(s2))
        max_coverage = 0
        for i in range(1, N+1):
            s1_suffix = s1[-i:]
            s2_prefix = s2[:i]
            if s1_suffix == s2_prefix:
                max_coverage = i
        return len(s2) - max_coverage

    def shortestSuperstring(self, words: List[str]) -> str:
        N = len(words)
        distances = [[self.distance(words[i], words[j]) for j in range(N)] for i in range(N)]
        dp = [[inf for _ in range(N)] for _ in range(1<<N)]
        path = [[(None, None) for _ in range(N)] for _ in range(1<<N)]

        for mask in range(1<<N):
            possible_cur_bits = []
            for cur_bit in range(N):
                if (mask & (1<<cur_bit)) != 0:
                    possible_cur_bits.append(cur_bit)
            
            for cur_bit in possible_cur_bits:
                dp[mask][cur_bit] = inf
                
                last_mask = mask ^ (1 << cur_bit)
                if last_mask == 0:
                    dp[mask][cur_bit] = len(words[cur_bit])
                else:
                    possible_last_bits = []
                    for last_bit in range(N):
                        if (last_mask & (1<<last_bit)) != 0:
                            possible_last_bits.append(last_bit)

                    for last_bit in possible_last_bits:
                        total_distance = dp[last_mask][last_bit] + distances[last_bit][cur_bit]
                        if total_distance < dp[mask][cur_bit]:
                            dp[mask][cur_bit] = total_distance
                            path[mask][cur_bit] = (last_mask, last_bit)

        best_last_bit = 0
        best_len = inf
        for i in range(N):
            if dp[(1<<N) - 1][i] < best_len:
                best_len = dp[(1<<N) - 1][i]
                best_last_bit = i

        word_order = []
        cur_mask = (1<<N) - 1
        cur_bit = best_last_bit
        while cur_bit != None:
            word_order.append(cur_bit)
            cur_mask, cur_bit = path[cur_mask][cur_bit]
        word_order = word_order[::-1]

        answer = words[word_order[0]]
        for i in range(1, N):
            last_word_id = word_order[i-1]
            cur_word_id = word_order[i]
            d = distances[last_word_id][cur_word_id]
            answer += words[cur_word_id][-d:]

        return answer


S = Solution()
words = ["catg","ctaagt","gcta","ttca","atgcatc"]
# words = ["abc", "bcd", "efghi", "efghij", "de"]
print(S.shortestSuperstring(words))