class Node():
  def __init__(self):
    self.key = None
    self.val = None

class BinaryHeap():
  
  def __init__(self):
    self.a = []
    self.n = 0
  
  def left(self,i):
    return (2 * i) + 1

  def right(self, i):
    return 2 * (i + 1)

  def parent(self, i):
    return int((i - 1)/ 2)
  
  def newNode(self):
    return Node()

  def addHeap(self, key, val):
    x = self.newNode()
    x.key = key
    x.val = val
    self.a.append(x)
    self.n += 1
    self.bubble_up(self.n - 1)
    return True 

  def bubble_up(self,i):
    p = self.parent(i)
    while i > 0 and self.a[i].key > self.a[p].key:
      self.a[i], self.a[p] = self.a[p], self.a[i]
      i = p
      p = self.parent(i)
  
  def removeHeap(self):
    root = self.a[0]
    self.a[0] = self.a[self.n - 1]
    self.n -= 1
    self.trickle_down(0)
    return root

  def trickle_down(self,i):
    while i >= 0:
      j = -1
      r = self.right(i)
      
      if r < self.n and self.a[r].key > self.a[i].key:
        l = self.left(i)
        if self.a[l].key > self.a[r].key:
          j = l
        else:
          j = r
      
      else:
        l = self.left(i)
        if l < self.n and self.a[l].key > self.a[i].key:
          j = l

      if j >= 0 :
        self.a[j],self.a[i] = self.a[i], self.a[j]
      i = j
