from sentence_transformers import SentenceTransformer
from chromadb.utils import embedding_functions
import pandas as pd

# Exemple : modèle multilingue E5
embedder = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="intfloat/multilingual-e5-base"
)

from chromadb import Client
from chromadb.config import Settings

class db():
    def __init__(self):
        self.client = Client(Settings(persist_directory="C:\\Users\\ihadi\\Desktop\\Semestre 9\\BI Pipeline\\hackathon_IBM_DIA\\chroma_db"))
        self.collection = self.client.get_or_create_collection(name="my_multilingual_rag", embedding_function=embedder)

    def add_document(self, document):
        self.collection.add(
            documents=[document],
            metadatas=[{"source": "faq"}],
            ids=["doc_fr_en"]
        )

    def query(self, query_text):
        return self.collection.query(query_text)
    
    def similarity_search(self, query_text, n_results=1):
        results = self.collection.query(
            query_texts=[query_text],
            n_results=n_results
        )
        return results

    def csv_to_chroma(self, csv='data_pretraitee.csv'):
        df = pd.read_csv(csv)
        for index, row in df.iterrows():
            question = row['Title']
            answer = row['Content']
            self.collection.add(documents=[f'''Q: {question}, A: {answer}'''],
                                metadatas=[{"Post Type": row['Post Type'], 
                                            "Langues": row['Langues'], 
                                            "Thématiques": row['Thématiques'], 
                                            "Utilisateurs": row['Utilisateurs'], 
                                            "Écoles": row['Écoles']}],
                                ids=["doc_fr_en"])
            print(f"Added document {index+1}/{len(df)} to ChromaDB")

# Exemple d'utilisation
db_chroma = db()
db_chroma.csv_to_chroma()
result = db_chroma.similarity_search("Comment Changer de mot de passe ?", n_results=1)
print(result)