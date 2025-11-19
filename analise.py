# Arquivo: analise.py

class AnalisadorDeSoftSkills:
    """Responsável por processar os dados e gerar recomendações."""

    NIVEIS = ("Iniciante", "Em desenvolvimento", "Intermediário", "Avançado", "Expert")

    def __init__(self):
        # Base de conhecimento (Dicionário)
        self.base_conhecimento = {
            "Comunicação": {
                "baixa": "Pratique escuta ativa e tente estruturar suas ideias antes de falar.",
                "alta": "Você pode atuar como mentor ou porta-voz em projetos."
            },
            "Liderança": {
                "baixa": "Comece assumindo pequenas responsabilidades e iniciativas no time.",
                "alta": "Foque em desenvolver novos líderes e gestão estratégica."
            },
            "Resiliência": {
                "baixa": "Tente ver erros como aprendizado e não leve críticas para o lado pessoal.",
                "alta": "Ajude colegas a manterem a calma em momentos de crise."
            },
            "Trabalho em Equipe": {
                "baixa": "Busque entender o papel dos outros e ofereça ajuda proativamente.",
                "alta": "Excelente! Foque em facilitar a colaboração entre áreas diferentes."
            },
            "Criatividade": {
                "baixa": "Exercite o pensamento lateral. Resolva problemas antigos de formas novas.",
                "alta": "Use sua criatividade para inovação de processos, não apenas ideias."
            }
        }

    def analisar_competencia(self, competencia):
        """Gera um feedback específico para uma competência."""
        nivel_idx = competencia.pontuacao - 1
        nivel_texto = self.NIVEIS[nivel_idx]
        
        if competencia.pontuacao <= 2:
            dica = self.base_conhecimento.get(competencia.nome, {}).get("baixa", "Busque cursos introdutórios.")
            status = "Ponto de Atenção"
        elif competencia.pontuacao == 3:
            dica = "Você está na média. A prática constante o levará ao próximo nível."
            status = "Em evolução"
        else:
            dica = self.base_conhecimento.get(competencia.nome, {}).get("alta", "Continue assim!")
            status = "Ponto Forte"

        return {
            "skill": competencia.nome,
            "nota": competencia.pontuacao,
            "nivel": nivel_texto,
            "status": status,
            "recomendacao": dica
        }

    def gerar_norte_carreira(self, perfil):
        """Define um arquétipo básico baseado nas maiores notas."""
        fortes = [c.nome for c in perfil.competencias.values() if c.pontuacao >= 4]
        
        print(f"\n--- PROFILE: {perfil.nome} ---")
        
        if "Liderança" in fortes and "Comunicação" in fortes:
            print(">> Perfil sugerido: Gestão/Liderança.")
            print("   Invista em metodologias ágeis e gestão de pessoas.")
        elif "Criatividade" in fortes and "Resiliência" in fortes:
            print(">> Perfil sugerido: Inovação/Empreendedorismo.")
            print("   Ambientes de startup ou P&D são ideais.")
        elif "Trabalho em Equipe" in fortes:
            print(">> Perfil sugerido: Facilitador/Agilista.")
            print("   Considere cargos como Scrum Master ou HRBP.")
        else:
            print(">> Perfil sugerido: Especialista técnico.")
            print("   Foque em elevar suas Soft Skills para complementar suas Hard Skills.")