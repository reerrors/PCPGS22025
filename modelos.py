# Arquivo: modelos.py

class Competencia:
    """Representa uma única competência (Soft Skill) e sua pontuação."""
    def __init__(self, nome, pontuacao):
        self.nome = nome
        self.pontuacao = pontuacao # 1 a 5

    def __str__(self):
        return f"{self.nome}: {self.pontuacao}/5"


class Perfil:
    """Representa o usuário e suas características agregadas."""
    def __init__(self, nome):
        self.nome = nome
        self.competencias = {} 
        self.media_geral = 0.0

    def adicionar_competencia(self, competencia):
        self.competencias[competencia.nome] = competencia

    def calcular_media(self):
        if not self.competencias:
            return 0
        soma = sum(c.pontuacao for c in self.competencias.values())
        self.media_geral = soma / len(self.competencias)
        return self.media_geral