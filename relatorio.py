import streamlit as st
import pandas as pd
from google import genai

st.set_page_config(page_title="Relatório de Pesquisas")
st.title("Relatório de Pesquisas de Satisfação")

api_key = st.secrets.get("GEMINI_API_KEY")
if not api_key:
    st.error("A chave 'GEMINI_API_KEY' não foi encontrada nos Secrets do Streamlit Cloud.")
    st.stop()
client = genai.Client(api_key=api_key)

st.write("Olá! Irei analisar os resultados da sua pesquisa de satisfação e gerar um relatório com os dados e sugestões.")
client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])   # conectar com a ia
arquivo = st.file_uploader("Envie a planilha com os dados da sua pesquisa", type=["xlsx"])

if arquivo is not None:
      dados = pd.read_excel(arquivo)
      st.write("A planilha foi carregada com sucesso.")
      if st.button("Gerar relatório da pesquisa com o Gemini"):
            st.write("O Gemini está montando seu relatório. Aguarde.") 
            texto_dados = dados.to_string()

            prompt = f"""   
            Você é um especialista em experiência e satisfação do cliente.
            Analise as respostas da pesquisa abaixo e elabore um relatório claro:

            DADOS DA PESQUISA:
            {texto_dados}

            Com base nas respostas, faça um relatório abordando os seguintes tópicos:
            1. Nível geral de satisfação dos clientes: como eles estão se sentindo em relação a cada pergunta?
            2. O que já está bom: Liste os pontos positivos e elogios que devem ser mantidos.
            3. O que precisa mudar: Aponte as principais reclamações e dê sugestões práticas de melhorias.
        """

            try:
                resposta = client.models.generate_content(model="gemini-2.5-pro", contents=prompt)
                st.write(resposta.text)
            
            except Exception as e:
                st.error("Falha ao comunicar com a API do Gemini.")
                st.code(str(e))
            
      
       
