#Edimilton Ferreira

from binarytree import BinaryTree

class BinarySearchTree(BinaryTree):
        
    def __init__(self):
        super(BinarySearchTree, self).__init__()
        
    def clear(self):
        self.r = None

    def find(self, x):
        return self._find(x, self.r)

    def _find(self, x, u):
        if u == None: return False
        elif x == u.key: return True
        elif x < u.key: return self._find(x, u.left)
        else: return self._find(x, u.right)

    def add(self, x):
        self.r = self._add(x, self.r)
        return self.r   

    def _add(self, x, u):
        if u == None: return self._new_node(x)
        elif x < u.key: u.left = self._add(x, u.left)
        else: u.right = self._add(x, u.right)
        return u

    def _new_node(self, x):
        u = self.Node(x)
        return u
    
    def remove(self, x):
        if not self.find(x): return None
        self.r = self._remove(x, self.r)
        return self.r

    def _remove(self, x, u):
        if x > u.key: u.right = self._remove(x, u.right)
        elif x < u.key: u.left = self._remove(x, u.left)
        else :
              if u.left == None and u.right == None:
                  self._free(u)
                  return None
              elif u.left == None:
                  temp = u.right
                  self._free(u)
                  return temp
              elif u.right == None:
                  temp = u.left
                  self.free(u)
                  return temp
              else:
                  rightMin = self._getRightMin(u.right)
                  u.key = rightMin
                  u.right = self._remove(rightMin,u.right)
        return u

    def _free(self, u):
        u.key = u.left = u.right = u.parent = None

    def _getRightMin(self, u):
        temp = u
        while temp.left is not None:  
            temp = temp.left
        return temp.key

    def  menorValor(self, u):
      if u == None: return -10
      while u.left != None:
        u = u.left
      return u.key