from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.openai import OpenAI

loader = TextLoader('data/example_data.txt')

documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)

chunks = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings()

vectorstore = FAISS.from_documents(chunks, embeddings)

retriever = vectorstore.as_retriever() 