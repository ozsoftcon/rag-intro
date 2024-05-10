
from typing import List
from haystack import Document
from haystack_integrations.components.retrievers.chroma import ChromaEmbeddingRetriever
from haystack_integrations.document_stores.chroma import ChromaDocumentStore

class DocumentRetriever():

    def __init__(
            self,
            persist_path: str,
            collection_name:str,
            top_k: int
    ):
        self._document_store = ChromaDocumentStore(
            collection_name=collection_name,
            persist_path=persist_path
        )

        self._top_k = top_k

        self._document_retriever = ChromaEmbeddingRetriever(
            document_store=self._document_store
        )

    def retrieve_documents(
            self,
            embedding: List[float]
    )->List[Document]:
        
        retrieved_documents = self._document_retriever.run(
            query_embedding=embedding,
            top_k = self._top_k
        )

        return retrieved_documents["documents"]