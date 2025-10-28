import sys
sys.path.append("../")

from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores.faiss import FAISS
from langchain_core.documents import Document

from pathlib import Path
from dotenv import load_dotenv, find_dotenv
import pandas as pd
import os


_ = load_dotenv(find_dotenv())


def create_documents(path_to_file):
    df = pd.read_excel(path_to_file)
    loaded_docs = []
    for index, row in df.iterrows():
        page_content = f"""Node type: {row['Component']}. {row['Definition']} Example: {row['Example(s)']}"""
        metadata = row.to_dict()
        metadata['row'] = index
        metadata['source'] = path_to_file
        
        doc = Document(page_content=page_content, metadata=metadata)
        loaded_docs.append(doc)
    
    return loaded_docs


def vector_store(loaded_docs):
    local_vector = Path("FaissMutOp")
    embedding_model = OpenAIEmbeddings(model="text-embedding-3-large")
    if not local_vector.exists():
        vector_store = FAISS.from_documents(
            documents=loaded_docs,
            embedding=embedding_model
        )
        vector_store.save_local("FaissMutOp")
    else: 
        vector_store = FAISS.load_local(
            folder_path="FaissMutOp",
            embeddings=embedding_model,
            allow_dangerous_deserialization=True)

    retriever = vector_store.as_retriever(
        search_type = "similarity",
        search_kwargs = {"k": 1}
    )
    return retriever


def build_retriever(EXCEL_MUT_OP_PATH: str):
    _ = load_dotenv(find_dotenv())

    api_openai = os.getenv('OPENAI_API_KEY')
    if api_openai:
        print('OpenAI API loaded.')
    else:
        print('missing api key: OPEN_API_KEY')
        raise("You must provide OpenAI API key")
        return

    loaded_docs = create_documents(EXCEL_MUT_OP_PATH)
    retriever = vector_store(loaded_docs)

    return retriever