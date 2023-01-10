# Edimilton Ferreira

from trie import Trie
from binaryheap import BinaryHeap

# captura das palavras do arquivo 

with open("article.txt", "r") as article:
  article = article.read().split()

trie = Trie()

for word in article:
  trie.insert(word)

# captura dos valores e chaves

vals = []

for c in range(26):
  wordsList = (trie.keysWithPrefix(chr(ord('a') + c)))
  for w in wordsList:
    vals.append(w)

keys = []

for w in vals:
  keys.append(trie.word_Counter(w))

# adicionando as chaves e valores na trie

heap = BinaryHeap()

for i in range(len(keys)):
  heap.addHeap(keys[i], vals[i])

# ordenacao pela chave

heap.heapsort()

#main

def main():
	# contagem de palavras
  print("contagem de palavras:")
  print("{} ---- {}".format("dados",trie.word_Counter("dados")))
  print("{} ---- {}".format("imagens",trie.word_Counter("imagens")))
  print("{} ---- {}".format("imag",trie.word_Counter("imag")))
  print("{} ---- {}".format("jogo",trie.word_Counter("jogo")))
  
  # listar palavras com prefixo
  print("\nlistar palavras com prefixo:")
  print("{} ---- {}".format("comp",trie.keysWithPrefix("comp")))
  print("{} ---- {}".format("imag",trie.keysWithPrefix("imag")))
  print("{} ---- {}".format("de",trie.keysWithPrefix("de"))) 
  print("{} ---- {}".format("pr",trie.keysWithPrefix("pr")))
  
  # listagem ordenada pela chave
  print("\nlistagem ordenada pela chave:")
  for i in range(heap.n):
    print(heap.a[i].key, end =' : ')
    print(heap.a[i].val)


if __name__ == '__main__':
	main()