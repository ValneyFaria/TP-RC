# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 04:27:08 2020

@author: ygorm
"""

from igraph import *

g = Graph.Read_GML("covid_04_11.gml")


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

print( g.vs['label'],g.evcent())
print("porcentagem e IDH")
print(g.vs["porcentagem"])
VetorCent = g.vs["porcentagem"]
VetorCity = g.vs["label"]
VetorIdh = g.vs["IDH"]
print("Top 20 cidades")
print("Rank Nome porcetagem IDH")
for item in range(20):
    print(item+1,VetorCity[VetorCent.index(max(VetorCent))],round(max(VetorCent)/10,3),VetorIdh[VetorCent.index(max(VetorCent))])
    del(VetorCity[VetorCent.index(max(VetorCent))])
    del(VetorIdh[VetorCent.index(max(VetorCent))])
    del(VetorCent[VetorCent.index(max(VetorCent))])
