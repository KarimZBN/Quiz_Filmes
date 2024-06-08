import json
import random
from collections import defaultdict

class QuizLogic:
    def __init__(self, perguntas):
        self.perguntas_completas = perguntas
        self.perguntas = self.selecionar_perguntas()
        self.current_question = 0
        self.respostas = []
        self.filmes = self.carregar_filmes('filmes.json')

    @staticmethod
    def carregar_perguntas(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    @staticmethod
    def carregar_filmes(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def selecionar_perguntas(self):
        perguntas_por_genero = defaultdict(list)
        for pergunta in self.perguntas_completas:
            for genero in pergunta['generos']:
                perguntas_por_genero[genero].append(pergunta)

        perguntas_selecionadas = []
        generos = list(perguntas_por_genero.keys())
        num_generos = len(generos)
        num_perguntas_por_genero = 20 // num_generos

        for genero in generos:
            perguntas_selecionadas.extend(random.sample(perguntas_por_genero[genero], min(num_perguntas_por_genero, len(perguntas_por_genero[genero]))))

        # Se não atingiu o número total desejado, completar com perguntas aleatórias
        while len(perguntas_selecionadas) < 20:
            perguntas_selecionadas.append(random.choice(self.perguntas_completas))

        random.shuffle(perguntas_selecionadas)
        return perguntas_selecionadas

    def responder(self, resposta):
        self.respostas.append(resposta)
        self.current_question += 1
        return self.current_question < len(self.perguntas)

    def voltar_pergunta(self):
        if self.current_question > 0:
            self.current_question -= 1
            self.respostas.pop()
        return self.current_question > 0

    def get_pergunta(self):
        return self.perguntas[self.current_question]

    def calcular_pontuacao(self):
        generos = {
            'ação': 0,
            'comédia': 0,
            'drama': 0,
            'ficção': 0,
            'terror': 0,
            'romance': 0,
            'comédia-romântica': 0,
            'fantasia': 0,
            'musical': 0,
            'aventura': 0,
            'documentário': 0,
            'mistério': 0
        }
        contagem_generos = {genero: 0 for genero in generos}

        for resposta, pergunta in zip(self.respostas, self.perguntas):
            valor = self.valor_resposta(resposta)
            for genero in pergunta['generos']:
                generos[genero] += valor
                contagem_generos[genero] += 1

        return generos, contagem_generos

    @staticmethod
    def valor_resposta(resposta):
        valores = {
            'Amo': 2,
            'Gosto': 1,
            'Indiferente': 0,
            'Não Gosto': -1,
            'Detesto': -2
        }
        return valores.get(resposta, 0)

    @staticmethod
    def calcular_porcentagens(pontuacao, contagem_generos):
        porcentagens = {}
        for genero, pontuacao_genero in pontuacao.items():
            total_perguntas_genero = contagem_generos[genero]
            if total_perguntas_genero > 0:
                porcentagem = (pontuacao_genero / (2 * total_perguntas_genero)) * 100
                porcentagens[genero] = max(porcentagem, 0)  # Garantir que a porcentagem não seja negativa
            else:
                porcentagens[genero] = 0
        return porcentagens