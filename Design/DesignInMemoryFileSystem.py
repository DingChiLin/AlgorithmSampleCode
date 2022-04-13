from collections import defaultdict

class Node:
    def __init__(self):
        self.nodes = defaultdict(Node)
        self.text = ""
        
class FileSystem(object):
    def __init__(self):
        self.root = Node()

    def find(self, path):
        cur = self.root
        if len(path)==1:
            return self.root
        for word in path.split("/")[1:]:
            cur = cur.nodes[word]
        return cur
        
    def ls(self, path):
        cur = self.find(path)
        if cur.text:
            return [path.split('/')[-1]]
        childs = cur.nodes.keys()
        return sorted(childs)
		
    def mkdir(self, path):
        self.find(path)

    def addContentToFile(self, filePath, content):
        cur = self.find(filePath)
        cur.text += content

    def readContentFromFile(self, filePath):
        cur = self.find(filePath)
        return cur.text