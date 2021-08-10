"""
Version 1: Use Dictionary
"""

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

    def search(self, word):
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

    def startsWith(self, prefix):
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

T = Trie()
T.insert('word')
T.insert('word')
T.insert('word')
T.insert('wordd')
T.insert('get')
T.insert('cat')
T.insert('dog')
T.insert('world')
r = T.get_root()
print(r.links["w"].links["o"].links["r"].links["d"].links["d"].word)

print('--- find all and max ---')
print(T.find_all())
print(T.find_max())
print('--- search ---')
print(T.search('wor'))
print(T.search('word'))
print(T.search('wordd'))
print(T.search('worddd'))
print('--- starts with ---')
print(T.startsWith('wor'))
print(T.startsWith('word'))
print(T.startsWith('wordd'))
print(T.startsWith('worddd'))
print('--- remove ---')
T.remove('word')
print(T.find_all())
print(T.search('word'))
T.remove('word')
print(T.find_all())
print(T.search('word'))
print(T.search('wordd'))
T.remove('word')
print(T.find_all())
print(T.search('word'))
print(T.search('wordd'))
T.remove('wordd')
print(T.find_all())
print(T.search('word'))
print(T.search('wordd'))

"""
Version 2: Use Array
"""

# class TrieNode:
#     def __init__(self):
#         self.cnt = 0 # +1 for all the nodes in a path of a word
#         self.links = [None]*26
#         self.word = ""
#         self.word_cnt = 0

# class Trie:
#     def __init__(self):
#         self.root = TrieNode()
    
#     def get_root(self):
#         return self.root
    
#     def insert(self, word):
#         curr = self.root
#         for c in word:
#             index = ord(c) - ord('a')
#             if curr.links[index]:
#                 curr = curr.links[index]
#             else:
#                 curr.links[index] = TrieNode()
#                 curr = curr.links[index]
#             curr.cnt += 1
#         curr.word_cnt += 1
#         curr.word = word
    
#     def remove(self, word): # word most existed
#         curr = self.root
#         for c in word:
#             index = ord(c) - ord('a')
#             curr.links[index].cnt -= 1
#             if (curr.links[index].cnt == 0):
#                 curr.links[index] = None
#                 return
#             else:
#                 curr = curr.links[index]
#         curr.word_cnt -= 1
#         if curr.word_cnt == 0:
#             curr.word = ""

#     def search(self, word):
#         curr = self.root
#         for c in word:
#             index = ord(c) - ord('a')
#             if curr.links[index]:
#                 curr = curr.links[index]
#             else:
#                 return False
#         if curr.word:
#             return True
#         else:
#             return False

#     def startsWith(self, prefix):
#         curr = self.root
#         for c in prefix:
#             index = ord(c) - ord('a')
#             if curr.links[index]:
#                 curr = curr.links[index]
#             else:
#                 return False
#         return True

#     def find_all(self):
#         result = []
#         stack = [self.root]
#         while stack:
#             node = stack.pop()
#             if node.word:
#                 result.append((node.word, node.word_cnt))
#             for n in node.links:
#                 if n:
#                     stack.append(n)
#         return result

#     def find_max(self):
#         max_number = 0
#         word = None
#         stack = [self.root]
#         while stack:
#             node = stack.pop()
#             if node.word:
#                 if node.cnt > max_number:
#                     max_number = node.word_cnt
#                     word = node.word
#             else:
#                 for n in node.links:
#                     if n:
#                         stack.append(n)
#         return (word, max_number)

# T = Trie()
# T.insert('word')
# T.insert('word')
# T.insert('word')
# T.insert('wordd')
# T.insert('get')
# T.insert('cat')
# T.insert('dog')
# T.insert('world')
# r = T.get_root()
# print(r.links[22].links[14].links[17].links[3].links[3].word)

# print('--- find all and max ---')
# print(T.find_all())
# print(T.find_max())
# print('--- search ---')
# print(T.search('wor'))
# print(T.search('word'))
# print(T.search('wordd'))
# print(T.search('worddd'))
# print('--- starts with ---')
# print(T.startsWith('wor'))
# print(T.startsWith('word'))
# print(T.startsWith('wordd'))
# print(T.startsWith('worddd'))
# print('--- remove ---')
# T.remove('word')
# print(T.find_all())
# print(T.search('word'))
# T.remove('word')
# print(T.find_all())
# print(T.search('word'))
# print(T.search('wordd'))
# T.remove('word')
# print(T.find_all())
# print(T.search('word'))
# print(T.search('wordd'))
# T.remove('wordd')
# print(T.find_all())
# print(T.search('word'))
# print(T.search('wordd'))
