# Arquivo: main.py
import time
# Importação dos módulos criados (devem estar na mesma pasta)
from modelos import Perfil, Competencia
from analise import AnalisadorDeSoftSkills

def exibir_titulo():
    print("_"*50)
    print("       CLI DE ANÁLISE DE SOFT SKILLS")
    print("_"*50)

def obter_input_valido(skill_nome):
    """Função auxiliar para validar a entrada de dados."""
    while True:
        try:
            valor = int(input(f" • De 1 a 5, como é sua {skill_nome}? "))
            if 1 <= valor <= 5:
                return valor
            else:
                print("   [!] Por favor, digite um número entre 1 e 5.")
        except ValueError:
            print("   [!] Entrada inválida. Digite apenas números inteiros.")

def main():
    exibir_titulo()
    
    nome_usuario = input("Qual é o seu nome? ")
    
    # Instanciando classes importadas
    usuario = Perfil(nome_usuario)
    analisador = AnalisadorDeSoftSkills()

    lista_skills = ["Comunicação", "Liderança", "Resiliência", "Trabalho em Equipe", "Criatividade"]

    print("\nResponda com sinceridade para obter o melhor 'norte'.")
    print("_" * 50)

    for skill in lista_skills:
        nota = obter_input_valido(skill)
        # Criando objeto Competencia (importado de modelos.py)
        nova_competencia = Competencia(skill, nota)
        usuario.adicionar_competencia(nova_competencia)

    print("\nProcessando seus dados...")
    time.sleep(1) 
    
    usuario.calcular_media()

    # Relatório
    print("\n" + "_"*50)
    print(f"RELATÓRIO DE PERFIL: {usuario.nome}")
    print(f"Média Geral: {usuario.media_geral:.1f}/5.0")
    print("_"*50 + "\n")

    for nome_skill, obj_skill in usuario.competencias.items():
        # Usando o analisador (importado de analise.py)
        resultado = analisador.analisar_competencia(obj_skill)
        
        print(f"SKILL: {resultado['skill']} ({resultado['nota']}/5)")
        print(f"Status: {resultado['status']} | Nível: {resultado['nivel']}")
        print(f"Dica: {resultado['recomendacao']}")
        print("-" * 30)

    analisador.gerar_norte_carreira(usuario)
    print("\nFim da análise.\n")

if __name__ == "__main__":
    main()