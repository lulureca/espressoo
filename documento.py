class Pergunta1:
    def _init_(self):
        self.respostas = {
            "sim:": 18,
            "não:": 7,
            "não muito:": 5
        }

    def apresentar_dados(self):
        print("Você gosta de café?")
        for resposta, percentual in self.respostas.items():
            print(f"{resposta.capitalize()} {percentual}")


class Pergunta2:
    def _init_(self):
        self.respostas2 = {
            "1-3": 12,
            "3/mais": 5,
            "quase nunca": 7,
            "nenhuma das alternativas": 5
        }

    def apresentar_dados2(self):
        print("Com quanta frequência você toma café?")
        for resposta, percentual in self.respostas2.items():
            print(f"{resposta.capitalize()}: {percentual}")


class Pergunta3:
    def _init_(self):
        self.respostas3 = {
            "sim": 27,
            "não": 3
        }

    def apresentar_dados3(self):
        print("Você pode tomar café?")
        for resposta, percentual in self.respostas3.items():
            print(f"{resposta.capitalize()}: {percentual}")


class Pergunta4:
    def _init_(self):
        self.respostas4 = {
            "1-3": 15,
            "5/mais": 4,
            "3-5": 2,
            "nenhuma das alternativas": 8
        }

    def apresentar_dados4(self):
        print("Quantas xícaras de café você toma por dia?")
        for resposta, percentual in self.respostas4.items():
            print(f"{resposta.capitalize()}: {percentual}")


class Pergunta5:
    def _init_(self):
        self.respostas5 = {
            "açúcar": 17,
            "leite ou leite em pó": 3,
            "outros": 4,
            "não adoça": 4
        }

    def apresentar_dados5(self):
        print("Como você adoça seu café?")
        for resposta, percentual in self.respostas5.items():
            print(f"{resposta.capitalize()}: {percentual}")


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


def exibir_estatisticas(p1, p2, p3, p4, p5):
    media_p1 = calcular_media(p1.respostas)
    media_p2 = calcular_media(p2.respostas2)
    media_p3 = calcular_media(p3.respostas3)
    media_p4 = calcular_media(p4.respostas4)
    media_p5 = calcular_media(p5.respostas5)

    moda_p1 = calcular_moda(p1.respostas)
    moda_p2 = calcular_moda(p2.respostas2)
    moda_p3 = calcular_moda(p3.respostas3)
    moda_p4 = calcular_moda(p4.respostas4)
    moda_p5 = calcular_moda(p5.respostas5)

    mediana_p1 = calcular_mediana(p1.respostas)
    mediana_p2 = calcular_mediana(p2.respostas2)
    mediana_p3 = calcular_mediana(p3.respostas3)
    mediana_p4 = calcular_mediana(p4.respostas4)
    mediana_p5 = calcular_mediana(p5.respostas5)

    print(f"Média da Pergunta 1: {media_p1:.2f}")
    print(f"Moda da Pergunta 1: {', '.join(map(str, moda_p1))}")
    print(f"Mediana da Pergunta 1: {mediana_p1:.2f}")
    
    print(f"Média da Pergunta 2: {media_p2:.2f}")
    print(f"Moda da Pergunta 2: {', '.join(map(str, moda_p2))}")
    print(f"Mediana da Pergunta 2: {mediana_p2:.2f}")
    
    print(f"Média da Pergunta 3: {media_p3:.2f}")
    print(f"Moda da Pergunta 3: {', '.join(map(str, moda_p3))}")
    print(f"Mediana da Pergunta 3: {mediana_p3:.2f}")
    
    print(f"Média da Pergunta 4: {media_p4:.2f}")
    print(f"Moda da Pergunta 4: {', '.join(map(str, moda_p4))}")
    print(f"Mediana da Pergunta 4: {mediana_p4:.2f}")
    
    print(f"Média da Pergunta 5: {media_p5:.2f}")
    print(f"Moda da Pergunta 5: {', '.join(map(str, moda_p5))}")
    print(f"Mediana da Pergunta 5: {mediana_p5:.2f}")


def todas_as_respostas():
    p1 = Pergunta1()
    p2 = Pergunta2()
    p3 = Pergunta3()
    p4 = Pergunta4()
    p5 = Pergunta5()

    # Apresentar todas as respostas
    p1.apresentar_dados()
    print()
    
    p2.apresentar_dados2()
    print()
    
    p3.apresentar_dados3()
    print()
    
    p4.apresentar_dados4()
    print()
    
    p5.apresentar_dados5()
    print()

    # Exibir as estatísticas
    exibir_estatisticas(p1, p2, p3, p4, p5)

todas_as_respostas()
