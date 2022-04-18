from functools import lru_cache
from typing import List
from math import inf


'''
Basic Idea
'''
class TreeNode:
	def __init__(self):
		self.end = False
		self.nodes = [None] * 2

class Trie:
    def __init__(self):
        self.root = TreeNode()

    def insert(self, bits):
        curr = self.root
        for bit in bits:
            if not curr.nodes[bit]:
                curr.nodes[bit] = TreeNode()
            curr = curr.nodes[bit]
        curr.end = True

    def get_max_xor_val(self, bits, max_bit):
        curr = self.root
        digit_val = 0
        for i in range(max_bit):
            bit = bits[i]
            complement = (bit+1) % 2
            if curr.nodes[complement]:
                digit_val += (1<<(max_bit-i-1))
                curr = curr.nodes[complement]
            else:
                curr = curr.nodes[bit]
        return digit_val

class Solution:
    @lru_cache(None)
    def get_bits(self, n, max_bit):
        bits = [0] * max_bit
        for i in range(max_bit):
            bit = (1<<(max_bit-i-1))
            if n >= bit:
                n -= bit
                bits[i] = 1
        return bits

    def findMaximumXOR(self, nums: List[int]) -> int:
        max_bit = max(nums).bit_length()
        trie = Trie()
        for n in nums:
            bits = self.get_bits(n, max_bit)
            trie.insert(bits)

        ans = -inf
        for n in nums:
            bits = self.get_bits(n, max_bit)
            ans = max(ans, trie.get_max_xor_val(bits, max_bit))

        return ans

'''
Improved Version
'''

class Trie:
    def __init__(self, max_bit):
        self.root = [None, None]
        self.max_bit = max_bit

    def insert(self, bits):
        digit_val = 0
        add_node = self.root
        xor_node = self.root
        for i in range(self.max_bit):
            bit = bits[i]
            if not add_node[bit]:
                add_node[bit] = [None, None]
            add_node = add_node[bit]            
            
            complement = (1 - bit)
            if xor_node[complement]:
                digit_val += (1<<(self.max_bit-i-1))
                xor_node = xor_node[complement]
            else:
                xor_node = xor_node[bit]
        return digit_val

class Solution:
    @lru_cache(None)
    def get_bits(self, n, max_bit):
        bits = [0] * max_bit
        for i in range(max_bit):
            if n & 1:
                bits[i] = 1
            n >>= 1
        return bits[::-1]

    def findMaximumXOR(self, nums: List[int]) -> int:
        max_bit = max(nums).bit_length()
        trie = Trie(max_bit)
        ans = -inf
        for n in nums:
            bits = self.get_bits(n, max_bit)
            ans = max(ans, trie.insert(bits)) # calculate current answer while insert

        return ans

