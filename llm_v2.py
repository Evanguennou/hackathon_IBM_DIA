from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from chromadb.utils import Settings

embedding_function = HuggingFaceEmbeddings(model_name="intfloat/multilingual-e5-base")

vectordb = Chroma(
    client_settings=Settings(
        chroma_server_host="localhost",   
        chroma_server_http_port=8000      
    ),
    embedding_function=embedding_function,
    collection_name="ma_collection"
)

retriever = vectordb.as_retriever(search_kwargs={"k": 1})