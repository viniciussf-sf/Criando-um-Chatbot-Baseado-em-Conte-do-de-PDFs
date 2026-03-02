import pickle
from sklearn.metrics.pairwise import cosine_similarity
from pdf_loader import carregar_pdfs

def carregar_indice():
    with open("indice.pkl", "rb") as f:
        vectorizer, X = pickle.load(f)
    return vectorizer, X

def buscar_resposta(pergunta, vectorizer, X, textos):
    pergunta_vec = vectorizer.transform([pergunta])
    similitudes = cosine_similarity(pergunta_vec, X)
    idx = similitudes.argmax()
    return textos[idx]

if __name__ == "__main__":
    textos = carregar_pdfs("../data/pdfs")
    vectorizer, X = carregar_indice()

    print("Chatbot iniciado! Digite 'sair' para encerrar.")
    while True:
        pergunta = input("Você: ")
        if pergunta.lower() in ["sair","exit"]:
            break
        resposta = buscar_resposta(pergunta, vectorizer, X, textos)
        print("Chatbot:", resposta[:500], "...")
