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
    
    def dfs(self):
        pred = [-1 for _ in range(self.num_vertices)]
        visitados = [False for _ in range(self.num_vertices)]
        pilha = deque()                     #criando a pilha para a dfs

        for v in range(self.num_vertices):  #itera sobre todos os vertices do grafo
            if(visitados[v] == False):      #se um vertice nao foi visitado e empilhado e marcado como visitado
                pilha.append(v)
                visitados[v] = True

            while pilha:     
                u = pilha.pop()             #executa busca no vertice topo da pilha, empilhando seus adjacentes
                                            #para que sejam buscados e guarda seus predecessores
                for vizinho in self.L[u]:
                    if(visitados[vizinho] == False):
                        pilha.append(vizinho)
                        visitados[vizinho] = True
                        pred[vizinho] = u
                
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

