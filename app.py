import streamlit as st
import requests
from datetime import datetime

# Configuração da página
st.set_page_config(page_title="Diagnóstico PJ", layout="centered")

# Estilo visual personalizado (Verde Oliva)
st.markdown("""
    <style>
    .stApp { background-color: #f0f7ee; }
    h1, h2, h3 { color: #2e4d23; font-weight: bold; }
    .stButton>button { background-color: #4c6340; color: white; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

# --- CABEÇALHO E OBJETIVO ---
st.title("FORMULÁRIO DE DIAGNÓSTICO – PRESTADORES PJ")
[span_1](start_span)st.write("**Objetivo:** Este formulário tem como objetivo coletar percepções sobre a prestação de serviços e a interação profissional com a empresa. As respostas são anônimas e serão utilizadas exclusivamente para melhoria de processos e da comunicação entre as partes.")[span_1](end_span)

# --- SEÇÃO 1: DADOS INICIAIS ---
with st.expander("SEÇÃO 1 – DADOS INICIAIS", expanded=True):
    [span_2](start_span)genero_selecionado = st.radio("Qual é seu gênero?", ["Feminino", "Masculino", "Não binário", "Prefiro não responder", "Outro"])[span_2](end_span)
    
    genero = genero_selecionado
    if genero_selecionado == "Outro":
        genero = st.text_input("Por favor, especifique seu gênero:")

    [span_3](start_span)tipo_servico = st.text_input("Qual tipo de prestação de serviço você realiza?")[span_3](end_span)
    
    setor = st.selectbox("Para qual área você presta serviço?", [
        "Assessoria da Presidência", "Checkout", "Consultoria", "Contabilidade", 
        "CRM Estrutural", "CTN Brasil", "CTN Global", "CTN Vendedores (App)", 
        "Dados", "Desenvolvimento/Produto TI", "Engenharia", "Finanças Estratégicas", 
        "Financeiro", "FP&A", "Inteligência/BI", "Melhoria Contínua", "Motor RCE", 
        "Operações de Tecnologia", "Pessoas e Cultura", "Presidência", "Produto", 
        "Projetos", "Qualidade", "Regional Centro Sul", "Regional Costa Leste", 
        "Regional Interior", "Regional Equatorial", "Regional São Paulo/Minas", 
        "Segurança/Governança", "Suporte"
    [span_4](start_span)])[span_4](end_span)

# --- EXPLICAÇÃO DA ESCALA ---
st.markdown("---")
[span_5](start_span)st.subheader("ESCALA PADRÃO (USAR EM TODAS AS PERGUNTAS ABAIXO)")[span_5](end_span)
[span_6](start_span)st.write("**0** = Nunca | **1** = Raramente | **2** = Às vezes | **3** = Frequentemente | **4** = Sempre")[span_6](end_span)

# Função para criar o seletor de nota
def quest(label):
    return st.select_slider(label, options=[0, 1, 2, 3, 4])

# --- ESTRUTURA DAS 12 SEÇÕES ---
secoes_dados = {
    "SEÇÃO 2 – CONDUTAS E RESPEITO": [
        "Presenciei ou vivenciei comentários ofensivos ou inadequados no ambiente de atuação", 
        "Sinto segurança para relatar situações de desrespeito", 
        "Existe canal seguro e sigiloso para relato", 
        "Situações de desrespeito são tratadas adequadamente", 
        "A empresa demonstra compromisso com ambiente respeitoso"
    [span_7](start_span)],[span_7](end_span)
    "SEÇÃO 3 – RELACIONAMENTO PROFISSIONAL": [
        "Existe colaboração adequada entre as partes envolvidas", 
        "Os pontos de contato fornecem informações necessárias", 
        "Existem canais para tratar dúvidas ou ajustes", 
        "O ambiente de interação é respeitoso e colaborativo"
    [span_8](start_span)],[span_8](end_span)
    "SEÇÃO 4 – COMUNICAÇÃO": [
        "Mudanças são comunicadas de forma clara", 
        "Existe transparência nas decisões que impactam as entregas", 
        "Informações são disponibilizadas no momento adequado", 
        "Há facilidade de comunicação com as pessoas envolvidas"
    [span_9](start_span)],[span_9](end_span)
    "SEÇÃO 5 – CLAREZA DOS SERVIÇOS PRESTADOS": [
        "As demandas e entregas são definidas de forma clara", 
        "As expectativas de entrega são bem definidas", 
        "A comunicação contribui para execução das entregas"
    [span_10](start_span)],[span_10](end_span)
    "SEÇÃO 6 – RETORNO SOBRE ENTREGAS": [
        "Recebo feedback sobre a aderência das entregas", 
        "A ausência de feedback impacta a qualidade das entregas"
    [span_11](start_span)],[span_11](end_span)
    "SEÇÃO 7 – AUTONOMIA (ESSENCIAL PJ)": [
        "Tenho autonomia na execução das entregas", 
        "Existe confiança na forma de execução", 
        "Há excesso de processos ou controles", 
        "Existe interferência excessiva na execução"
    [span_12](start_span)],[span_12](end_span)
    "SEÇÃO 8 – DEMANDAS E PRAZOS": [
        "O volume de operações realizadas é compatível com os prazos definidos", 
        "Os prazos são adequados para execução das entregas"
    [span_13](start_span)],[span_13](end_span)
    "SEÇÃO 9 – RELACIONAMENTOS": [
        "Evitei interações devido a conflitos", 
        "Percebo conflitos recorrentes", 
        "Os conflitos são resolvidos adequadamente"
    [span_14](start_span)],[span_14](end_span)
    "SEÇÃO 10 – SITUAÇÕES CRÍTICAS": [
        "Vivenciei situações graves (agressões, ameaças etc.)", 
        "Passei por situações de risco", 
        "Alguma situação causou impacto significativo"
    [span_15](start_span)],[span_15](end_span)
    "SEÇÃO 11 – CONDIÇÕES DE EXECUÇÃO": [
        "As condições de execução dificultam a comunicação", 
        "A distância impacta a troca de informações"
    [span_16](start_span)],[span_16](end_span)
    "SEÇÃO 12 – FORMATO DE ATUAÇÃO": [
        "O formato (remoto/presencial) impacta a comunicação", 
        "Recebo informações suficientes mesmo à distância"
    [span_17](start_span)]
}

respostas_finais = {}
for titulo, perguntas in secoes_dados.items():
    with st.expander(titulo):
        for p in perguntas:
            respostas_finais[p] = quest(p)

# --- SEÇÃO FINAL ---
st.divider()
sugestoes = st.text_area("SEÇÃO FINAL – Deixe sugestões ou pontos de atenção que considere relevantes:")[span_17](end_span)

# --- BOTÃO DE ENVIO E INTEGRAÇÃO ---
if st.button("Enviar Diagnóstico"):
    # URL gerada pelo Power Automate (Substitua pela sua)
    URL_WEBHOOK = "SUA_URL_AQUI"
    
    if URL_WEBHOOK == "SUA_URL_AQUI":
        st.warning("Por favor, configure a URL do Power Automate no código.")
    else:
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        erro_envio = False

        # Loop para enviar cada resposta como uma linha na planilha
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
                envio = requests.post(URL_WEBHOOK, json=payload)
                if envio.status_code not in [200, 202]:
                    erro_envio = True
            except:
                erro_envio = True

        if not erro_envio:
            st.success("Diagnóstico enviado com sucesso! Obrigado por colaborar.")
        else:
            st.error("Ocorreu um erro ao enviar os dados para a planilha.")
