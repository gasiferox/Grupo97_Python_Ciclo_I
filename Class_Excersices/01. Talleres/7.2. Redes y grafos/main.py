""" Programa grafos

    Oscar Franco-Bedoya
    Junio 2-2021 """

#---------------- Zona librerias------------


#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================

#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación (Conquistar)
# =====================================================================


import networkx as nx
import os
import matplotlib.pyplot as plt

#then set the 'MPLCONFIGDIR' to '/tmp'

os.environ['MPLCONFIGDIR'] = '/home/runner/72-Redes-y-grafos'

G = nx.Graph() # Creación de un grafo no dirigido
# Adicion de nodos individuales
G.add_node("espinaca")
G.add_node("espárragos")
G.add_node("frijoles")
G.add_node("papas")
G.add_node("zanahorias")
G.add_node("carne")
G.add_node("tomates")

# Adicion de una coleccion de nodos
G.add_nodes_from(["vitamina A", "Acido Fólico", "vitamina B6", "Calcio", "Zinc","Niacina", "vitamina C", "Riboflavina", "vitamina B12", "Selenio" ])

G.add_edge("espinaca", "Acido Fólico")
G.add_edge("espárragos", "vitamina B6")
G.add_edge("espárragos", "Acido Fólico")
G.add_edge("frijoles", "vitamina B6")
G.add_edge("frijoles", "Calcio")
G.add_edge("papas", "vitamina B6")
G.add_edge("papas", "Zinc")
G.add_edge("papas", "Selenio")

# Adicion desde una lista de ejes
G.add_edges_from([("zanahorias", "vitamina C"), ("zanahorias", "vitamina A"),
                  ("carne", "vitamina B12"), ("carne", "Niacina"), ("carne", "Zinc"),
                  ("carne", "Riboflavina"),("tomates", "vitamina C"), ("tomates", "vitamina A")])

print(G.edges()) #Imprime la lista de ejes
print(G.nodes()) #Imprime la lista de nodos

nx.draw(G, with_labels=True).sho # grafico por defectocd..
plt.show()
