from matplotlib import pyplot as plt

# Função para plotar com valores no topo
def plot_grafico(titulo, labels, values, cor, y_lim):
    plt.figure(figsize=(10, 6))
    bars = plt.bar(labels, values, color=cor)
    plt.title(titulo, fontsize=20)
    plt.xlabel("Parâmetros", fontsize=18)
    plt.ylabel("Quantidade", fontsize=18)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.ylim(0, y_lim)  # Altura do eixo Y definida como 20

    # Adiciona os valores no topo das barras
    for bar in bars:
        altura = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, altura + 0.3, str(altura),
                 ha='center', va='bottom', fontsize=14)

    plt.tight_layout()
    plt.show()

# Dados Bovino atualizados
bovino_labels = [
    'Positivos para putrefação', 'Negativos para putrefação',
    'pH Fora do Padrão', 'Textura Ruim', 'Odor Ruim'
]
bovino_values = [6, 14, 11, 10, 4]

# Dados Suíno atualizados
suino_labels = [
    'Positivos para putrefação', 'Negativos para putrefação',
    'pH Fora do Padrão', 'Textura Ruim', 'Odor Ruim'
]
suino_values = [7, 13, 9, 8, 3]

# Plots com y_lim = 20
plot_grafico("Resultado da análise de carnes bovinas", bovino_labels, bovino_values, 'saddlebrown', y_lim=20)
plot_grafico("Resultado da análise de carnes suínas", suino_labels, suino_values, 'darkred', y_lim=20)
