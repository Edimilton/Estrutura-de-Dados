from binaryheap import BinaryHeap

arv = BinaryHeap()

arv.addHeap(5, 'um')
arv.addHeap(4, 'dois')
arv.addHeap(9, 'tres')
arv.addHeap(10, 'quatro')
arv.addHeap(14, 'cinco')
arv.addHeap(20, 'seis')
arv.addHeap(17, 'sete')

for i in range(arv.n):
  print(arv.a[i].key)


'''
ilustração da arvore
'
'          4          
'    5          9
' 10   14      
'        
''' 
'''
'         20          
'      10      17
'    4    9   5  14  
'''