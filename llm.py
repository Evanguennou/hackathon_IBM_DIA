from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chains import retrieval_qa
from transformers import pipeline
from langchain_community.llms.huggingface_pipeline import HuggingFacePipeline
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory

persist_directory = "C:\\Users\\ihadi\\Desktop\\Semestre 9\\BI Pipeline\\hackathon_IBM_DIA\\chroma_db"

embedding_function = HuggingFaceEmbeddings(model_name="intfloat/multilingual-e5-base")

vectordb = Chroma(
    persist_directory=persist_directory,
    embedding_function=embedding_function,
    collection_name="my_multilingual_rag"
)

retriever = vectordb.as_retriever(search_kwargs={"k": 3})

model_id = "bigscience/bloomz-560m" 

pipe = pipeline(
    task="text-generation",
    model=model_id,
    tokenizer=model_id,
    max_new_tokens=256,
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
        memory=memory
    )

def generate_response(question):
    response = qa_chain.invoke(question)
    return response#.get('answer', '')

print(generate_response("infos sur les échanges universitaires"))