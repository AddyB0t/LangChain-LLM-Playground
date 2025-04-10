from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader


loader=PyPDFLoader('chains/dl-curriculum.pdf')

docs=loader.load()


splitter=CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separator='\n'
)

result=splitter.split_documents(docs)

print(result)
