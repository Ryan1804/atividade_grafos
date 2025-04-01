# -*- coding: utf-8 -*-
import queue
from collections import deque

class Graph:
    def __init__(self, n):
        self.num_vertices = n
        self.M = [[0 for _ in range(n)] for _ in range(n)]
        self.L = [ [] for _ in range(n)]

    def print(self):
        print("Número de Vértices: " + str(self.num_vertices))
        print("Matriz de adjacência:")
        print(self.M)
        print("Lista de Adjacência:")
        print(self.L)
    
    def num_comp(self):
        pred = self.dfs()
        num = 0
        for v in range(self.num_vertices):
            if(pred[v] == -1):
                num += 1
        return num
    
    def dfs(self, source):
        pred = [-1 for _ in range(self.num_vertices)]
        visitados = [False for _ in range(self.num_vertices)]
        pilha = deque()             #criando a pilha para a dfs

        pilha.append(source)
        visitados[source] = True    #vertice fonte para a dfs é adicionado a pilha e marcado como visitado

        while(len(pilha) != 0):     
            v = pilha.pop()         #enquanto a pilha nao estiver vazia remove o primeiro vertice e vai
                                    #até um vertice terminal a partir do vertice removido da pilha
                                    #adicionando a pilha os vertices nao buscados
            for u in self.L[v]:
                if(visitados[u] == False):
                  pilha.append(u)
                  visitados[u] = True
                  pred[u] = v
                
        return pred
        
    def bfs(self, source):
        visitados = [False for _ in range(self.num_vertices)]
        pred = [-1 for _ in range(self.num_vertices)]
        D = [-1 for _ in range(self.num_vertices)]
        Q = queue.Queue()
        Q.put(source)
        visitados[source] = True
        D[source] = 0
        
        while(Q.empty() == False):
            v = Q.get()
            print("Vertice:" + str(v))
            for u in self.L[v]:
                if(visitados[u] == False):
                    Q.put(u)
                    visitados[u] = True
                    D[u] = D[v] + 1
                    pred[u] = v
        
        return D, pred
    
    def print_caminho(self, s, t):
        D, pred = self.bfs(s)

        if(D[t] == -1):                                 #verificando se há caminho entre os vertices
            print("não há caminho entre os vértices")
            return

        caminho = []
        passo = t                                       #comecando pela vertice final                                       

        while(passo != -1):                             #achando o caminho da vertice final para a inicial
            caminho.append(passo)
            passo = pred[passo]

        caminho.reverse()                               #caminho agora da vertice inicial para a final

        print("Caminho:", caminho)

