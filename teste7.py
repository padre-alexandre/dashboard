import streamlit as st

# Função para definir o estado inicial
def define_estado():
    return {
        'pagina_atual': 'Página Inicial'
    }

# Função para obter o estado atual
def get_estado():
    if 'estado' not in st.session_state:
        st.session_state.estado = define_estado()
    return st.session_state.estado

def pagina_principal():
    estado = get_estado()
    st.title('Página Inicial')
    opcao_pagina = st.selectbox('Selecione uma página:', ['Alunos', 'Professores', 'Mentoria'])

    if opcao_pagina == 'Alunos':
        estado['pagina_atual'] = 'Alunos'
        pagina_alunos()
    elif opcao_pagina == 'Professores':
        estado['pagina_atual'] = 'Professores'
        pagina_professores()
    elif opcao_pagina == 'Mentoria':
        estado['pagina_atual'] = 'Mentoria'
        pagina_mentoria()

def pagina_alunos():
    estado = get_estado()
    st.title('Página Alunos')
    # Adicione elementos e lógica para a página de Alunos aqui

def pagina_professores():
    estado = get_estado()
    st.title('Página Professores')
    # Adicione elementos e lógica para a página de Professores aqui

def pagina_mentoria():
    estado = get_estado()
    st.title('Página Mentoria')
    opcao_mentoria = st.selectbox('Selecione uma opção de mentoria:', ['Opção 1', 'Opção 2', 'Opção 3'])
    st.write(opcao_mentoria)
    # Adicione elementos e lógica para a página de Mentoria aqui

def main():
    pagina_principal()

if __name__ == '__main__':
    main()
