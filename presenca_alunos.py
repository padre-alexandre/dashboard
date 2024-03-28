import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import plotly.graph_objects as go
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from plotly.subplots import make_subplots
from PIL import Image
import numpy as np
from google.auth.transport.requests import Request
#from dashboard import get_estado, define_estado

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

'''
import os
import json

credentials_path = os.getenv('GOOGLE_CREDENTIALS_PATH')
token_path = os.getenv('GOOGLE_TOKEN_PATH')

# Lendo o arquivo credentials.json
with open(credentials_path, 'r') as f:
    credentials = json.load(f)

# Lendo o arquivo token.json
with open(token_path, 'r') as f:
    token = json.load(f)
'''
    

# The ID and range of a sample spreadsheet.
#SAMPLE_SPREADSHEET_ID = "1btxVkFS-J4jkXR_SXr45NYkUzqnn4M3GB9eCuzzxPLk"
#SAMPLE_RANGE_NAME = "Presença nas aulas | Streamlit | Tabela alunos!A1:J100"

# Adicione esta linha ao início do seu script, fora de qualquer função específica
st.markdown('<style>td { border-right: none !important; }</style>', unsafe_allow_html=True)

def define_estado():
    return {
        'pagina_atual': 'Página Inicial'
    }

def get_estado():
    if 'estado' not in st.session_state:
        st.session_state.estado = define_estado()
    return st.session_state.estado



def ler_planilha(SAMPLE_SPREADSHEET_ID, SAMPLE_RANGE_NAME):
  """Shows basic usage of the Sheets API.
  Prints values from a sample spreadsheet.
  """
  creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=8080)
    # Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())

  try:
    service = build("sheets", "v4", credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = (
        sheet.values()
        .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME)
        .execute()
    )

    values = result.get("values", [])
    
    values2 = pd.DataFrame(values[1:], columns=values[0])

  except HttpError as err:
    var = 1

  return values2

'''
def ler_planilha(SAMPLE_SPREADSHEET_ID, SAMPLE_RANGE_NAME):
    """Shows basic usage of the Sheets API. Prints values from a sample spreadsheet."""
    
    creds = None
    
    # Define SCOPES
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
    
    # Define caminhos dos arquivos de credenciais a partir das variáveis de ambiente
    credentials_path = os.getenv('GOOGLE_CREDENTIALS_PATH', 'credentials.json')
    token_path = os.getenv('GOOGLE_TOKEN_PATH', 'token.json')
    
    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)
        
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)
            creds = flow.run_local_server(port=8080)
            
        with open(token_path, "w") as token:
            token.write(creds.to_json())

    try:
        service = build("sheets", "v4", credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME).execute()

        values = result.get("values", [])
        values2 = pd.DataFrame(values[1:], columns=values[0])

    except HttpError as err:
        var = 1

    return values2
'''
    

def graficos_semana(presenca_por_semana):

    # Adiciona um texto acima dos gráficos
    st.markdown(
        """
        <div style="display: flex; flex-direction: column; align-items: center; text-align: center; margin-top: -20px; margin-bottom: -40px;">
            <div style="font-size: 50px; font-weight: bold; text-transform: uppercase; color: #9E089E;">Presença Semanal</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Converter vírgulas para pontos apenas em colunas numéricas
    presenca_por_semana[['Presença', 'Presença Manhã', 'Presença Tarde']] = presenca_por_semana[['Presença', 'Presença Manhã', 'Presença Tarde']].applymap(lambda x: x.replace(',', '.') if isinstance(x, str) else x)

    # Converter as colunas para float
    presenca_por_semana[['Presença', 'Presença Manhã', 'Presença Tarde']] = presenca_por_semana[['Presença', 'Presença Manhã', 'Presença Tarde']].astype(float)

    # Sample data
    x = presenca_por_semana['Semana']
    y1 = presenca_por_semana['Presença']
    y2 = presenca_por_semana['Presença Manhã']
    y3 = presenca_por_semana['Presença Tarde']

    # Cor da linha e da área
    cor_linha = '#9E089E'
    cor_area = 'rgba(158, 8, 158, 0.5)'  # Cor com transparência

    # Create three separate figures, each with one line
    fig1 = go.Figure(go.Scatter(x=x, y=y1, fill='tozeroy', mode='lines', line=dict(color=cor_linha), fillcolor=cor_area, name='Line 1'))
    fig2 = go.Figure(go.Scatter(x=x, y=y2, fill='tozeroy', mode='lines', line=dict(color=cor_linha), fillcolor=cor_area, name='Line 2'))
    fig3 = go.Figure(go.Scatter(x=x, y=y3, fill='tozeroy', mode='lines', line=dict(color=cor_linha), fillcolor=cor_area, name='Line 3'))

    with st.container():
        col0, col1, col2, col3, col4, col5= st.columns([0.05,1,0.05,1,0.05,1])
        with col1:
            # Adiciona um marcador para criar espaço para a forma e o texto
            st.markdown('<div style="height: 50px;"></div>', unsafe_allow_html=True)

            # Adiciona uma caixa colorida acima do primeiro gráfico com texto dentro
            st.markdown(
                """
                <div style="background-color: rgba(158, 8, 158, 0.8); color: white; padding: 10px; border-top-left-radius: 10px; border-top-right-radius: 10px; text-align: center; ">
                    Presença Total
                </div>
                """,
                unsafe_allow_html=True
            )

            presenca_por_aluno = ler_planilha("1btxVkFS-J4jkXR_SXr45NYkUzqnn4M3GB9eCuzzxPLk", "Presença nas aulas | Streamlit | Tabela alunos!A1:K100")

            presenca_por_aluno[['Presença']] = presenca_por_aluno[['Presença']].applymap(lambda x: x.replace(',', '.') if isinstance(x, str) else x)

            # Converter as colunas para float
            presenca_por_aluno[['Presença']] = presenca_por_aluno[['Presença']].astype(float)

            presenca_por_aluno = presenca_por_aluno[presenca_por_aluno['Presença'] > 0]

            presenca_por_aluno['Presença'] = (presenca_por_aluno['Presença'].replace([np.inf, -np.inf, np.nan], 0) * 100).astype(int)

            media_presenca = presenca_por_aluno['Presença'].mean()

            formatted_html = """
                <div style="background-color: white; color: #9E089E; font-weight: bold; height: 40px; padding: -10px; border-radius: 10px; text-align: center; margin-top: 20px; margin-bottom: -20px; display: flex; align-items: center; justify-content: center; font-size: 30px;">
                    {:.0%}
                </div>
            """.format(media_presenca / 100)  # Convert to percentage by dividing by 100

            st.markdown(formatted_html, unsafe_allow_html=True)


        with col3:
            # Adiciona um marcador para criar espaço para a forma e o texto
            st.markdown('<div style="height: 50px;"></div>', unsafe_allow_html=True)

            # Adiciona uma caixa colorida acima do primeiro gráfico com texto dentro
            st.markdown(
                """
                <div style="background-color: rgba(158, 8, 158, 0.8); color: white; padding: 10px; border-top-left-radius: 10px; border-top-right-radius: 10px; text-align: center;">
                    Presença Manhã
                </div>
                """,
                unsafe_allow_html=True
            )

            presenca_por_aluno_manha = presenca_por_aluno[presenca_por_aluno['Turno'] == 'Manhã']

            media_presenca_manha = presenca_por_aluno_manha['Presença'].mean()

            formatted_html = """
                <div style="background-color: white; color: #9E089E; font-weight: bold; height: 40px; padding: -10px; border-radius: 10px; text-align: center; margin-top: 20px; margin-bottom: -20px; display: flex; align-items: center; justify-content: center; font-size: 30px;">
                    {:.0%}
                </div>
            """.format(media_presenca_manha / 100)  # Convert to percentage by dividing by 100

            st.markdown(formatted_html, unsafe_allow_html=True)

        with col5:
            # Adiciona um marcador para criar espaço para a forma e o texto
            st.markdown('<div style="height: 50px;"></div>', unsafe_allow_html=True)

            # Adiciona uma caixa colorida acima do primeiro gráfico com texto dentro
            st.markdown(
                """
                <div style="background-color: rgba(158, 8, 158, 0.8); color: white; padding: 10px; border-top-left-radius: 10px; border-top-right-radius: 10px; text-align: center;">
                    Presença Tarde
                </div>
                """,
                unsafe_allow_html=True
            )

            presenca_por_aluno_tarde = presenca_por_aluno[presenca_por_aluno['Turno'] == 'Tarde']

            media_presenca_tarde = presenca_por_aluno_tarde['Presença'].mean()

            formatted_html = """
                <div style="background-color: white; color: #9E089E; font-weight: bold; height: 40px; padding: -10px; border-radius: 10px; text-align: center; margin-top: 20px; margin-bottom: -20px; display: flex; align-items: center; justify-content: center; font-size: 30px;">
                    {:.0%}
                </div>
            """.format(media_presenca_tarde / 100)  # Convert to percentage by dividing by 100

            st.markdown(formatted_html, unsafe_allow_html=True)

    # Organizar os gráficos mais próximos usando make_subplots
    fig = make_subplots(rows=1, cols=3)#, subplot_titles=['Presença', 'Presença Manhã', 'Presença Tarde'])

    # Adicionar os traces corretamente
    fig.add_trace(fig1.data[0], row=1, col=1)
    fig.add_trace(fig2.data[0], row=1, col=2)
    fig.add_trace(fig3.data[0], row=1, col=3)

    # Adicionar texto dentro das formas
    fig.add_trace(
        go.Scatter(
            x=[5, 15, 25],  # Ajuste as posições conforme necessário
            y=[1.1, 1.1, 1.1],
            text=['Texto 1', 'Texto 2', 'Texto 3'],
            mode='text',
            showlegend=False,
            textposition="middle center"
        )
    )

    # Atualizar layout
    fig.update_layout(showlegend=False, height=400, width=1200, yaxis=dict(
                title='Presença',
            ),xaxis=dict(title='Semana'), margin=dict(l=5, r=5, b=50, t=50, pad=0))

    # Atualizar os limites do eixo Y para ir de 0 a 1 em todos os subgráficos
    fig.update_yaxes(range=[0, 1], row=1, col=1)
    fig.update_yaxes(range=[0, 1], row=1, col=2)
    fig.update_yaxes(range=[0, 1], row=1, col=3)

    fig.update_xaxes(range=[0, 20], row=1, col=1)
    fig.update_xaxes(range=[0, 20], row=1, col=2)
    fig.update_xaxes(range=[0, 20], row=1, col=3)

    # Atualizar os rótulos e o formato do eixo Y para porcentagem
    fig.update_yaxes(title_text='Presença (%)', tickformat=',.0%')
    fig.update_xaxes(title_text='Semana')

    # Exibir gráfico usando st.plotly_chart
    st.plotly_chart(fig, use_container_width=True)

def tabela_alunos(presenca_por_aluno):

    presenca_por_aluno[['Presença']] = presenca_por_aluno[['Presença']].applymap(lambda x: x.replace(',', '.') if isinstance(x, str) else x)

    # Converter as colunas para float
    presenca_por_aluno[['Presença']] = presenca_por_aluno[['Presença']].astype(float)

    presenca_por_aluno = presenca_por_aluno[presenca_por_aluno['Presença'] > 0]

    # Sort the DataFrame by 'Presença'
    presenca_por_aluno2 = presenca_por_aluno.sort_values(by='Presença', ascending=False)

    presenca_por_aluno2['Presença'] = (presenca_por_aluno2['Presença'].replace([np.inf, -np.inf, np.nan], 0) * 100).astype(int).astype(str) + '%'
    
    presenca_por_aluno2['Presença 1ª fase'] = presenca_por_aluno2['Presença 1ª fase'].str.replace(',', '.').astype(float)
    presenca_por_aluno2['Presença 1ª fase'].replace([np.inf, -np.inf, np.nan], 0, inplace=True)
    presenca_por_aluno2['Presença 1ª fase'] = (presenca_por_aluno2['Presença 1ª fase'] * 100).astype(int).astype(str) + '%'

    presenca_por_aluno2['Presença 2ª fase'] = presenca_por_aluno2['Presença 2ª fase'].str.replace(',', '.').astype(float)
    presenca_por_aluno2['Presença 2ª fase'].replace([np.inf, -np.inf, np.nan], 0, inplace=True)
    presenca_por_aluno2['Presença 2ª fase'] = (presenca_por_aluno2['Presença 2ª fase'] * 100).astype(int).astype(str) + '%'

    # Adiciona um texto acima dos gráficos
    st.markdown(
        """
        <div style="display: flex; flex-direction: column; align-items: center; text-align: center; margin-top: 20px; margin-bottom: 10px;">
            <div style="font-size: 50px; font-weight: bold; text-transform: uppercase; color: #9E089E;">Ranking de Presença dos Alunos</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    with st.container():
        col1, col2, col3 = st.columns([0.01,5,0.01])
        with col2:
            # Display the table with HTML
            st.markdown("""
                <style>
                    th, td {
                        border-top: none;
                        padding: 0px;  /* Adjust padding for better visual appearance */
                        text-align: center;  /* Center align text */
                        height: 60px; 
                        vertical-align: middle;
                    }
                </style>
                <table style="border-collapse: collapse; margin-top: 10px; margin-bottom: -32px;">
                    <thead>
                        <tr style="background-color: rgba(158, 8, 158, 0.8); color: white; font-weight: bold;">
                            <th style="width: 150px; min-width: 150px; max-width: 150px; text-align: center; border-top-left-radius: 10px;border-right: 1px solid rgba(158, 8, 158, 0.8);border-left: 0px solid rgba(158, 8, 158, 0.8);border-top: 0px solid rgba(158, 8, 158, 0.8);">Nome</th>
                            <th style="width: 250px; min-width: 250px; max-width: 250px; text-align: center;border-right: 1px solid rgba(158, 8, 158, 0.8);border-top: 0px solid rgba(158, 8, 158, 0.8);">Email</th>
                            <th style="width: 280px; min-width: 280px; max-width: 280px; text-align: center;border-right: 1px solid rgba(158, 8, 158, 0.8);border-top: 0px solid rgba(158, 8, 158, 0.8);">Turma</th>
                            <th style="width: 100px; min-width: 100px; max-width: 100px; text-align: center;border-right: 1px solid rgba(158, 8, 158, 0.8);border-top: 0px solid rgba(158, 8, 158, 0.8);">Presença</th>
                            <th style="width: 100px; min-width: 100px; max-width: 100px; text-align: center;border-right: 1px solid rgba(158, 8, 158, 0.8);border-top: 0px solid rgba(158, 8, 158, 0.8);">Total de aulas</th>
                            <th style="width: 100px; min-width: 100px; max-width: 100px; text-align: center;border-right: 1px solid rgba(158, 8, 158, 0.8);border-top: 0px solid rgba(158, 8, 158, 0.8);">Presença Total</th>
                            <th style="width: 100px; min-width: 100px; max-width: 100px; text-align: center;border-right: 1px solid rgba(158, 8, 158, 0.8);border-top: 0px solid rgba(158, 8, 158, 0.8);">Presença 1ª fase</th>
                            <th style="width: 100px; min-width: 100px; max-width: 100px; text-align: center; border-top-right-radius: 10px;border-right: 0px solid rgba(158, 8, 158, 0.8);border-top: 0px solid rgba(158, 8, 158, 0.8)">Presença 2ª fase</th>
                        </tr>
                    </thead>
                    <tbody>
            """, unsafe_allow_html=True)
    

    with st.container():
        col1, col2, col3 = st.columns([0.01,5,0.01])
        with col1:
           st.write("")
        with col2:
            # Iteration over the rows of the DataFrame
            for _, row in presenca_por_aluno2.iterrows():
                # Building the table row
                st.markdown("""
                <tr style="text-align: center; ">
                    <td style="width: 150px; min-width: 150px; max-width: 150px; text-align: center; border-bottom: 1px solid #9E089E; padding: 10px; height: 40px; border-left: 1px solid white; border-right: 1px solid white;">{0}</td>
                    <td style="width: 250px; min-width: 250px; max-width: 250px; text-align: center; border-bottom: 1px solid #9E089E; padding: 10px; height: 40px; border-left: 1px solid white; border-right: 1px solid white;">{1}</td>
                    <td style="width: 280px; min-width: 280px; max-width: 280px; text-align: center; border-bottom: 1px solid #9E089E; padding: 10px; height: 40px; border-left: 1px solid white; border-right: 1px solid white;">{2}</td>
                    <td style="width: 100px; min-width: 100px; max-width: 100px; text-align: center; border-bottom: 1px solid #9E089E; padding: 10px; height: 40px; border-left: 1px solid white; border-right: 1px solid white;">{3}</td>
                    <td style="width: 100px; min-width: 100px; max-width: 100px; text-align: center; border-bottom: 1px solid #9E089E; padding: 10px; height: 40px; border-left: 1px solid white; border-right: 1px solid white;">{4}</td>
                    <td style="width: 100px; min-width: 100px; max-width: 100px; text-align: center; border-bottom: 1px solid #9E089E; padding: 10px; height: 40px; border-left: 1px solid white; border-right: 1px solid white;">{5}</td>
                    <td style="width: 100px; min-width: 100px; max-width: 100px; text-align: center; border-bottom: 1px solid #9E089E; padding: 10px; height: 40px; border-left: 1px solid white; border-right: 1px solid white;">{6}</td>
                    <td style="width: 100px; min-width: 100px; max-width: 100px; text-align: center; border-bottom: 1px solid #9E089E; padding: 10px; height: 40px; border-left: 1px solid white; border-right: 1px solid white;">{7}</td>
                </tr>
            """.format(row['Nome'], row['Email'], row['Turma'], row['Presença'], row['Total de aulas'], row['Presença Total'], row['Presença 1ª fase'], row['Presença 2ª fase']), unsafe_allow_html=True)
        with col3:
           st.write("")

    # Closing the table
    st.markdown("""
            </tbody>
        </table>
    """, unsafe_allow_html=True)

def mostrar_presenca_alunos():
    
    estado = get_estado()
    # Adicione esta linha ao início do seu script, fora de qualquer função específica
    st.markdown('<style>td { border-right: none !important; }</style>', unsafe_allow_html=True)

    presenca_por_aluno = ler_planilha("1btxVkFS-J4jkXR_SXr45NYkUzqnn4M3GB9eCuzzxPLk", "Presença nas aulas | Streamlit | Tabela alunos!A1:K100")
    presenca_por_semana = ler_planilha("1btxVkFS-J4jkXR_SXr45NYkUzqnn4M3GB9eCuzzxPLk", "Presença nas aulas | Streamlit | Presença semanal!A1:D21")

    graficos_semana(presenca_por_semana)
    tabela_alunos(presenca_por_aluno)
