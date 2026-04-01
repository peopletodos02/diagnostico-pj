import streamlit as st
import requests
from datetime import datetime

# Configuração da página
st.set_page_config(page_title="Diagnóstico PJ", layout="centered")

# Estilo visual (Verde Oliva)
st.markdown("""
    <style>
    .stApp { background-color: #f0f7ee; }
    h1, h2, h3 { color: #2e4d23; font-weight: bold; }
    .stButton>button { background-color: #4c6340; color: white; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

# Título e Objetivo conforme o documento
st.title("FORMULÁRIO DE DIAGNÓSTICO – PRESTADORES PJ")
[span_1](start_span)st.write("**Objetivo:** Este formulário tem como objetivo coletar percepções sobre a prestação de serviços e a interação profissional com a empresa.[span_1](end_span)")
[span_2](start_span)st.write("As respostas são anônimas e serão utilizadas exclusivamente para melhoria de processos e da comunicação entre as partes.[span_2](end_span)")

# --- SEÇÃO 1: DADOS INICIAIS ---
with st.expander("SEÇÃO 1 – DADOS INICIAIS", expanded=True):
    [span_3](start_span)genero_selecionado = st.radio("Qual é seu gênero?[span_3](end_span)", ["Feminino", "Masculino", "Não binário", "Prefiro não responder", "Outro"])
    
    genero = genero_selecionado
    if genero_selecionado == "Outro":
        genero = st.text_input("Por favor, especifique seu gênero:")

    [span_4](start_span)tipo_servico = st.text_input("Qual tipo de prestação de serviço você realiza?[span_4](end_span)")
    
    [span_5](start_span)setor = st.selectbox("Para qual área você presta serviço?[span_5](end_span)", [
        "Assessoria da Presidência", "Checkout", "Consultoria", "Contabilidade", 
        "CRM Estrutural", "CTN Brasil", "CTN Global", "CTN Vendedores (App)", 
        "Dados", "Desenvolvimento/Produto TI", "Engenharia", "Finanças Estratégicas", 
        "Financeiro", "FP&A", "Inteligência/BI", "Melhoria Contínua", "Motor RCE", 
        "Operações de Tecnologia", "Pessoas e Cultura", "Presidência", "Produto", 
        "Projetos", "Qualidade", "Regional Centro Sul", "Regional Costa Leste", 
        "Regional Interior", "Regional Equatorial", "Regional São Paulo/Minas", 
        "Segurança/Governança", "Suporte"
    ])

# --- EXPLICAÇÃO DA ESCALA ---
st.markdown("---")
[span_6](start_span)st.subheader("ESCALA PADRÃO (USAR EM TODAS AS PERGUNTAS ABAIXO)[span_6](end_span)")
[span_7](start_span)st.write("**0** = Nunca | **1** = Raramente | **2** = Às vezes | **3** = Frequentemente | **4** = Sempre[span_7](end_span)")

# Função para criar a pergunta
def quest(label):
    return st.select_slider(label, options=[0, 1, 2, 3, 4])

# [span_8](start_span)Estrutura de Seções[span_8](end_span)
secoes_dados = {
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

respostas_finais = {}
for titulo, perguntas in secoes_dados.items():
    with st.expander(titulo):
        for p in perguntas:
            respostas_finais[p] = quest(p)

st.divider()
[span_9](start_span)sugestoes = st.text_area("SEÇÃO FINAL – Deixe sugestões ou pontos de atenção que considere relevantes:[span_9](end_span)")

# --- ENVIO DOS DADOS ---
if st.button("Enviar Diagnóstico"):
    URL_WEBHOOK = "SUA_URL_AQUI" # Cole aqui a URL do Power Automate
    
    if URL_WEBHOOK == "SUA_URL_AQUI":
        st.warning("Por favor, configure a URL do Power Automate no código.")
    else:
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        erro_envio = False

        for pergunta, nota in respostas_finais.items():
            payload = {
                "Gênero": genero,
                "Setor": setor,
                "Tipo_Serviço": tipo_servico,
                "Pergunta": pergunta,
                "Nota": nota,
                "Sugestões": sugestoes,
                "Data_Hora": data_hora
            }
            try:
                requests.post(URL_WEBHOOK, json=payload)
            except:
                erro_envio = True

        if not erro_envio:
            st.success("Diagnóstico enviado com sucesso!")
        else:
            st.error("Erro ao enviar alguns dados. Verifique a conexão.")
