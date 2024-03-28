import streamlit as st

st.set_page_config(page_title="Jazz Vestibular", page_icon="", layout="wide")

st.set_option('client.caching', False)

import streamlit.components.v1 as components
from alunos import mostrar_alunos
from professores import mostrar_professores
from mentoria import mostrar_mentoria
from logs import escrever_planilha
import datetime
import pytz
#from user_agents import parse


#@st.cache
#def get_user_agent():
#    query_params = st.experimental_get_query_params()
#    user_agent = query_params.get("user_agent")
#    if user_agent:
#        return parse(user_agent)
#    else:
#        return None

#user_agent = get_user_agent()
#if user_agent:
#    st.write("User Agent:", user_agent)
#else:
#    st.write("O parâmetro 'user_agent' não foi encontrado na URL.")


def dia_hora():

    fuso_horario_brasilia = pytz.timezone('America/Sao_Paulo')
    data_e_hora_brasilia = datetime.datetime.now(fuso_horario_brasilia)
    data_hoje_brasilia = str(data_e_hora_brasilia.date())
    hora_atual_brasilia = str(data_e_hora_brasilia.strftime('%H:%M:%S'))
    return data_hoje_brasilia, hora_atual_brasilia

# Função para definir o estado inicial
def define_estado():
    return {
        'pagina_atual': 'Página Inicial'
    }

def get_estado():
    if 'estado' not in st.session_state:
        st.session_state.estado = define_estado()
    return st.session_state.estado

def mostrar_botoes(permissao, nome):

    estado = get_estado()
    #st.write("Estado 1: "+str(estado))

    ### Logo do Jazz
    html_br="""
        <br>
        """

    with st.container():
            col1, col2, col3 = st.columns([3,4,3])
            with col1:
                st.markdown(html_br, unsafe_allow_html=True)
            with col2:
                st.image("./logo_jazz.png")
            with col3:
                st.markdown(html_br, unsafe_allow_html=True)

    ### Menu de Botões

    def ChangeButtonColour(widget_label, font_color, background_color='transparent'):
        htmlstr = f"""
            <script>
                var elements = window.parent.document.querySelectorAll('button');
                for (var i = 0; i < elements.length; ++i) {{ 
                    if (elements[i].innerText == '{widget_label}') {{ 
                        elements[i].style.color ='{font_color}';
                        elements[i].style.background = '{background_color}';
                        elements[i].style.width = '120px';  // Adiciona a largura desejada
                        elements[i].style.height = '50px';  // Adiciona a altura desejada
                    }}
                }}
            </script>
            """
        components.html(f"{htmlstr}", height=0, width=0)

    if permissao == "Administrador":

        with st.container():
                col1, col2, col3, col4, col5, col6, col7, col8, col9 = st.columns([1,1,1,1,1,1,1,1,1])
                with col1:
                    botao_clicado1 = col1.button('Alunos', key='b1')
                    ChangeButtonColour('Alunos', 'white', '#9E089E')
                with col2:
                    botao_clicado2 = col2.button('Professores', key='b2')
                    ChangeButtonColour('Professores', 'white', '#9E089E')
                with col3:
                    botao_clicado3 = col3.button('Marketing', key='b3')
                    ChangeButtonColour('Marketing', 'white', '#9E089E')
                with col4:
                    botao_clicado4 = col4.button('Vendas', key='b4')
                    ChangeButtonColour('Vendas', 'white', '#9E089E')
                with col5:
                    botao_clicado5 = col5.button('Financeiro', key='b5')
                    ChangeButtonColour('Financeiro', 'white', '#9E089E')
                with col6:
                    botao_clicado6 = col6.button('Gente', key='b6')
                    ChangeButtonColour('Gente', 'white', '#9E089E')
                with col7:
                    botao_clicado7 = col7.button('Estratégico', key='b7')
                    ChangeButtonColour('Estratégico', 'white', '#9E089E')
                with col8:
                    botao_clicado8 = col8.button('Rotinas', key='b8')
                    ChangeButtonColour('Rotinas', 'white', '#9E089E')
                with col9:
                    botao_clicado9 = col9.button('Mentoria', key='b9')
                    ChangeButtonColour('Mentoria', 'white', '#9E089E')

        # Linha com estilo de margem ajustado

        st.markdown(
            """
            <hr style="border: 1px solid #9E089E; margin-top: -30px;">
            """,
            unsafe_allow_html=True
        )

        botoes_menu = [botao_clicado1, botao_clicado2, botao_clicado3, botao_clicado4, botao_clicado5, botao_clicado6, botao_clicado7, botao_clicado8, botao_clicado9]

        if all(not botao for botao in botoes_menu) and estado['pagina_atual'] == 'Alunos':
            #st.write("Estado 2: "+str(estado))
            estado = get_estado()
            #st.write("Estado 3: "+str(estado))
            estado['pagina_atual'] = 'Alunos'
            mostrar_alunos(nome, permissao)

        if botao_clicado1 or estado['pagina_atual'] == 'Alunos':
            estado = get_estado()
            estado['pagina_atual'] = 'Alunos'
            mostrar_alunos(nome, permissao)

        if botao_clicado2 or estado['pagina_atual'] == 'Professores':
            estado = get_estado()
            estado['pagina_atual'] = 'Professores'
            mostrar_professores(nome, permissao)

        if botao_clicado9 or estado['pagina_atual'] == 'Mentoria':
            estado = get_estado()
            estado['pagina_atual'] = 'Mentoria'
            #data_hoje_brasilia, hora_atual_brasilia = dia_hora()
            #data_to_write = [[nome, permissao, data_hoje_brasilia, hora_atual_brasilia, get_estado()['pagina_atual']]]
            #escrever_planilha("1Folwdg9mIwSxyzQuQlmwCoEPFq_sqC39MohQxx_J2_I", data_to_write, "Logs")
            mostrar_mentoria(nome, permissao)

    elif permissao == "Time":

        with st.container():
                col1, col2, col3, col4, col5, col6, col8, col9 = st.columns([1,1,1,1,1,1,1,1])
                with col1:
                    botao_clicado1 = col1.button('Alunos', key='b1')
                    ChangeButtonColour('Alunos', 'white', '#9E089E')
                with col2:
                    botao_clicado2 = col2.button('Professores', key='b2')
                    ChangeButtonColour('Professores', 'white', '#9E089E')
                with col3:
                    botao_clicado3 = col3.button('Marketing', key='b3')
                    ChangeButtonColour('Marketing', 'white', '#9E089E')
                with col4:
                    botao_clicado4 = col4.button('Vendas', key='b4')
                    ChangeButtonColour('Vendas', 'white', '#9E089E')
                with col5:
                    botao_clicado5 = col5.button('Financeiro', key='b5')
                    ChangeButtonColour('Financeiro', 'white', '#9E089E')
                with col6:
                    botao_clicado6 = col6.button('Gente', key='b6')
                    ChangeButtonColour('Gente', 'white', '#9E089E')
                #with col7:
                #    botao_clicado7 = col7.button('Estratégico', key='b7')
                #    ChangeButtonColour('Estratégico', 'white', '#9E089E')
                with col8:
                    botao_clicado8 = col8.button('Rotinas', key='b8')
                    ChangeButtonColour('Rotinas', 'white', '#9E089E')
                with col9:
                    botao_clicado9 = col9.button('Mentoria', key='b9')
                    ChangeButtonColour('Mentoria', 'white', '#9E089E')

        # Linha com estilo de margem ajustado

        st.markdown(
            """
            <hr style="border: 1px solid #9E089E; margin-top: -30px;">
            """,
            unsafe_allow_html=True
        )

        botoes_menu = [botao_clicado1, botao_clicado2, botao_clicado3, botao_clicado4, botao_clicado5, botao_clicado6, botao_clicado8, botao_clicado9]

        if all(not botao for botao in botoes_menu):
            estado = get_estado()
            estado['pagina_atual'] = 'Alunos'
            mostrar_alunos(nome, permissao)

        if botao_clicado1:
            estado = get_estado()
            estado['pagina_atual'] = 'Alunos'
            mostrar_alunos(nome, permissao)

        if botao_clicado2:
            estado = get_estado()
            estado['pagina_atual'] = 'Professores'
            mostrar_professores(nome, permissao)
        
        if botao_clicado9:
            estado = get_estado()
            estado['pagina_atual'] = 'Mentoria'
            #data_hoje_brasilia, hora_atual_brasilia = dia_hora()
            #data_to_write = [[nome, permissao, data_hoje_brasilia, hora_atual_brasilia, get_estado()['pagina_atual']]]
            #escrever_planilha("1Folwdg9mIwSxyzQuQlmwCoEPFq_sqC39MohQxx_J2_I", data_to_write, "Logs")
            mostrar_mentoria(nome, permissao)

    elif permissao == "Mentor":
        st.write('entrei')
        container = st.container()
        with container:
            cols = st.columns([1])  # Create a single-column layout
            col9 = cols[0]  # Get the first (and only) column from the list
            botao_clicado9 = col9.button('Mentoria', key='b9')
            ChangeButtonColour('Mentoria', 'white', '#9E089E')

        # Linha com estilo de margem ajustado

        st.markdown(
            """
            <hr style="border: 1px solid #9E089E; margin-top: -30px;">
            """,
            unsafe_allow_html=True
        )

        botoes_menu = [botao_clicado9]

        #if all(not botao for botao in botoes_menu):
            #mostrar_mentoria()
        #    mostrar_alunos()

        #if botao_clicado1:
        #    mostrar_alunos()

        #if botao_clicado2:
        #    mostrar_professores()

        if botao_clicado9:
            estado = get_estado()
            estado['pagina_atual'] = 'Mentoria'
            #data_hoje_brasilia, hora_atual_brasilia = dia_hora()
            #data_to_write = [[nome, permissao, data_hoje_brasilia, hora_atual_brasilia, get_estado()['pagina_atual']]]
            #escrever_planilha("1Folwdg9mIwSxyzQuQlmwCoEPFq_sqC39MohQxx_J2_I", data_to_write, "Logs")
            mostrar_mentoria(nome, permissao)

from tela_login import mostrar_tela_login

if __name__ == "__main__":

    #user_agent = get_user_agent()
    #st.write("User Agent:", user_agent)
    
    login, permissao, nome = mostrar_tela_login()

    if login:
        mostrar_botoes(permissao, nome)
        if get_estado()['pagina_atual'] == 'Página Inicial':
            data_hoje_brasilia, hora_atual_brasilia = dia_hora()
            data_to_write = [[nome, permissao, data_hoje_brasilia, hora_atual_brasilia, get_estado()['pagina_atual']]]
            escrever_planilha("1Folwdg9mIwSxyzQuQlmwCoEPFq_sqC39MohQxx_J2_I", data_to_write, "Logs")


    

    


