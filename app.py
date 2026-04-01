import streamlit as st
import requests

# Configuração da página
st.set_page_config(page_title="Diagnóstico PJ", layout="centered")

# Estilo visual
st.markdown("""
    <style>
    .stApp { background-color: #f0f7ee; }
    h1, h2, h3 { color: #2e4d23; }
    </style>
    """, unsafe_allow_html=True)

st.title("FORMULÁRIO DE DIAGNÓSTICO – PRESTADORES PJ")
st.write("Objetivo: Coletar percepções sobre a prestação de serviços e a interação profissional.")

# SEÇÃO 1
with st.expander("SEÇÃO 1 – DADOS INICIAIS", expanded=True):
    genero = st.radio("Qual é seu gênero?", ["Feminino", "Masculino", "Não binário", "Prefiro não responder", "Outro"])
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

# Escala 0 a 4
escala = {0: "0 (Nunca)", 1: "1 (Raramente)", 2: "2 (Às vezes)", 3: "3 (Frequentemente)", 4: "4 (Sempre)"}

def quest(label):
    return st.select_slider(label, options=list(escala.keys()), format_func=lambda x: escala[x])

# Dicionário com todas as seções do documento
secoes = {
    "SEÇÃO 2 – CONDUTAS E RESPEITO": ["Presenciei comentários ofensivos", "Segurança para relatar desrespeito", "Existe canal seguro", "Desrespeito é tratado adequadamente", "Empresa demonstra compromisso"],
    "SEÇÃO 3 – RELACIONAMENTO": ["Colaboração adequada", "Pontos de contato informativos", "Canais para dúvidas", "Ambiente respeitoso"],
    "SEÇÃO 4 – COMUNICAÇÃO": ["Mudanças claras", "Transparência nas decisões", "Informações no momento adequado", "Facilidade de comunicação"],
    "SEÇÃO 5 – CLAREZA": ["Demandas claras", "Expectativas bem definidas", "Comunicação ajuda na execução"],
    "SEÇÃO 6 – FEEDBACK": ["Recebo feedback", "Falta de feedback impacta qualidade"],
    "SEÇÃO 7 – AUTONOMIA": ["Tenho autonomia", "Confiança na execução", "Excesso de processos", "Interferência excessiva"],
    "SEÇÃO 8 – PRAZOS": ["Volume compatível", "Prazos adequados"],
    "SEÇÃO 9 – CONFLITOS": ["Evitei interações", "Percebo conflitos recorrentes", "Conflitos resolvidos adequadamente"],
    "SEÇÃO 10 – CRÍTICA": ["Situações graves", "Situações de risco", "Impacto significativo"],
    "SEÇÃO 11 – CONDIÇÕES": ["Execução dificulta comunicação", "Distância impacta trocas"],
    "SEÇÃO 12 – FORMATO": ["Remoto/Presencial impacta", "Informações suficientes à distância"]
}

respostas_coletadas = {}
for titulo, perguntas in secoes.items():
    with st.expander(titulo):
        for p in perguntas:
            respostas_coletadas[p] = quest(p)

st.divider()
sugestoes = st.text_area("SEÇÃO FINAL – Deixe sugestões ou pontos de atenção")

if st.button("Enviar"):
    st.success("Formulário enviado com sucesso!")
