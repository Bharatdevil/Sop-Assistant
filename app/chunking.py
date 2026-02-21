from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_documents(docs):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=350, chunk_overlap=0)
    chunks = text_splitter.split_documents(docs)
    return chunks