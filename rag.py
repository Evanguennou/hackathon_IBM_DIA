import pandas as pd
import chromadb
from chromadb.config import Settings
from langchain_community.embeddings import HuggingFaceEmbeddings
import numpy as np

# # 1️⃣ Charger ton CSV
# df = pd.read_csv("data_pretraitee.csv")  # colonnes "Title" et "Content"

# # 2️⃣ Créer l'instance d'embeddings
# embedding_model = HuggingFaceEmbeddings(model_name="intfloat/multilingual-e5-base")

# # 3️⃣ Préparer les textes et IDs
# texts = [f'Q: {row["Title"]} A: {row["Content"]}' for _, row in df.iterrows()]
# ids = [str(i) for i in range(len(texts))]

# # 4️⃣ Calculer les embeddings en batch
# # HuggingFaceEmbeddings retourne une liste de listes, compatible avec Chroma
# embeddings = embedding_model.embed_documents(texts)

# 5️⃣ Connexion à Chroma Server (Docker)
client = chromadb.HttpClient(host="localhost", port=8000)

# 6️⃣ Créer ou récupérer la collection
collection_name = "ma_collection"
try:
    # Essaie de créer la collection
    collection = client.create_collection(name=collection_name)
except Exception as e:
    # Si elle existe déjà, récupère-la
    collection = client.get_collection(name=collection_name)

# 7️⃣ Ajouter les documents avec les embeddings
# collection.add(
#     ids=ids,
#     documents=texts,
#     embeddings=embeddings
# )

# 8️⃣ Vérifier le nombre de documents
print("Nombre de documents dans Chroma :", collection.count())

