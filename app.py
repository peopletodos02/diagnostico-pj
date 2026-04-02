import streamlit as st
import requests
from datetime import datetime
import pytz

# Configuração da página
st.set_page_config(page_title="Diagnóstico PJ", layout="centered")

# Estilo visual limpo
st.markdown("""
    <style>
    .stApp { background-color: #f0f7ee; }
    h1, h2, h3 { color: #2e4d23; font-weight: bold; }
    .stButton>button { background-color: #4c6340; color: white; width: 100%; font-weight: bold; }
    /* Ajuste para reduzir o espacamento entre elementos */
    .block-container { padding-top: 2rem; }
    </style>
    """, unsafe_allow_html=True)

st.title("FORMULÁRIO DE DIAGNÓSTICO – PRESTADORES PJ")
st.write("**Objetivo:** Este formulário tem como objetivo coletar percepções sobre a prestação de serviços e a interação profissional com a empresa. As respostas são anônimas e serão utilizadas exclusivamente para melhoria de processos e da comunicação entre as partes.")

# --- SEÇÃO 1: DADOS INICIAIS ---
with st.expander("SEÇÃO 1 – DADOS INICIAIS", expanded=True):
    genero_sel = st.radio("Qual é seu gênero?", ["Feminino", "Masculino", "Não binário", "Prefiro não responder", "Outro"])
    genero = genero_sel
    if genero_sel == "Outro":
        genero = st.text_input("Por favor, especifique seu gênero:")

    setor = st.selectbox("Para qual área você presta serviço?", [
        "Assessoria da Presidência", "Checkout", "Consultoria", "Contabilidade", 
        "CRM Estrutural", "CTN Brasil", "CTN Global", "CTN Vendedores (App)", 
        "Dados", "Desenvolvimento/Produto TI", "Engenharia", "Finanças Estratégicas", 
        "Financeiro", "FP&A", "Inteligência/BI", "Melhoria Contínua", "Motor RCE", 
        "Operações de Tecnologia", "Pessoas e Cultura", "Presidência", "Produto", 
        "Projetos", "Qualidade", "Regional Centro-Sul", "Regional Costa Leste", 
        "Regional Interior", "Regional Equatorial", "Regional São Paulo/Minas", 
        "Segurança/Governança", "Suporte"
    ])

st.markdown("---")
st.subheader("ESCALA PADRÃO (0 a 4)")

# --- DICIONÁRIO DE SEÇÕES ---
secoes_dados = {
    "SEÇÃO 2 – CONDUTAS E RESPEITO": ["Presenciei ou vivenciei comentários ofensivos ou inadequados no ambiente de atuação", "Sinto segurança para relatar situações de desrespeito", "Existe canal seguro e sigiloso para relato", "Situações de desrespeito são tratadas adequadamente", "A empresa demonstra compromisso com um ambiente respeitoso"],
    "SEÇÃO 3 – RELACIONAMENTO PROFISSIONAL": ["Existe colaboração adequada entre as partes envolvidas", "Os pontos de contato fornecem informações necessárias", "Existem canais para tratar dúvidas ou ajustes", "O ambiente de interação é respeitoso e colaborativo"],
    "SEÇÃO 4 – COMUNICAÇÃO": ["Mudanças são comunicadas de forma clara", "Existe transparência nas decisões que impactam as entregas", "Informações são disponibilizadas no momento adequado", "Há facilidade de comunicação com as pessoas envolvidas"],
    "SEÇÃO 5 – CLAREZA DOS SERVIÇOS PRESTADOS": ["As demandas e entregas são definidas de forma clara", "As expectativas de entrega é bem definidas", "A comunicação contribui para a execução das entregas"],
    "SEÇÃO 6 – RETORNO SOBRE ENTREGAS": ["Recebo feedback sobre a aderência das entregas", "A ausência de feedback impacta a qualidade das entregas"],
    "SEÇÃO 7 – AUTONOMIA (ESSENCIAL PJ)": ["Tenho autonomia na execução das entregas", "Existe confiança na forma de execução", "Há excesso de processos ou controles", "Existe interferência excessiva na execução"],
    "SEÇÃO 8 – DEMANDAS E PRAZOS": ["O volume de operações realizadas é compatível com os prazos definidos", "Os prazos são adequados para a execução das entregas"],
    "SEÇÃO 9 – RELACIONAMENTOS": ["Evitei interações devido a conflitos", "Percebo conflitos recorrentes", "Os conflitos são resolvidos adequadamente"],
    "SEÇÃO 10 – SITUAÇÕES CRÍTICAS": ["Vivenciei situações graves (agressões, ameaças etc.)", "Passei por situações de risco", "Alguma situação causou impacto significativo"],
    "SEÇÃO 11 – CONDIÇÕES DE EXECUÇÃO": ["As condições de execução dificultam a comunicação", "A distância impacta a troca de informações"],
    "SEÇÃO 12 – FORMATO DE ATUAÇÃO": ["O formato (remoto/presencial) impacta a comunicação", "Recebo informações suficientes mesmo à distância"]
}

respostas_finais = {}
secoes_respondidas = {}

for titulo, perguntas in secoes_dados.items():
    with st.expander(titulo):
        for p in perguntas:
            respostas_finais[p] = st.select_slider(p, options=[0, 1, 2, 3, 4], key=f"slider_{p}")
        
        # Removido a linha divisória e o espaçamento grande
        # O checkbox agora aparece logo após a última pergunta
        secoes_respondidas[titulo] = st.checkbox(f"Concluí o preenchimento da {titulo}", key=f"check_{titulo}")

st.divider()
sugestoes = st.text_area("SEÇÃO FINAL – Deixe sugestões ou pontos de atenção relevantes:")

# --- LÓGICA DE ENVIO ---
if st.button("ENVIAR"):
    secoes_faltantes = [s for s, respondida in secoes_respondidas.items() if not respondida]
    
    if secoes_faltantes:
        st.error("⚠️ Atenção! Verifique o preenchimento de todas as perguntas e a marcação de confirmação ao final de cada seção.")
        for faltante in secoes_faltantes:
            st.write(f"- {faltante}")
    else:
        URL_WEBHOOK = "https://defaulte93279240f9745ba871f4a124f3343.19.environment.api.powerplatform.com:443/powerautomate/automations/direct/workflows/f7d6b663cfc34b1f981db313ccb54778/triggers/manual/paths/invoke?api-version=1&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=t-SrxxdoHxMTU17DPujee1OCyVh0Z3sC1IC_rC2Bn2E"
        
        if URL_WEBHOOK == "COLE_SUA_URL_AQUI":
            st.warning("Por favor, configure a URL do Power Automate no código.")
        else:
            barra = st.progress(0)
            status = st.empty()
            
            fuso_sp = pytz.timezone('America/Sao_Paulo')
            agora_sp = datetime.now(fuso_sp)
            
            id_formulario = agora_sp.strftime("%Y%m%d%H%M%S")
            data_hora_envio = agora_sp.strftime("%d/%m/%Y %H:%M:%S")
            
            lista_perguntas = list(respostas_finais.items())
            total = len(lista_perguntas)
            erro = False

            for i, (p_texto, nota_val) in enumerate(lista_perguntas):
                percentual = (i + 1) / total
                barra.progress(percentual)
                status.text(f"Enviando dados... {i+1} de {total}")
                
                payload = {
                    "ID": id_formulario, 
                    "Genero": genero, 
                    "Setor": setor,
                    "Pergunta": p_texto, 
                    "Nota": nota_val, 
                    "Sugestoes": sugestoes,
                    "Data_Hora": data_hora_envio
                }
                try:
                    requests.post(URL_WEBHOOK, json=payload)
                except:
                    erro = True

            barra.empty()
            status.empty()

            if not erro:
                st.success("Resposta enviada com sucesso! Agradecemos a sua colaboração.")
            else:
                st.error("Ocorreu um problema ao enviar. Verifique a conexão.")
