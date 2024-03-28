import streamlit as st
from alunos import mostrar_alunos
from streamlit import components

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

# CSS Botão
st.markdown(
    f"""
    <style>
        div.stButton > button:first-child {{
            background-color: #9E089E;
            width: 120px;
            height: 50px;
            color: white
        }}
    </style>
    """,
    unsafe_allow_html=True
)

# Função para adicionar estilos aos botões usando HTML e CSS
def add_button_style(button_id, background_color, width, height, color, border_radius):
    style = f"background-color: {background_color}; width: {width}px; height: {height}px; color: {color}; border-radius: {border_radius}px; border: 0px solid #000;"
    return st.markdown(f'<button id="{button_id}" style="{style}">Custom Button</button>', unsafe_allow_html=True)

# Função para lidar com eventos de clique nos botões
def handle_button_click(button_id):
    st.write(f'Botão {button_id} clicado!')

with st.container():
        col1, col2, col3, col4, col5, col6, col7, col8, col9 = st.columns([1,1,1,1,1,1,1,1,1])
        with col1:
            button1 = add_button_style("button1", "#FFA73E", 150, 50, "white", 10)
        with col2:
            botao_clicado2 = st.button("Professores", key="botao2")
        with col3:
            botao_clicado3 = st.button("Marketing", key="botao3")
        with col4:
            botao_clicado4 = st.button("Vendas", key="botao4")
        with col5:
            botao_clicado5 = st.button("Financeiro", key="botao5")
        with col6:
            botao_clicado6 = st.button("Gente", key="botao6")
        with col7:
            botao_clicado7 = st.button("Estratégico", key="botao7")
        with col8:
            botao_clicado8 = st.button("Mentoria", key="botao8")
        with col9:
            botao_clicado9 = st.button("Rotinas", key="botao9")

st.markdown("<hr>", unsafe_allow_html=True)

st.markdown(
    f"""
    <style>
        hr {{
            border: 1px solid #9E089E;
            margin-top: 5px;  /* Ajuste a margem superior conforme necessário */
        }}
    </style>
    """,
    unsafe_allow_html=True
)

### Mostrar páginas após clicar no botão

botoes_menu = [botao_clicado2, botao_clicado3, botao_clicado4, botao_clicado5, botao_clicado6, botao_clicado7, botao_clicado8, botao_clicado9]

if all(not botao for botao in botoes_menu):
    st.write("Mostrar alunos")
    mostrar_alunos()







def ChangeButtonColour(widget_label, font_color, background_color='transparent'):
    htmlstr = f"""
        <script>
            var elements = window.parent.document.querySelectorAll('button');
            for (var i = 0; i < elements.length; ++i) {{ 
                if (elements[i].innerText == '{widget_label}') {{ 
                    elements[i].style.color ='{font_color}';
                    elements[i].style.background = '{background_color}'
                }}
            }}
        </script>
        """
    components.html(f"{htmlstr}", height=0, width=0)

cols = st.columns(4)
cols[0].button('first button', key='b1')
cols[1].button('second button', key='b2')
cols[2].button('third button', key='b3')
cols[3].button('fourth button', key='b4')

ChangeButtonColour('second button', 'red', 'blue') # button txt to find, colour to assign
ChangeButtonColour('fourth button', '#c19af5', '#354b75') # button txt to find, colour to assign

















