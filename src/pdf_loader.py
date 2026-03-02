import os
import pdfplumber

def carregar_pdfs(caminho_pasta):
    textos = []
    for arquivo in os.listdir(caminho_pasta):
        if arquivo.endswith(".pdf"):
            caminho_pdf = os.path.join(caminho_pasta, arquivo)
            with pdfplumber.open(caminho_pdf) as pdf:
                texto = ""
                for pagina in pdf.pages:
                    texto += pagina.extract_text() + "\n"
                textos.append(texto)
    return textos

if __name__ == "__main__":
    pdfs = carregar_pdfs("../data/pdfs")
    print(f"Carregados {len(pdfs)} PDFs.")
    if pdfs:
        print(pdfs[0][:500])
