from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
from pdf_loader import carregar_pdfs

def criar_indice(textos):
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(textos)
    with open("indice.pkl", "wb") as f:
        pickle.dump((vectorizer, X), f)
    print("Índice criado com sucesso.")

if __name__ == "__main__":
    textos = carregar_pdfs("../data/pdfs")
    criar_indice(textos)
