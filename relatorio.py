import streamlit as st
import pandas as pd
from google import genai

st.set_page_config(page_title="Relatório de Pesquisas")
st.title("Relatório de Pesquisas de Satisfação)
st.write("Olá! Irei analisar os resultados da sua pesquisa de satisfação e gerar um relatório com os dados e sugestões.")
client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])   # conectar com a ia
arquivo = st.file_uploader("Envie a planilha com os dados da sua pesquisa", type=[.xlsx])

if arquivo is not None:
      dados = pd.read_excel(arquivo)
      st.write("A planilha foi carregada com sucesso.)
      if st.button("Gerar relatório da pesquisa com o Gemini"):
            st.write("O Gemini está montando seu relatório. Aguarde.") 
            colunas = tabela.columns
            pergunta1 = colunas[1]     # pegar perguntas e respostas da planilha
            respostas1 = tabela[pergunta1]
            pergunta2 = colunas[2]
            respostas2 = tabela[pergunta2]
            pergunta3 = colunas[3]
            respostas3 = tabela[pergunta3]
            pergunta4 = colunas[4]
            respostas4 = tabela[pergunta4]
            pergunta5 = colunas[5]
            respostas5 = tabela[pergunta5]
            pergunta6 = colunas[6]
            respostas6 = tabela[pergunta6]
            pergunta7 = colunas[7]
            respostas7 = tabela[pergunta7]
            pergunta8 = colunas[8]
            respostas8 = tabela[pergunta8]
            pergunta9 = colunas[9]
            respostas9 = tabela[pergunta9]

            prompt = f"""   
            Você é um especialista em experiência e satisfação do cliente.
            Analise as respostas da pesquisa abaixo e elabore um relatório claro:

            PERGUNTA 1: {pergunta1}
            RESPOSTAS:
            {respostas1}

            PERGUNTA 2: {pergunta2}
            RESPOSTAS:
            {respostas2}

            PERGUNTA 3: {pergunta3}
            RESPOSTAS:
            {respostas3}

            PERGUNTA 4: {pergunta4}
            RESPOSTAS:
            {respostas4}

            PERGUNTA 5: {pergunta5}
            RESPOSTAS:
            {respostas5}

            PERGUNTA 6: {pergunta6}
            RESPOSTAS:
            {respostas6}

            PERGUNTA 7: {pergunta7}
            RESPOSTAS:
            {respostas7}

            PERGUNTA 8: {pergunta8}
            RESPOSTAS:
            {respostas8}
            
            PERGUNTA 9: {pergunta9}
            RESPOSTAS:
            {respostas9}

            Com base nas respostas, faça um relatório abordando os seguintes tópicos:
            1. Nível Geral de Satisfação: Como os clientes estão se sentindo em relação a cada pergunta?
            2. O que já está bom: Liste os pontos positivos e elogios que devem ser mantidos.
            3. O que precisa mudar: Aponte as principais reclamações e dê sugestões práticas de melhorias.
        """

            resposta = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)  # mandar para o gemini
      
            st.write(resposta.text)
      
       
