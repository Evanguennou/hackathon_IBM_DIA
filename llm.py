from langchain_community.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings

persist_directory = "C:\\Users\\ihadi\\Desktop\\Semestre 9\\BI Pipeline\\hackathon_IBM_DIA\\chroma_db"

embedding_function = HuggingFaceEmbeddings(model_name="intfloat/multilingual-e5-base")

vectordb = Chroma(
    persist_directory=persist_directory,
    embedding_function=embedding_function,
    collection_name="my_multilingual_rag"
)
