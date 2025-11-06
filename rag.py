from sentence_transformers import SentenceTransformer
from chromadb.utils import embedding_functions
import pandas as pd
from chromadb import Client
from chromadb.config import Settings

# Modèle multilingue
embedder = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="intfloat/multilingual-e5-base"
)

class db:
    def __init__(self):
        self.client = Client(Settings(
            persist_directory="C:\\Users\\ihadi\\Desktop\\Semestre 9\\BI Pipeline\\hackathon_IBM_DIA\\chroma_db"
        ))
        self.collection = self.client.get_or_create_collection(
            name="my_multilingual_rag",
            embedding_function=embedder
        ) 

    def add_document(self, document, doc_id):
        self.collection.add(
            documents=[document],
            metadatas=[{"source": "faq"}],
            ids=[doc_id]
        )

    def similarity_search(self, query_text, n_results=1):
        return self.collection.query(query_texts=[query_text], n_results=n_results)

    def csv_to_chroma(self, csv='data_pretraitee.csv'):
        df = pd.read_csv(csv)
        for index, row in df.iterrows():
            question = row['Title']
            answer = row['Content']
            doc = f"Q: {question}, A: {answer}"

            self.collection.add(
                documents=[doc],
                metadatas=[{
                    "Post Type": row['Post Type'],
                    "Langues": row['Langues'],
                    "Thématiques": row['Thématiques'],
                    "Utilisateurs": row['Utilisateurs'],
                    "Écoles": row['Écoles']
                }],
                ids=[f"doc_{index}"]
            )

            print(f"✅ Added document {index+1}/{len(df)} to ChromaDB")

def search_similar_documents(db_chroma):
    result = db_chroma.similarity_search("Comment puis-je postuler pour un programme d'échange universitaire ?", n_results=3)
    return result

db_chroma = db()
db_chroma.csv_to_chroma()
