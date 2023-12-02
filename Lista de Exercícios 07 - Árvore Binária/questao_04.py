# 4. Imagine uma árvore binária representando uma árvore genealógica.
# Cada nó possui informações sobre um membro da família.
# Desenvolva um código em Python para criar e imprimir essa árvore.

from arvore import No, ArvoreBinaria

arvore_genealogica = ArvoreBinaria()

raiz = No("Filho")
raiz.esquerda = No("Mãe")
raiz.direita = No("Pai")
raiz.esquerda.esquerda = No("Avó Materna")
raiz.esquerda.direita = No("Avô Materno")
raiz.direita.esquerda = No("Avó Paterna")
raiz.direita.direita = No("Avô Paterno")

arvore_binaria = ArvoreBinaria()
arvore_binaria.raiz = raiz

arvore_binaria.post_order_traversal()
