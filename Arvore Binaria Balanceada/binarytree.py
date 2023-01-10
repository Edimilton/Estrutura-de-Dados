#Edimilton Ferreira

from arrayqueue import ArrayQueue

class BinaryTree():
  
    class Node():
        def __init__(self, key):
            self.key = key
            self.left = self.right = self.parent = None

    def __init__(self):
        self.r = None
        
    def depth(self, u):
        d = 0
        while (u != self.r):
            u = u.parent
            d += 1
        return d
    
    def size(self):
        return self._size(self.r)
    
    def _size(self, u):
        if u is None: return 0
        return 1 + self._size(u.left) + self._size(u.right)
    
    def height(self):
        return self._height(self.r)
    
    def _height(self, u):
        if u is None: return -1 
        return 1 + max(self._height(u.left), self._height(u.right))
    
    def inOrder(self):
        return self._inOrder(self.r)

    def _inOrder(self, u):
        if u is None: return
        self._inOrder(u.left) 
        print(u.key, end = ' ')
        self._inOrder(u.right)

    def preOrder(self):
        return self._preOrder(self.r)

    def _preOrder(self, u):
        if u is None: return
        print(u.key, end = ' ')
        self._preOrder(u.left) 
        self._preOrder(u.right)
    
    def postOrder(self):
        return self._postOrder(self.r)

    def _postOrder(self, u):
        if u is None: return
        self._postOrder(u.left) 
        self._postOrder(u.right)
        print(u.key, end = ' ')

    def bf(self):
        queue = ArrayQueue()
        if self.r is not None: queue.add(self.r)
        while queue.n != 0:
            u = queue.remove()
            print(u.key, end = ' ')
            if u.left is not None: queue.add(u.left)
            if u.right is not None: queue.add(u.right)
