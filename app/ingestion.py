from langchain_community.document_loaders import PyPDFLoader

def load_documents():
    file_path = "data/HR_Policy2.pdf"
    loader = PyPDFLoader(file_path)
    docs = loader.load()
    return docs
# docs[0]

# import pprint

# pprint.pp(docs[0].metadata)
# print(docs[0].page_content[:500])