
from os import environ
from .query_embedding import QueryEmbedder
from .prompt_builder import RAGPromptBuilder
from .document_retrieval import DocumentRetriever
from haystack_integrations.components.generators.ollama import OllamaGenerator


LANGUAGE_MODEL = environ.get("LANGUAGE_MODEL", "mistral")
EMBEDDER_ENDPOINT = environ.get(
    "EMBEDDING_ENDPOINT", "http://localhost:11434/api/embeddings")

GENERATOR_ENDPOINT = environ.get(
    "GENERATOR_ENDPOINT", "http://localhost:11434/api/generate"
)

RETRIEVAL_TOP_K = 20

class RAGPipeline():

    def __init__(
            self,
            persist_path: str,
            collection_name: str,
            top_k: int = RETRIEVAL_TOP_K
    ):
        self._top_k = top_k
        self._query_embedder = QueryEmbedder(
            embedding_model=LANGUAGE_MODEL,
            embedding_endpoint=EMBEDDER_ENDPOINT
        )

        self._document_retriever = DocumentRetriever(
            persist_path=persist_path,
            collection_name=collection_name,
            top_k = self._top_k
        )

        self._prompt_builder = RAGPromptBuilder()

        self._generator = OllamaGenerator(model=LANGUAGE_MODEL, url=GENERATOR_ENDPOINT)

    def run_rag(
            self,
            query

    ):
        query_embedding = self._query_embedder.run_embedding(query=query)
        documents = self._document_retriever.retrieve_documents(embedding=query_embedding)
        prompt = self._prompt_builder.run_prompt_builder(query=query, documents=documents)

        generated_text = self._generator.run(
            prompt = prompt,
        )

        replies = generated_text["replies"]

        movies = [(doc.meta["title"], doc.content) for doc in documents]

        return replies, movies

