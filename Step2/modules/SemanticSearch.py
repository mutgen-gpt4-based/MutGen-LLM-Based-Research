from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores.faiss import FAISS
import pandas as pd

class SemanticSearch:
    def __init__(self):
        embedding_model = OpenAIEmbeddings(model="text-embedding-3-large")
        complete_vector_store = FAISS.load_local(
                    folder_path="CleanTrainDataset",
                    embeddings=embedding_model,
                    allow_dangerous_deserialization=True)
        self.retriever = complete_vector_store.as_retriever(search_type = "similarity", search_kwargs = {"k": 1})


    def run_search(self, ref_tp):
        rag = self.retriever.invoke(ref_tp)
        most_similar_fixed_code_from_train_dataset = rag[0].page_content
        correlated_buggy_code_from_train_dataset = rag[0].metadata["buggy_train_version"]
        gumtree_diff = rag[0].metadata["gumtree_diff"]
        
        return {
            "fixed_train_data": most_similar_fixed_code_from_train_dataset,
            "buggy_train_data": correlated_buggy_code_from_train_dataset,
            "gumtree_diff": gumtree_diff
            }
    

    def collect_batch(self, df):
        all_fixed = list(df["fixed"])
        results = self.retriever.batch(all_fixed)

        list_docs_info = []
        for doc in results:
            new_dict = {}
            new_dict["fixed_train"] = doc[0].page_content
            new_dict["buggy_train"] = doc[0].metadata["buggy_train_version"]
            new_dict["gumtree_diff"] = doc[0].metadata["gumtree_diff"]
            list_docs_info.append(new_dict)
        
        return list_docs_info



        
