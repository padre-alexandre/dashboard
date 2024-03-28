import streamlit as st

# Função para mostrar a página de Alunos
def mostrar_alunos():
    st.write("Você está na página de Alunos.")

# Função para mostrar a página de Professores
def mostrar_professores():
    st.write("Você está na página de Professores.")

# Função para mostrar a página de Mentoria
def mostrar_mentoria():
    st.write("Você está na página de Mentoria.")
    # Adiciona um dropdown na página de Mentoria
    opcao_periodo = st.selectbox('Selecione o período:', ['Última semana', 'Últimas 4 semanas', 'Desde o início'])

# Função para obter ou definir a página atual
def get_pagina_atual():
    if 'pagina_atual' not in st.session_state:
        st.session_state.pagina_atual = "Página Inicial"
    return st.session_state.pagina_atual

def set_pagina_atual(pagina):
    st.session_state.pagina_atual = pagina

# Mostra os botões para selecionar a página
def mostrar_botoes():
    pagina_atual = get_pagina_atual()
    if st.button("Alunos"):
        set_pagina_atual("Alunos")
    if st.button("Professores"):
        set_pagina_atual("Professores")
    if st.button("Mentoria"):
        set_pagina_atual("Mentoria")

# Executa a função para mostrar os botões e a página atual
mostrar_botoes()

# Determina qual página mostrar com base na página atual
pagina_atual = get_pagina_atual()
if pagina_atual == "Alunos":
    mostrar_alunos()
elif pagina_atual == "Professores":
    mostrar_professores()
elif pagina_atual == "Mentoria":
    mostrar_mentoria()
