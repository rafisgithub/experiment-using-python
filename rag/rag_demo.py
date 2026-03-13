# Install required packages first (if not installed)
# pip install langchain-openai langchain-community faiss-cpu

import os
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# 1. Your OpenAI API key
os.environ["OPENAI_API_KEY"] = "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"

# 2. Sample documents
documents = [
    "Python is a popular programming language known for its readability and versatility.",
    "RAG stands for Retrieval-Augmented Generation and combines a retriever with a generative model.",
    "LangChain is a Python framework that makes it easy to build applications with LLMs."
]

# 3. Create embeddings and vector store
embeddings = OpenAIEmbeddings()
vector_store = FAISS.from_texts(documents, embeddings)

# 4. Set up retriever
retriever = vector_store.as_retriever()

# 5. Create RAG chain using LCEL (LangChain Expression Language)
template = """Answer the question based only on the following context:
{context}

Question: {question}
"""
prompt = ChatPromptTemplate.from_template(template)
llm = ChatOpenAI(temperature=0)

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

# 6. Ask a question
query = "What is RAG?"
answer = rag_chain.invoke(query)
print("Answer:", answer)