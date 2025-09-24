import PyPDF2
from PyPDF2.errors import PdfReadError

def Ler_Pdf(caminho_arquivo):
    try:
        with open(caminho_arquivo, "rb") as arquivo_pdf:
            pdf = PyPDF2.PdfReader(arquivo_pdf)
            texto_primeira_pagina = pdf.pages[0].extract_text()
            return texto_primeira_pagina

    except FileExistsError:
        print("Arquivo não encontrado.")
        return None
    except PdfReadError:
        print("Erro ao ler o arquivo PDF.")
        return None
