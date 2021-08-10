class TrieNode:
    def __init__(self):
        self.cnt = 0
        self.links = {}
        self.word = ""
        self.word_cnt = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def get_root(self):
        return self.root
    
    def insert(self, word):
        curr = self.root
        for c in word:
            if c in curr.links:
                curr = curr.links[c]
            else:
                curr.links[c] = TrieNode()
                curr = curr.links[c]
            curr.cnt += 1
        curr.word = word
        curr.word_cnt += 1

    def remove(self, word): # word most existed
        curr = self.root
        for c in word:
            curr.links[c].cnt -= 1
            if (curr.links[c].cnt == 0):
                del curr.links[c]
                return
            else:
                curr = curr.links[c]
        curr.word_cnt -= 1
        if curr.word_cnt == 0:
            curr.word = ""

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c in curr.links:
                curr = curr.links[c]
            else:
                return False
        if curr.word:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c in curr.links:
                curr = curr.links[c]
            else:
                return False
        return True

    def find_all(self):
        result = []
        stack = [self.root]
        while stack:
            node = stack.pop()
            if node.word:
                result.append((node.word, node.word_cnt))
            for _, n in node.links.items():
                stack.append(n)
        return result

    def find_max(self):
        max_number = 0
        word = None
        stack = [self.root]
        while stack:
            node = stack.pop()
            if node.word:
                if node.cnt > max_number:
                    max_number = node.word_cnt
                    word = node.word
            else:
                for _, n in node.links.items():
                    stack.append(n)
        return (word, max_number)
