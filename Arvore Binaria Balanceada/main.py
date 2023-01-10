#Edimilton Ferreira

from avltree import AvlTree 

tree = AvlTree()

tree.addAvl(10)
tree.addAvl(5)
tree.addAvl(13)
tree.addAvl(3)
tree.addAvl(4)
tree.addAvl(12)
tree.addAvl(8)
#tree.addAvl(1)
#tree.addAvl(2)

print(tree.removeAvl(10))

print('Percurso inOrder: ', end = '' )
tree.inOrder()
print()
print('Percurso preOrder: ', end = '' )
tree.preOrder()
print()
print('Percurso postOrder: ', end = '' )
tree.postOrder()
print()
print('Percurso postOrderIter: ', end = '' )
tree.postOrderIter()
print()
print(tree.menorValor(tree.r))

'''
ilustração da arvore apos as operacoes de adicao e remocao
'
'          5          
'    3          10
'     4      8     12
'                     13
'        
''' 