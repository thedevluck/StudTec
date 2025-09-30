import streamlit as st
import google.generativeai as genai

# ==========================
# CONFIGURAÇÃO DA API GEMINI
# ==========================
genai.configure(api_key="YAIzaSyBuW08z3WaNt3lvdlmvkmRaWiLJ9PnZvP0")
model = genai.GenerativeModel("gemini-1.5-flash")

# ==========================
# FUNÇÃO DE RESUMO
# ==========================
def gerar_resumo(area, materia, subtopico, tema):
    prompt = f"""
    Resuma o conteúdo de ENEM abaixo de forma clara e objetiva:
    Área: {area}
    Matéria: {materia}
    Subtópico: {subtopico}
    Tema: {tema}
    """
    response = model.generate_content(prompt)
    return response.text

# ==========================
# CONTEÚDOS COMPLETOS DO ENEM
# ==========================
conteudos = {
    "MATEMÁTICA E SUAS TECNOLOGIAS": {
        "Álgebra": {
            "Funções": [
                "Função Afim", "Função Quadrática", "Função Exponencial", "Função Logarítmica",
                "Função Modular", "Função Composta", "Função Inversa"
            ],
            "Equações e Inequações": [
                "Equações do 1º grau", "Equações do 2º grau", "Sistemas Lineares",
                "Inequações de 1º grau", "Inequações de 2º grau"
            ],
            "Progressões": ["Progressão Aritmética (PA)", "Progressão Geométrica (PG)"]
        },
        "Geometria": {
            "Geometria Plana": [
                "Polígonos", "Triângulos", "Quadriláteros", "Círculo e Circunferência",
                "Teorema de Tales", "Teorema de Pitágoras", "Semelhança de Triângulos",
                "Áreas de Figuras Planas"
            ],
            "Geometria Espacial": [
                "Prismas", "Pirâmides", "Cilindros", "Cone", "Esfera", "Volume e Área"
            ],
            "Geometria Analítica": [
                "Ponto Médio", "Distância entre Pontos", "Equação da Reta",
                "Equação da Circunferência"
            ],
            "Trigonometria": [
                "Razões Trigonométricas no Triângulo Retângulo",
                "Lei dos Senos", "Lei dos Cossenos",
                "Funções Trigonométricas"
            ]
        },
        "Estatística e Probabilidade": {
            "Estatística": ["Média", "Mediana", "Moda", "Variância", "Desvio Padrão"],
            "Probabilidade": ["Eventos Independentes", "Eventos Dependentes", "Arranjos", "Permutações", "Combinações"]
        },
        "Análise Combinatória": {
            "Princípio Fundamental da Contagem": ["Contagem Simples", "Contagem com Repetição"],
            "Problemas Clássicos": ["Anagramas", "Distribuição de Objetos"]
        },
        "Matemática Financeira": {
            "Porcentagem": ["Cálculo Simples", "Aumento e Desconto"],
            "Juros": ["Juros Simples", "Juros Compostos"],
            "Taxas": ["Taxa Efetiva", "Taxa Nominal"]
        }
    },
    "CIÊNCIAS DA NATUREZA E SUAS TECNOLOGIAS": {
        "Biologia": {
            "Citologia": [
                "Estrutura da célula", "Organelas", "Mitose", "Meiose",
                "Divisão celular", "Membrana plasmática"
            ],
            "Genética": [
                "1ª Lei de Mendel", "2ª Lei de Mendel", "Herança ligada ao sexo",
                "Mutação", "Biotecnologia"
            ],
            "Evolução": [
                "Teorias Evolutivas", "Darwinismo", "Neodarwinismo", "Seleção Natural"
            ],
            "Ecologia": [
                "Cadeias e teias alimentares", "Ciclos Biogeoquímicos", "Populações", "Comunidades",
                "Biomas", "Impactos Ambientais"
            ],
            "Fisiologia Humana": [
                "Sistema Digestório", "Sistema Respiratório", "Sistema Circulatório",
                "Sistema Nervoso", "Sistema Endócrino", "Sistema Reprodutor"
            ]
        },
        "Química": {
            "Química Geral": [
                "Estrutura Atômica", "Tabela Periódica", "Ligações Químicas", "Forças Intermoleculares"
            ],
            "Química Inorgânica": [
                "Funções Inorgânicas (Ácidos, Bases, Sais e Óxidos)",
                "Reações Inorgânicas", "Balanceamento", "Soluções"
            ],
            "Química Orgânica": [
                "Hidrocarbonetos", "Funções Orgânicas", "Isomeria",
                "Reações Orgânicas", "Polímeros"
            ],
            "Físico-Química": [
                "Termoquímica", "Cinética Química", "Equilíbrio Químico", "Eletroquímica"
            ]
        },
        "Física": {
            "Mecânica": [
                "Cinemática", "Leis de Newton", "Gravitação Universal",
                "Trabalho, Potência e Energia", "Quantidade de Movimento", "Impulso"
            ],
            "Termologia": [
                "Calor e Temperatura", "Dilatação Térmica",
                "Leis da Termodinâmica", "Calorimetria"
            ],
            "Ondulatória": [
                "Movimento Harmônico", "Ondas Mecânicas", "Som", "Óptica Geométrica"
            ],
            "Eletromagnetismo": [
                "Eletrostática", "Eletrodinâmica", "Magnetismo", "Indução Eletromagnética"
            ],
            "Moderna": [
                "Relatividade", "Física Quântica", "Radioatividade"
            ]
        }
    },
    "CIÊNCIAS HUMANAS E SUAS TECNOLOGIAS": {
        "História": {
            "Brasil": [
                "Período Colonial", "Período Imperial", "Período Republicano"
            ],
            "Mundo": [
                "Antiguidade Oriental e Clássica",
                "Idade Média", "Idade Moderna",
                "Idade Contemporânea"
            ]
        },
        "Geografia": {
            "Geografia Física": [
                "Relevo", "Clima", "Vegetação", "Hidrografia", "Solo"
            ],
            "Geografia Humana": [
                "Urbanização", "Indústria", "Agricultura", "Globalização"
            ],
            "Geopolítica": [
                "Blocos Econômicos", "Guerra Fria", "Conflitos Atuais"
            ]
        },
        "Filosofia": {
            "Antiga": ["Pré-socráticos", "Sócrates", "Platão", "Aristóteles"],
            "Medieval": ["Agostinho", "Tomás de Aquino"],
            "Moderna": ["Descartes", "Hobbes", "Locke", "Kant", "Rousseau"],
            "Contemporânea": ["Nietzsche", "Existencialismo", "Escola de Frankfurt"]
        },
        "Sociologia": {
            "Clássicos": ["Marx", "Durkheim", "Weber"],
            "Temas": ["Cultura", "Identidade", "Movimentos Sociais", "Trabalho"]
        }
    },
    "LINGUAGENS, CÓDIGOS E SUAS TECNOLOGIAS": {
        "Português": {
            "Interpretação de Texto": ["Poema", "Crônica", "Artigo de opinião", "Charge", "Cartum"],
            "Gramática": [
                "Classes de Palavras", "Concordância", "Regência", "Colocação Pronominal",
                "Pontuação", "Figuras de Linguagem"
            ],
            "Redação": [
                "Estrutura do Texto Dissertativo-Argumentativo",
                "Coesão e Coerência", "Argumentação", "Competências do ENEM"
            ]
        },
        "Literatura": {
            "Escolas Literárias": [
                "Trovadorismo", "Classicismo", "Barroco", "Arcadismo", "Romantismo",
                "Realismo", "Naturalismo", "Parnasianismo", "Simbolismo", "Modernismo"
            ],
            "Autores": ["Machado de Assis", "Carlos Drummond de Andrade", "Clarice Lispector", "Guimarães Rosa"]
        },
        "Artes": {
            "Vanguardas Europeias": ["Cubismo", "Futurismo", "Expressionismo", "Surrealismo"],
            "Arte no Brasil": ["Modernismo", "Semana de 22", "Arte Contemporânea"]
        },
        "Educação Física": {
            "Esportes": ["Coletivos", "Individuais"],
            "Saúde": ["Qualidade de Vida", "Corpo e Movimento"]
        },
        "Língua Estrangeira": {
            "Inglês": ["Interpretação de Textos", "Falsos Cognatos"],
            "Espanhol": ["Interpretação de Textos", "Falsos Cognatos"]
        },
        "Tecnologias da Informação": {
            "Comunicação": ["Meios de Comunicação", "Linguagens Digitais"],
            "Internet": ["Redes Sociais", "Cultura Digital"]
        }
    }
}

# ==========================
# INTERFACE STREAMLIT
# ==========================
st.set_page_config(page_title="Resumidor ENEM", layout="wide")
st.title("📚 Resumidor Interativo ENEM com Gemini")

# 1. Escolher área
area = st.selectbox("Selecione a Área:", list(conteudos.keys()))

# 2. Escolher matéria
materia = st.selectbox("Selecione a Matéria:", list(conteudos[area].keys()))

# 3. Escolher subtopico
subtopico = st.selectbox("Selecione o Subtópico:", list(conteudos[area][materia].keys()))

# 4. Escolher tema
tema = st.selectbox("Selecione o Tema:", conteudos[area][materia][subtopico])

# Botão para gerar resumo
if st.button("Gerar Resumo"):
    resumo = gerar_resumo(area, materia, subtopico, tema)
    st.subheader("📖 Resumo Gerado:")
    st.write(resumo)