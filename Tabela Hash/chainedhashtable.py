"""A Set implementation that uses hashing with chaining"""
import random

from utils import new_array
from arraystack import ArrayStack
from base import BaseSet

w = 32

class ChainedHashTable(BaseSet):
    def __init__(self, m, iterable=[]):
        self._initialize(m)
        self.add_all(iterable)
        
    def _initialize(self, m):
        self.d = m
        self.t = self._alloc_table((1<<self.d))
        self.z = self._random_odd_int()
        self.n = 0

    def _random_odd_int(self):
        return random.randrange(1<<w) | 1
            
    def clear(self):
        self.d = 1
        self.t = self._alloc_table((1<<self.d))
        self.n = 0
        
    def _alloc_table(self, s):
        return [ArrayStack() for _ in range(s)]
    
    def _resize(self):
        self.d = 1
        while (1 << self.d) <= self.n: self.d += 1
        self.n = 0
        old_t = self.t
        self.t = self._alloc_table(1<<self.d)
        for i in range(len(old_t)):
            for x in old_t[i]:
                self.add(x)
    
    def _hash(self, x):
        sum = 0
        for i in range(len(x)):
          sum = sum + (ord(x[i]) * 263**i)
        position = (sum % 1000000007) % self.d
        return position
    
    def add(self, x):
        if self.find(x) is not None: return False
        if self.n+1 > len(self.t): self._resize()
        self.t[self._hash(x)].append(x)
        self.n += 1
        return True
    
    def remove(self, x):
        ell = self.t[self._hash(x)]
        for y in ell:
            if y == x:
                ell.remove_value(y)
                self.n -= 1 
                return y
        return None 
        
    def find(self, x):
        for y in self.t[self._hash(x)]:
            if y == x:
                return y
        return None
    
    def check(self, i):
        return self.t[i]
    
    def __iter__(self):
        for ell in self.t:
            for x in ell:
                yield x
                
        


    