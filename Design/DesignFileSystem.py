from collections import defaultdict

class PathNode:
    def __init__(self):
        self.childs = defaultdict(PathNode)
        self.value = None

class FileSystem:
    def __init__(self):
        self.root = PathNode()
        return

    def createPath(self, path: str, value: int) -> bool:
        paths = path.split("/")
        cur = self.root
        N = len(paths)
        for i in range(1, N-1):
            p = paths[i]
            if p in cur.childs:
                cur = cur.childs[p]
            else:
                return False # parent not exists

        if paths[N-1] in cur.childs:
            return False # path existed
        cur.childs[paths[N-1]].value = value
        return True

    def get(self, path: str) -> int:
        paths = path.split("/")
        cur = self.root
        N = len(paths)
        for i in range(1, N):
            p = paths[i]
            if p in cur.childs:
                cur = cur.childs[p]
            else:
                return -1 # parent not exists
        return cur.value