from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chains import retrieval_qa
from transformers import pipeline
from langchain_community.llms.huggingface_pipeline import HuggingFacePipeline
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from chromadb.config import Settings

# 🔹 Template qui force le français et intègre le contexte récupéré par le retriever
template = """Réponds toujours en français.
Utilise uniquement les informations fournies dans le contexte pour répondre.
Si tu ne sais pas, dis que tu ne sais pas.

Contexte : {context}

Question : {question}

Réponse en français :""".format(context="{context}", question="{question}")

prompt = PromptTemplate(
    input_variables=["context", "question"],
    template=template
)

persist_directory = "C:\\Users\\ihadi\\Desktop\\Semestre 9\\BI Pipeline\\hackathon_IBM_DIA\\chroma_db"

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

model_id = "dimad000/gpt2-base-french_10" #"bigscience/bloomz-560m" 

pipe = pipeline(
    task="text-generation", 
    model=model_id,
    tokenizer=model_id,
    max_new_tokens=50,
    temperature=0.7
)

memory = ConversationBufferMemory(
    memory_key="chat_history",  # clé utilisée dans la chaîne
    return_messages=True
)

llm = HuggingFacePipeline(pipeline=pipe)

qa_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    memory=memory,
    condense_question_prompt=prompt
)


def generate_response(question):
    response = qa_chain.invoke(question, return_only_outputs=True)
    return str(response)

print(generate_response("Es que les alternants doivent payer la CVEC ?"))