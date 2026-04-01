import streamlit as st
import requests

# Configuração da página e estilo
st.set_page_config(page_title="Diagnóstico PJ", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #f0f7ee; }
    h1, h2, h3 { color: #2e4d23; }
    .stButton>button { background-color: #4c6340; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.title("FORMULÁRIO DE DIAGNÓSTICO – PRESTADORES PJ")
[span_2](start_span)st.write("Objetivo: Coletar percepções sobre a prestação de serviços e a interação profissional[span_2](end_span).")
[span_3](start_span)st.info("As respostas são anônimas e utilizadas para melhoria de processos[span_3](end_span).")

# --- SEÇÃO 1: DADOS INICIAIS ---
with st.expander("SEÇÃO 1 – DADOS INICIAIS", expanded=True):
    [span_4](start_span)genero = st.radio("Qual é seu gênero?[span_4](end_span)", ["Feminino", "Masculino", "Não binário", "Prefiro não responder", "Outro"])
    if genero == "Outro":
        outro_genero = st.text_input("Especifique:")
    
    [span_5](start_span)tipo_servico = st.text_input("Qual tipo de prestação de serviço você realiza?[span_5](end_span)")
    
    [span_6](start_span)setor = st.selectbox("Para qual área você presta serviço?[span_6](end_span)", [
        "Assessoria da Presidência", "Checkout", "Consultoria", "Contabilidade", 
        "CRM Estrutural", "CTN Brasil", "CTN Global", "CTN Vendedores (App)", 
        "Dados", "Desenvolvimento/Produto TI", "Engenharia", "Finanças Estratégicas", 
        "Financeiro", "FP&A", "Inteligência/BI", "Melhoria Contínua", "Motor RCE", 
        "Operações de Tecnologia", "Pessoas e Cultura", "Presidência", "Produto", 
        "Projetos", "Qualidade", "Regional Centro Sul", "Regional Costa Leste", 
        "Regional Interior", "Regional Equatorial", "Regional São Paulo/Minas", 
        "Segurança/Governança", "Suporte"
    ])

# [span_7](start_span)Definição da Escala[span_7](end_span)
escala = {0: "0 (Nunca)", 1: "1 (Raramente)", 2: "2 (Às vezes)", 3: "3 (Frequentemente)", 4: "4 (Sempre)"}

def quest(label):
    return st.select_slider(label, options=list(escala.keys()), format_func=lambda x: escala[x])

# --- LOOP PARA AS SEÇÕES DE PERGUNTAS ---
respostas = {}

secoes = {
    "SEÇÃO 2 – CONDUTAS E RESPEITO": [
        [span_8](start_span)"Presenciei ou vivenciei comentários ofensivos ou inadequados[span_8](end_span)",
        [span_9](start_span)"Sinto segurança para relatar situações de desrespeito[span_9](end_span)",
        [span_10](start_span)"Existe canal seguro e sigiloso para relato[span_10](end_span)",
        [span_11](start_span)"Situações de desrespeito são tratadas adequadamente[span_11](end_span)",
        [span_12](start_span)"A empresa demonstra compromisso com ambiente respeitoso[span_12](end_span)"
    ],
    "SEÇÃO 3 – RELACIONAMENTO PROFISSIONAL": [
        [span_13](start_span)"Existe colaboração adequada entre as partes[span_13](end_span)",
        [span_14](start_span)"Os pontos de contato fornecem informações necessárias[span_14](end_span)",
        [span_15](start_span)"Existem canais para tratar dúvidas ou ajustes[span_15](end_span)",
        [span_16](start_span)"O ambiente de interação é respeitoso e colaborativo[span_16](end_span)"
    ],
    "SEÇÃO 4 – COMUNICAÇÃO": [
        [span_17](start_span)"Mudanças são comunicadas de forma clara[span_17](end_span)",
        [span_18](start_span)"Transparência nas decisões que impactam as entregas[span_18](end_span)",
        [span_19](start_span)"Informações são disponibilizadas no momento adequado[span_19](end_span)",
        [span_20](start_span)"Há facilidade de comunicação com as pessoas envolvidas[span_20](end_span)"
    ],
    "SEÇÃO 5 – CLAREZA DOS SERVIÇOS PRESTADOS": [
        [span_21](start_span)"As demandas e entregas são definidas de forma clara[span_21](end_span)",
        [span_22](start_span)"As expectativas de entrega são bem definidas[span_22](end_span)",
        [span_23](start_span)"A comunicação contribui para execução das entregas[span_23](end_span)"
    ],
    "SEÇÃO 6 – RETORNO SOBRE ENTREGAS": [
        [span_24](start_span)"Recebo feedback sobre a aderência das entregas[span_24](end_span)",
        [span_25](start_span)"A ausência de feedback impacta a qualidade das entregas[span_25](end_span)"
    ],
    "SEÇÃO 7 – AUTONOMIA (ESSENCIAL PJ)": [
        [span_26](start_span)"Tenho autonomia na execução das entregas[span_26](end_span)",
        [span_27](start_span)"Existe confiança na forma de execução[span_27](end_span)",
        [span_28](start_span)"Há excesso de processos ou controles[span_28](end_span)",
        [span_29](start_span)"Existe interferência excessiva na execução[span_29](end_span)"
    ],
    "SEÇÃO 8 – DEMANDAS E PRAZOS": [
        [span_30](start_span)"O volume de operações é compatível com os prazos[span_30](end_span)",
        [span_31](start_span)"Os prazos são adequados para execução das entregas[span_31](end_span)"
    ],
    "SEÇÃO 9 – RELACIONAMENTOS": [
        [span_32](start_span)"Evitei interações devido a conflitos[span_32](end_span)",
        [span_33](start_span)"Percebo conflitos recorrentes[span_33](end_span)",
        [span_34](start_span)"Os conflitos são resolvidos adequadamente[span_34](end_span)"
    ],
    "SEÇÃO 10 – SITUAÇÕES CRÍTICAS": [
        [span_35](start_span)"Vivenciei situações graves (agressões, ameaças etc.)[span_35](end_span)",
        [span_36](start_span)"Passei por situações de risco[span_36](end_span)",
        [span_37](start_span)"Alguma situação causou impacto significativo[span_37](end_span)"
    ],
    "SEÇÃO 11 – CONDIÇÕES DE EXECUÇÃO": [
        [span_38](start_span)"As condições de execução dificultam a comunicação[span_38](end_span)",
        [span_39](start_span)"A distância impacta a troca de informações[span_39](end_span)"
    ],
    "SEÇÃO 12 – FORMATO DE ATUAÇÃO": [
        [span_40](start_span)"O formato (remoto/presencial) impacta a comunicação[span_40](end_span)",
        [span_41](start_span)"Recebo informações suficientes mesmo à distância[span_41](end_span)"
    ]
}

for titulo, perguntas in secoes.items():
    with st.expander(titulo):
        for p in perguntas:
            respostas[p] = quest(p)

# --- SEÇÃO FINAL ---
st.divider()
[span_42](start_span)sugestoes = st.text_area("SEÇÃO FINAL: Deixe sugestões ou pontos de atenção[span_42](end_span)")

if st.button("Enviar Diagnóstico"):
    # Preparando dados para o Power Automate
    payload = {
        "genero": genero,
        "setor": setor,
        "tipo_servico": tipo_servico,
        "respostas": respostas,
        "sugestoes": sugestoes
    }
    
    # URL do seu Webhook do Power Automate
    URL_WEBHOOK = "SUA_URL_AQUI"
    
    try:
        # Envio dos dados
        # r = requests.post(URL_WEBHOOK, json=payload)
        st.success("Obrigado! Suas percepções foram enviadas com sucesso.")
    except:
        st.error("Erro ao conectar com o servidor. Tente novamente.")
