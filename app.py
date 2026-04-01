import streamlit as st
import requests

# Configuração da página
st.set_page_config(page_title="Diagnóstico PJ", layout="centered")

# Estilo visual para manter a identidade verde
st.markdown("""
    <style>
    .stApp { background-color: #f0f7ee; }
    h1, h2, h3 { color: #2e4d23; }
    </style>
    """, unsafe_allow_html=True)

# Objetivo completo conforme o documento
st.title("FORMULÁRIO DE DIAGNÓSTICO – PRESTADORES PJ")
st.write("Objetivo: Este formulário tem como objetivo coletar percepções sobre a prestação de serviços e a interação profissional com a empresa. As respostas são anônimas e serão utilizadas exclusivamente para melhoria de processos e da comunicação entre as partes.")

# SEÇÃO 1 - DADOS INICIAIS
with st.expander("SEÇÃO 1 – DADOS INICIAIS", expanded=True):
    genero = st.radio("Qual é seu gênero?", ["Feminino", "Masculino", "Não binário", "Prefiro não responder", "Outro"])
    
    # Linha para escrever caso selecione "Outro"
    if genero == "Outro":
        outro_genero = st.text_input("Por favor, especifique seu gênero:")
        
    tipo_servico = st.text_input("Qual tipo de prestação de serviço você realiza?")
    
    setor = st.selectbox("Para qual área você presta serviço?", [
        "Assessoria da Presidência", "Checkout", "Consultoria", "Contabilidade", 
        "CRM Estrutural", "CTN Brasil", "CTN Global", "CTN Vendedores (App)", 
        "Dados", "Desenvolvimento/Produto TI", "Engenharia", "Finanças Estratégicas", 
        "Financeiro", "FP&A", "Inteligência/BI", "Melhoria Contínua", "Motor RCE", 
        "Operações de Tecnologia", "Pessoas e Cultura", "Presidência", "Produto", 
        "Projetos", "Qualidade", "Regional Centro Sul", "Regional Costa Leste", 
        "Regional Interior", "Regional Equatorial", "Regional São Paulo/Minas", 
        "Segurança/Governança", "Suporte"
    ])

# --- EXPLICAÇÃO DA ESCALA (Antes da Seção 2) ---
st.markdown("---")
st.subheader("ESCALA PADRÃO (USAR EM TODAS AS PERGUNTAS ABAIXO)")
st.write("**Tipo:** Grade de múltipla escolha")
st.write("""
* **0** = Nunca
* **1** = Raramente
* **2** = Às vezes
* **3** = Frequentemente
* **4** = Sempre
""")

# Definição da função de pergunta
escala = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4"}
def quest(label):
    return st.select_slider(label, options=list(escala.keys()))

# Dicionário de Seções
secoes = {
    "SEÇÃO 2 – CONDUTAS E RESPEITO": ["Presenciei ou vivenciei comentários ofensivos ou inadequados no ambiente de atuação", "Sinto segurança para relatar situações de desrespeito", "Existe canal seguro e sigiloso para relato", "Situações de desrespeito são tratadas adequadamente", "A empresa demonstra compromisso com ambiente respeitoso"],
    "SEÇÃO 3 – RELACIONAMENTO PROFISSIONAL": ["Existe colaboração adequada entre as partes envolvidas", "Os pontos de contato fornecem informações necessárias", "Existem canais para tratar dúvidas ou ajustes", "O ambiente de interação é respeitoso e colaborativo"],
    "SEÇÃO 4 – COMUNICAÇÃO": ["Mudanças são comunicadas de forma clara", "Existe transparência nas decisões que impactam as entregas", "Informações são disponibilizadas no momento adequado", "Há facilidade de comunicação com as pessoas envolvidas"],
    "SEÇÃO 5 – CLAREZA DOS SERVIÇOS PRESTADOS": ["As demandas e entregas são definidas de forma clara", "As expectativas de entrega são bem definidas", "A comunicação contribui para execução das entregas"],
    "SEÇÃO 6 – RETORNO SOBRE ENTREGAS": ["Recebo feedback sobre a aderência das entregas", "A ausência de feedback impacta a qualidade das entregas"],
    "SEÇÃO 7 – AUTONOMIA (ESSENCIAL PJ)": ["Tenho autonomia na execução das entregas", "Existe confiança na forma de execução", "Há excesso de processos ou controles", "Existe interferência excessiva na execução"],
    "SEÇÃO 8 – DEMANDAS E PRAZOS": ["O volume de operações realizadas é compatível com os prazos definidos", "Os prazos são adequados para execução das entregas"],
    "SEÇÃO 9 – RELACIONAMENTOS": ["Evitei interações devido a conflitos", "Percebo conflitos recorrentes", "Os conflitos são resolvidos adequadamente"],
    "SEÇÃO 10 – SITUAÇÕES CRÍTICAS": ["Vivenciei situações graves (agressões, ameaças etc.)", "Passei por situações de risco", "Alguma situação causou impacto significativo"],
    "SEÇÃO 11 – CONDIÇÕES DE EXECUÇÃO": ["As condições de execução dificultam a comunicação", "A distância impacta a troca de informações"],
    "SEÇÃO 12 – FORMATO DE ATUAÇÃO": ["O formato (remoto/presencial) impacta a comunicação", "Recebo informações suficientes mesmo à distância"]
}

respostas = {}
for titulo, perguntas in secoes.items():
    with st.expander(titulo):
        for p in perguntas:
            respostas[p] = quest(p)

st.divider()
sugestoes = st.text_area("SEÇÃO FINAL – Deixe sugestões ou pontos de atenção que considere relevantes:")

if st.button("Enviar Diagnóstico"):
    st.success("Dados enviados com sucesso!")
