#Edimilton Ferreira

from arraystack import ArrayStack
from binarysearchtree import BinarySearchTree

class AvlTree(BinarySearchTree):
  
    def __init__(self):
        super(AvlTree, self).__init__()
    
    def addAvl(self, x):
        self.add(x)
        fatorBal = self._getFatorBal(self.r)
        if abs(fatorBal) > 1:
          self.r = self._balance(self.r, fatorBal)
        return self.r
    
    def removeAvl(self, x):
        self.remove(x)
        fatorBal = self._getFatorBal(self.r)
        if abs(fatorBal) > 1: 
          self.r = self._balance(self.r, fatorBal)
        return self.r

    def _getFatorBal(self, u):
        if u == None: return 0
        return self._height(u.left) - self._height(u.right)
    
    def _balance(self, u, fator):
        if fator > 1:
          if self._getFatorBal(u.left) >= 0:
            return self.rightRotate(u) 
          else:
            u.left = self.leftRotate(u.left)
            return self.rightRotate(u)
        if fator < -1:
          if self._getFatorBal(u.right) <= 0: 
            return self.leftRotate(u)
          else:
            u.right = self.rightRotate(u.right)
            return self.leftRotate(u)

    def leftRotate(self, z):
        y = z.right
        z.right = y.left
        y.left = z
        return y

    def rightRotate(self, z):
        y = z.left
        z.left = y.right
        y.right = z
        return y
    
    def postOrderIter(self):
        if self.r is None: return None
        stackMain = ArrayStack()
        stackMain.push(self.r)
        stackAux = ArrayStack()

        while stackMain.n != 0:
            u = stackMain.pop()
            stackAux.push(u)

            if u.left is not None:
                stackMain.push(u.left)

            if u.right is not None:
                stackMain.push(u.right)

        while stackAux.n != 0:
            u = stackAux.pop()
            print(u.key, end = ' ')


'''
ilustração da arvore apos as operacoes de adicao e remocao
'
'          5          
'    0          9
' -1   1      6   11
'        2
'
' stackMain        stackAux
'    ||              ||
'    ||              ||
'    ||              ||
'    ||              ||
'    ||              ||
'    ||              ||
'    ||              ||
'    ||              ||
''' 