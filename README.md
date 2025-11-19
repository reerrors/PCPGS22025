# CLI de Análise de Soft Skills

Este projeto é uma ferramenta de linha de comando (CLI) desenvolvida em **Python** que realiza uma autoavaliação de competências comportamentais (Soft Skills). O sistema coleta inputs do usuário, processa os dados utilizando regras de negócio predefinidas e gera um relatório com feedbacks personalizados e um direcionamento de carreira.

## Propósito

O objetivo da aplicação é oferecer um **"norte"** para o desenvolvimento profissional do usuário. Diferente de testes técnicos, este sistema foca em habilidades interpessoais, permitindo que o usuário:

1.  **Reflita** sobre suas capacidades atuais (notas de 1 a 5).
2.  **Receba Feedback** imediato sobre pontos fortes e pontos de atenção.
3.  **Identifique Arquétipos** de carreira baseados na combinação de suas habilidades dominantes (ex: Liderança + Comunicação = Perfil de Gestão).

## Estrutura do Projeto

O código foi desenvolvido seguindo o paradigma de **Orientação a Objetos (POO)** e organizado em **módulos** para garantir a separação de responsabilidades.

```text
/ (Raiz do Projeto)
│
├── main.py        # Ponto de entrada (Interface com o Usuário/View)
├── analise.py     # Lógica de Negócio e Regras de Recomendação (Controller/Service)
├── modelos.py     # Estrutura de Dados e Classes Básicas (Model)
└── README.md      # Documentação do projeto
```
## Arquitetura de Classes

### 1. Competencia (em modelos.py)

Representa uma unidade de habilidade.

    Atributos: nome (str), pontuacao (int).

    Propósito: Encapsular o dado bruto de uma skill.

### 2. Perfil (em modelos.py)

Representa o usuário avaliado.

    Atributos: nome (str), competencias (dicionário), media_geral (float).

    Métodos:

        adicionar_competencia(): Insere uma nova skill no perfil.

        calcular_media(): Retorna a média aritmética das pontuações.

### 3. AnalisadorDeSoftSkills (em analise.py)

Motor de decisão do sistema.

    Atributos: base_conhecimento (dicionário com dicas para níveis baixo/alto).

    Métodos:

        analisar_competencia(): Recebe uma competência e retorna status, nível (Iniciante a Expert) e recomendação.

        gerar_norte_carreira(): Analisa o conjunto de skills fortes para sugerir um caminho profissional (ex: Gestão, Inovação, Especialista).
        
## Como usar

