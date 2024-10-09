import matplotlib.pyplot as plt

class Pergunta:
    def _init_(self, titulo, respostas, cor):
        self.titulo = titulo
        self.respostas = respostas
        self.cor = cor

    def apresentar_dados(self):
        print(self.titulo)
        for resposta, percentual in self.respostas.items():
            print(f"{resposta.capitalize()}: {percentual}")

    def plotar_grafico(self, media, moda, mediana):
        plt.figure(figsize=(8, 6))
        plt.bar(self.respostas.keys(), self.respostas.values(), color=self.cor)
        plt.title(self.titulo)
        plt.xlabel("Respostas")
        plt.ylabel("Quantidade")
        
        # Adicionando estatísticas ao gráfico
        plt.axhline(y=media, color='r', linestyle='--', label=f'Média: {media:.2f}')
        plt.axhline(y=moda[0], color='g', linestyle='--', label=f'Moda: {", ".join(map(str, moda))}')
        plt.axhline(y=mediana, color='b', linestyle='--', label=f'Mediana: {mediana:.2f}')
        plt.legend()
        
        plt.show()


def calcular_media(respostas):
    return sum(respostas.values()) / len(respostas)


def calcular_moda(respostas):
    valores = list(respostas.values())
    frequencias = {x: valores.count(x) for x in valores}
    moda = [k for k, v in frequencias.items() if v == max(frequencias.values())]
    return moda


def calcular_mediana(respostas):
    valores = sorted(respostas.values())
    n = len(valores)
    meio = n // 2
    if n % 2 == 0:
        return (valores[meio - 1] + valores[meio]) / 2
    else:
        return valores[meio]


def exibir_estatisticas(p):
    media = calcular_media(p.respostas)
    moda = calcular_moda(p.respostas)
    mediana = calcular_mediana(p.respostas)
    
    p.apresentar_dados()
    print(f"Média: {media:.2f}")
    print(f"Moda: {', '.join(map(str, moda))}")
    print(f"Mediana: {mediana:.2f}")
    p.plotar_grafico(media, moda, mediana)


def todas_as_respostas():
    perguntas = [
        Pergunta("Você gosta de café?", {"sim": 18, "não": 7, "não muito": 5}, "blue"),
        Pergunta("Com quanta frequência você toma café?", {"1-3": 12, "3 ou mais": 5, "quase nunca": 7, "nenhuma das alternativas": 5}, "green"),
        Pergunta("Você pode tomar café?", {"sim": 27, "não": 3}, "orange"),
        Pergunta("Quantas xícaras de café você toma por dia?", {"1-3": 15, "5 ou mais": 4, "3-5": 2, "nenhuma das alternativas": 8}, "purple"),
        Pergunta("Como você adoça seu café?", {"açúcar": 17, "leite ou leite em pó": 3, "outros": 4, "não adoça": 4}, "cyan"),
    ]

    for pergunta in perguntas:
        exibir_estatisticas(pergunta)


# Chama a função para exibir os dados e as estatísticas
todas_as_respostas()