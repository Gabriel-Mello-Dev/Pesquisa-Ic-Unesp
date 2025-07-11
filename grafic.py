from matplotlib import pyplot as plt
import numpy as np

import pandas as pd



temperaturaC= int(input("Qual a Temperatura da carne?: "))
phC= float(input("Qual o ph da carne?: "))
classeC= int(input("Qual a classe da carne?: "))
positivosC= int(input("Quantos testes positivos deram na carne?: "))
negativosC= int(input("Quantos testes negativos deram na carne?: "))

legenda = ['Temperatura', 'Ph', 'Classe social', 'positivos', 'negativos']
parametros = [temperaturaC, phC, classeC, positivosC, negativosC]

plt.bar(legenda, parametros, label="Carne moida", color="b")
plt.xlabel("Parâmetros")
plt.ylabel("Valores")
plt.title("Avaliação do Produto")
plt.legend()
plt.show()



temperaturaL= int(input("Qual a Temperatura da Linguiça?: "))
phL= float(input("Qual o ph da Linguiça?: "))
classeL= int(input("Qual a classe da Linguiça?: "))
positivosL= int(input("Quantos testes positivos deram na Linguiça?: "))
negativosL= int(input("Quantos testes negativos deram na Linguiça?: "))

legendaL = ['Temperatura', 'Ph', 'Classe social', 'positivos', 'negativos']
parametrosL = [temperaturaL, phC, classeL, positivosL, negativosL]

plt.bar(legendaL, parametrosL, label="Linguiça", color="r")
plt.xlabel("Parâmetros")
plt.ylabel("Valores")
plt.title("Avaliação do Produto")
plt.legend()
plt.show()
