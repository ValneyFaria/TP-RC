# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 04:27:08 2020

@author: ygorm
"""

from igraph import *

g = Graph.Read_GML("covid_31_07.gml")


# Caracteristicas Basicas
print("Numero de vertices:", g.vcount())
print("Numero de arestas:", g.ecount())
print("Densidade:", g.density())
somaMedia = sum(g.degree())
Media = somaMedia/g.vcount()
print("Grau Médio:", Media)
print("Coeficiente de Cluterização médio:", g.transitivity_undirected())

# Visualização da rede
lay = g.layout_drl()
plot(g, bbox=(800, 600), layout=lay, vertex_size=g.vs["porcentagem"]).show()

# Distribuição de Graus
print("Graus:")
print(g.degree())
# plot(g, bbox=(800, 600),  layout=lay).show()

# Centralidade
print("Centralidade")
print(g.evcent())
VetorCent = g.evcent()
print("Top 20 centralidade")
print("Rank Nome Centralidade")
for item in range(20):
    print(item+1, g.vs['label']
          [VetorCent.index(max(VetorCent))], max(VetorCent))
    del(VetorCent[VetorCent.index(max(VetorCent))])
