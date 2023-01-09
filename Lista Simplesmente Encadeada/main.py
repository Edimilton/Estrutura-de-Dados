# EDIMILTON FERREIRA

import time
#import random
from sllist import SLList

# Creating new variables sllist

list01 = SLList()
list02 = SLList()

input01 = input()
for n in input01:
  num = int(n)
  list01.push(num)

input02 = input()
for n in input02:
  num = int(n)
  list02.push(num)


# function to sum sllist

def sumSL(less, more):
  nextM = more.head
  nextL = less.head

  while nextM is not None:
    result = nextM.x + nextL.x

    if result < 10:
      nextM.x = result

    else:
      nextM.x = result - 10

      if nextM.next is not None:
        nextM.next.x += 1
      else:
        more.append(1)

    nextM = nextM.next

    if nextL.next is not None:
      nextL = nextL.next
    else:
      nextL.x = 0
      if nextM is None or nextM.x < 10: 
        break      


# function to reverse sllist

def reverseSL(listSL):
    prev = None
    current = listSL.head
    listSL.tail = listSL.head

    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next

    listSL.head = prev
    

# function to print sllist

def printSL(listSL):
  reverseSL(listSL)
  for n in listSL:
    print(n, end = "")
  print("\n")


# function call

if list01.n > list02.n:
  start = time.time()
  sumSL(list02, list01)
  stop = time.time() - start
  printSL(list01)

else:
  start = time.time()
  sumSL(list01, list02)
  stop = time.time() - start
  printSL(list02)

print("the runtime is: " + str(stop))


# function to time analysis (always in the worst case)

'''
n = [100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000]
tempo = []
l = SLList()
for e in range(0,len(n)):
    l = SLList()
    m = SLList()
    for _ in range(n[e]):
        l._add(random.randint(0, 10))
        m._add(random.randint(0, 10))
    start = time.time()
    sumSL(l, m)
    stop = time.time() - start
    tempo.append(stop)

print(n)
print(tempo)
'''

# asymptotic analysis

'''
OMEGA(1): Omega sera constante para qualquer caso em que a lista menor é unitaria e nao sobra 1 da soma anterior para o proximo elemento da lista maior.

TETA(i): O algorito geralmente ira depender da quantidade de elementos da lista menor, exceto quando sobra 1 da soma anterior, nesse caso pode chegar até n.

O(n): Nos casos onde as listas possuem o mesmo tamanho ou e necessario somar ate o ultimo elemento da lista maior.
'''

# time analysis in replit

'''
size: [100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000]

time: [0.13787174224853516, 0.2263166904449463, 0.43760228157043457, 0.6793382167816162, 0.8375513553619385, 0.9180986881256104, 1.7999675273895264, 2.0864858627319336, 2.014291763305664, 2.414057970046997]
'''