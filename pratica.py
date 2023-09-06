class No:
    def __init__(self,valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None
    
    def __repr__(self):
        return '%s <-- %s --> %s' %(self.esquerda and self.esquerda.valor, self.valor , self.direita and self.direita.valor)
    
class arvoreBinaria:
    def __init__(self):
        self.raiz = None
    
    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self._inserir_recursivo(valor,self.raiz)
    
    def _inserir_recursivo(self,valor,no):
        if valor < no.valor:
            if no.esquerda is None:
                no.esquerda = No(valor)
            else:
                self._inserir_recursivo(valor, no.esquerda)
        else:
            if no.direita is None:
                no.direita = No(valor)        
            else:
                self._inserir_recursivo(valor, no.direita)
                
    def mostrar_pre_ordem(self):
        if self.raiz is None:
            print('A árvore está vazia!') 
        else:
            self.mostrar_pre_ordem_recursiva(self.raiz)
        
    def mostrar_pre_ordem_recursiva(self,no):
        print(no.valor, end=' ')
        if no.esquerda is not None:
            self.mostrar_pre_ordem_recursiva(no.esquerda)
        if no.direita  is not None:
            self.mostrar_pre_ordem_recursiva(no.direita)
    
    
    def mostrarRaiz (self):
        if self.raiz is None:
            return None
        else:
            return self.raiz.valor
    
    def altura(self):
        return self._altura_recursivo(self.raiz)

    def _altura_recursivo(self, no):
        if no is None:
            return -1
        altura_esquerda = self._altura_recursivo(no.esquerda)
        altura_direita = self._altura_recursivo(no.direita)
        return max(altura_esquerda, altura_direita) + 1
    
    def buscar(self, valor):
        if self._buscar_recursivo(valor, self.raiz):
            return print('O número digitado está na árvore!')
        else:
            return print('O número digitado não está na árvore!')
    
    def _buscar_recursivo(self,valor,no):
        if no is None:
            return False
        if valor == no.valor:
            return True
        elif valor < no.valor:
            return self._buscar_recursivo(valor, no.esquerda)
        else:
            return self._buscar_recursivo(valor, no.direita)
        
    def mostrar_nos_internos(self):
        if self.raiz is None:
            print('A árvore está vazia!')
        else:
            self.mostrar_nos_internos_recursivo(self.raiz)
            print()  # Adicionado para nova linha após exibição

    def mostrar_nos_internos_recursivo(self, no):
        if no:
            if no.esquerda or no.direita:
                print(no.valor, end=' ')
            self.mostrar_nos_internos_recursivo(no.esquerda)
            self.mostrar_nos_internos_recursivo(no.direita)

    def mostrar_folhas(self):
        if self.raiz is None:
            print('A arvore está vazia!')
        else:
            self.mostrar_folhas_recursivo(self.raiz)
            print()  # Adicionado para nova linha após exibição

    def mostrar_folhas_recursivo(self, no):
        if no:
            if not no.esquerda and not no.direita:
                print(no.valor, end=' ')
            self.mostrar_folhas_recursivo(no.esquerda)
            self.mostrar_folhas_recursivo(no.direita)
    

#TESTE 
arvore = arvoreBinaria()

numNos = int(input('Digite o número de nós: '))
print("\n")
#Valores do Nos: 4 2 6 1 3 5 7
for i in range(numNos):
    valor = int(input('Digite o valor do nó: '))
    arvore.inserir(valor)

print('\nPré Ordem:')
arvore.mostrar_pre_ordem()
print('\n\nRaiz:', arvore.mostrarRaiz())
print('\nAltura:', arvore.altura())
print('\nNós internos: ')
arvore.mostrar_nos_internos()
print('\nFolhas: ')
arvore.mostrar_folhas()

valorBusca = int(input('\nDigite um número para busca: '))
arvore.buscar(valorBusca)

