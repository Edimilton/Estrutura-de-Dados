# Edimilton Ferreira

R = 26

class TrieNode:
  def __init__(self):
    self.children = [None]*R
    self.val = 0
    self.isEndOfWord = False

class Trie:
  def __init__(self):
      self.root = self.getNode()

  def getNode(self):
      return TrieNode()
    
  def _charToIndex(self,ch):
      return ord(ch)-ord('a')
    
  def insert(self,key):
      key.lower()
      pCrawl = self.root
      length = len(key)
      for level in range(length):
          index = self._charToIndex(key[level])
          if not pCrawl.children[index]:
              pCrawl.children[index] = self.getNode()
          pCrawl = pCrawl.children[index]
      pCrawl.val += 1
      pCrawl.isEndOfWord = True

  def search(self, key):	
      pCrawl = self.root
      length = len(key)
      for level in range(length):
          index = self._charToIndex(key[level])
          if not pCrawl.children[index]:
              return False
          pCrawl = pCrawl.children[index]
      return pCrawl.isEndOfWord
  
  def word_Counter(self, key):
      pCrawl = self.root
      length = len(key)
      for level in range(length):
          index = self._charToIndex(key[level])
          if not pCrawl.children[index]:
              return 0
          pCrawl = pCrawl.children[index]
      return pCrawl.val

  def keysWithPrefix(self, pre):
      wordList = []
      self.collect(self.get(pre), pre, wordList)
      return wordList

  def collect(self, u, pre, wordList):
    if u == None: return None
    if u.isEndOfWord:
        wordList.append(pre)
    for c in range(26):
          self.collect(u.children[c] , pre + chr(ord('a') + c) , wordList)
  
  def get(self, pre):
      pCrawl = self.root
      length = len(pre)
      for level in range(length):
          index = self._charToIndex(pre[level])
          if not pCrawl.children[index]:
              return None
          pCrawl = pCrawl.children[index]
      return pCrawl

  
