from typing import List

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
