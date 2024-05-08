from typing import List
from os import environ

from haystack import Pipeline, Document
from haystack.components.writers import DocumentWriter
from haystack_integrations.document_stores.chroma import ChromaDocumentStore
from haystack_integrations.components.embedders.ollama import OllamaDocumentEmbedder


## we will use a fixed embedding service
## mistral from Ollama

EMBEDDING_MODEL = environ.get("EMBEDDING_MODEL", "mistral")
EMBEDDER_ENDPOINT = environ.get(
    "EMBEDDING_ENDPOINT", "http://localhost:11434/api/embeddings")

class IndexPipeline():

    def __init__(
            self,
            persist_path: str,
            collection_name: str
    ):
        self._persist_path = persist_path

        self._document_store = ChromaDocumentStore(
            collection_name=collection_name,
            persist_path=self._persist_path
        )

        self._embedder = OllamaDocumentEmbedder(
            model=EMBEDDING_MODEL,
            url=EMBEDDER_ENDPOINT
        )
        self._writer = DocumentWriter(self._document_store)
        self._pipeline = Pipeline()
        self._pipeline.add_component("embedder", self._embedder)
        self._pipeline.add_component("writer", self._writer)
        self._pipeline.connect("embedder.documents", "writer.documents")

    def run_pipeline(self, documents: List[Document]):
        
        self._pipeline.run(
            data = {"documents": documents}
        )