import streamlit as st

# Configuração da página
st.set_page_config(page_title="Diagnóstico de Prestadores PJ", layout="centered")

# Estilização básica para aproximar do modelo visual
st.markdown("""
    <style>
    .stApp { background-color: #f0f7ee; }
    .main-title { color: #2e4d23; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("FORMULÁRIO DE DIAGNÓSTICO – PRESTADORES PJ")
st.write("Objetivo: Coletar percepções sobre a prestação de serviços e a interação profissional.")

# --- SEÇÃO 1: DADOS INICIAIS ---
st.subheader("SEÇÃO 1 – DADOS INICIAIS")

genero = st.radio("Qual é o seu gênero?", ["Feminino", "Masculino", "Não binário", "Prefiro não responder", "Outro"])
if genero == "Outro":
    outro_genero = st.text_input("Especifique seu gênero:")

funcao = st.text_input("Qual é a sua função? (opcional)")

setor = st.selectbox("Qual é o seu setor? *", [
    "Assessoria da Presidência", "Checkout", "Consultoria", "Contabilidade", 
    "CRM Estrutural", "CTN Brasil", "CTN Global", "Dados", 
    "Desenvolvimento/Produto TI", "Engenharia", "Finanças Estratégicas", 
    "Financeiro", "FP&A", "Inteligência/BI", "Melhoria Contínua", 
    "Pessoas e Cultura", "Presidência", "Produto", "Projetos", "Qualidade"
])

# --- ESCALA PADRÃO ---
escala = {0: "0 (Nunca)", 1: "1 (Raramente)", 2: "2 (Às vezes)", 3: "3 (Frequentemente)", 4: "4 (Sempre)"}

def criar_pergunta(texto):
    return st.select_slider(texto, options=list(escala.keys()), format_func=lambda x: escala[x])

# --- SEÇÃO 2: CONDUTAS E RESPEITO ---
st.divider()
st.subheader("SEÇÃO 2 – CONDUTAS E RESPEITO")
p1 = criar_pergunta("Presenciei ou vivenciei comentários ofensivos ou inadequados no ambiente de atuação")
p2 = criar_pergunta("Sinto segurança para relatar situações de desrespeito")
p3 = criar_pergunta("Existe canal seguro e sigiloso para relato")

# --- SEÇÃO 7: AUTONOMIA (ESSENCIAL PJ) ---
st.divider()
st.subheader("SEÇÃO 7 – AUTONOMIA (ESSENCIAL PJ)")
p4 = criar_pergunta("Tenho autonomia na execução das entregas")
p5 = criar_pergunta("Existe confiança na forma de execução")
p6 = criar_pergunta("Existe interferência excessiva na execução")

# --- SEÇÃO FINAL ---
st.divider()
st.subheader("SEÇÃO FINAL")
sugestoes = st.text_area("Deixe sugestões ou pontos de atenção que considere relevantes:")

if st.button("Enviar Respostas"):
    st.success("Formulário enviado com sucesso!")

