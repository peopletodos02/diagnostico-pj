import streamlit as st
import requests
from datetime import datetime

# Configuracao da pagina
st.set_page_config(page_title="Diagnostico PJ", layout="centered")

# Estilo visual Verde Oliva (Identidade visual da empresa)
st.markdown("""
    <style>
    .stApp { background-color: #f0f7ee; }
    h1, h2, h3 { color: #2e4d23; font-weight: bold; }
    .stButton>button { background-color: #4c6340; color: white; width: 100%; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# Cabecalho e Objetivo conforme o documento oficial
st.title("FORMULARIO DE DIAGNOSTICO – PRESTADORES PJ")
[span_3](start_span)st.write("**Objetivo:** Este formulario tem como objetivo coletar percepcoes sobre a prestacao de servicos e a interacao profissional com a empresa. As respostas sao anonimas e serao utilizadas exclusivamente para melhoria de processos e da comunicacao entre as partes.")

# --- SECAO 1: DADOS INICIAIS ---
with st.expander("SECAO 1 – DADOS INICIAIS", expanded=True):
    [span_4](start_span)genero_sel = st.radio("Qual e seu genero?", ["Feminino", "Masculino", "Nao binario", "Prefiro nao responder", "Outro"])[span_4](end_span)
    
    genero = genero_sel
    if genero_sel == "Outro":
        genero = st.text_input("Por favor, especifique seu genero:")

    [span_5](start_span)tipo_servico = st.text_input("Qual tipo de prestacao de servico voce realiza?[span_5](end_span)")
    
    setor = st.selectbox("Para qual area voce presta servico?", [
        "Assessoria da Presidencia", "Checkout", "Consultoria", "Contabilidade", 
        "CRM Estrutural", "CTN Brasil", "CTN Global", "CTN Vendedores (App)", 
        "Dados", "Desenvolvimento/Produto TI", "Engenharia", "Financas Estrategicas", 
        "Financeiro", "FP&A", "Inteligencia/BI", "Melhoria Continua", "Motor RCE", 
        "Operacoes de Tecnologia", "Pessoas e Cultura", "Presidencia", "Produto", 
        "Projetos", "Qualidade", "Regional Centro Sul", "Regional Costa Leste", 
        "Regional Interior", "Regional Equatorial", "Regional Sao Paulo/Minas", 
        "Seguranca/Governanca", "Suporte"
    [span_6](start_span)])[span_6](end_span)

# --- EXPLICACAO DA ESCALA ---
st.markdown("---")
st.subheader("ESCALA PADRAO (USAR EM TODAS AS PERGUNTAS ABAIXO)")
[span_7](start_span)st.write("**0** = Nunca | **1** = Raramente | **2** = As vezes | **3** = Frequentemente | **4** = Sempre[span_7](end_span)")

def quest(label):
    return st.select_slider(label, options=[0, 1, 2, 3, 4])

# --- ESTRUTURA DAS 12 SECOES DO DOCUMENTO ---
secoes_dados = {
    [span_8](start_span)"SECAO 2 – CONDUTAS E RESPEITO": ["Presenciei ou vivenciei comentarios ofensivos ou inadequados no ambiente de atuacao", "Sinto seguranca para relatar situacoes de desrespeito", "Existe canal seguro e sigiloso para relato", "Situacoes de desrespeito sao tratadas adequadamente", "A empresa demonstra compromisso com ambiente respeitoso"],[span_8](end_span)
    "SECAO 3 – RELACIONAMENTO PROFISSIONAL": ["Existe colaboracao adequada entre as partes envolvidas", "Os pontos de contato fornecem informacoes necessarias", "Existem canais para tratar duvidas ou ajustes", "O ambiente de interacao e respeitoso e colaborativo"],
    "SECAO 4 – COMUNICACAO": ["Mudancas sao comunicadas de forma clara", "Existe transparencia nas decisoes que impactam as entregas", "Informacoes sao disponibilizadas no momento adequado", "Ha facilidade de comunicacao com as pessoas envolvidas"],
    "SECAO 5 – CLAREZA DOS SERVICOS PRESTADOS": ["As demandas e entregas sao definidas de forma clara", "As expectativas de entrega sao bem definidas", "A comunicacao contribui para execucao das entregas"],
    [span_9](start_span)"SECAO 6 – RETORNO SOBRE ENTREGAS": ["Recebo feedback sobre a aderencia das entregas", "A ausencia de feedback impacta a qualidade das entregas"],[span_9](end_span)
    [span_10](start_span)"SECAO 7 – AUTONOMIA (ESSENCIAL PJ)": ["Tenho autonomia na execucao das entregas", "Existe confianca na forma de execucao", "Ha excesso de processos ou controles", "Existe interferencia excessiva na execucao"],[span_10](end_span)
    "SECAO 8 – DEMANDAS E PRAZOS": ["O volume de operacoes realizadas e compativel com os prazos definidos", "Os prazos sao adequados para execucao das entregas"],
    "SECAO 9 – RELACIONAMENTOS": ["Evitei interacoes devido a conflitos", "Percebo conflitos recorrentes", "Os conflitos sao resolvidos adequadamente"],
    [span_11](start_span)"SECAO 10 – SITUACOES CRÍTICAS": ["Vivenciei situacoes graves (agressoes, ameacas etc.)", "Passei por situacoes de risco", "Alguma situacao causou impacto significativo"],[span_11](end_span)
    "SECAO 11 – CONDIÇÕES DE EXECUÇÃO": ["As condicoes de execucao dificultam a comunicacao", "A distancia impacta a troca de informacoes"],
    "SECAO 12 – FORMATO DE ATUAÇÃO": ["O formato (remoto/presencial) impacta a comunicação", "Recebo informacoes suficientes mesmo a distancia"]
}

respostas_finais = {}
for titulo, perguntas in secoes_dados.items():
    with st.expander(titulo):
        for p in perguntas:
            respostas_finais[p] = quest(p)

st.divider()
[span_12](start_span)sugestoes = st.text_area("SECAO FINAL – Deixe sugestões ou pontos de atencao que considere relevantes:")[span_12](end_span)

# --- LOGICA DE ENVIO COM BARRA DE PROGRESSO ---
if st.button("ENVIAR"):
    URL_WEBHOOK = "https://defaulte93279240f9745ba871f4a124f3343.19.environment.api.powerplatform.com:443/powerautomate/automations/direct/workflows/f7d6b663cfc34b1f981db313ccb54778/triggers/manual/paths/invoke?api-version=1&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=t-SrxxdoHxMTU17DPujee1OCyVh0Z3sC1IC_rC2Bn2E"
    
    if URL_WEBHOOK == "COLE_SUA_URL_DO_POWER_AUTOMATE_AQUI":
        st.warning("Por favor, configure a URL do Power Automate no codigo.")
    else:
        # Iniciando barra de progresso e ID unico
        barra = st.progress(0)
        status = st.empty()
        id_formulario = datetime.now().strftime("%Y%m%d%H%M%S")
        data_envio = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        
        lista_perguntas = list(respostas_finais.items())
        total = len(lista_perguntas)
        erro_grave = False

        for i, (pergunta, nota) in enumerate(lista_perguntas):
            # Atualizando feedback visual
            progresso_atual = (i + 1) / total
            barra.progress(progresso_atual)
            status.text(f"Enviando dados... {i+1} de {total}")
            
            payload = {
                "ID": id_formulario,
                "Genero": genero,
                "Setor": setor,
                "Tipo_Servico": tipo_servico,
                "Pergunta": pergunta,
                "Nota": nota,
                "Sugestoes": sugestoes,
                "Data_Hora": data_envio
            }
            
            try:
                requests.post(URL_WEBHOOK, json=payload)
            except:
                erro_grave = True

        # Limpando barra e mostrando sucesso
        barra.empty()
        status.empty()

        if not erro_grave:
            st.snow()
            st.success("Resposta enviada com sucesso! Agradecemos a sua colaboração.")
        else:
            st.error("Erro parcial no envio. Por favor, verifique.")
