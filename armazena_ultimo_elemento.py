import numpy as np  # Importa a biblioteca NumPy, que é usada para operações eficientes com arrays

# Define um array NumPy 2D onde cada linha representa um cliente e as colunas representam diferentes atributos dos clientes
clientes = np.array([[1, 'João', 30, 'Rua A', 100, 'eletrônicos'],
                     [2, 'Maria', 25, 'Rua B', 200, 'moda'],
                     [3, 'Pedro', 35, 'Rua C', 50, 'esportes']])

# Extrai todas as colunas a partir da quinta coluna (índice 4) até o final, ou seja, as intenções de compras
intencao_compras = clientes[:, 4:]

# Imprime o array contendo as intenções de compras
print(intencao_compras)

# Outra forma de extrair as intenções de compras: aqui especificamos as colunas da quinta até a sexta (índices 4 e 5)
intencao_compras = clientes[:, 4:6]

# Imprime o array contendo as intenções de compras
print(intencao_compras)
