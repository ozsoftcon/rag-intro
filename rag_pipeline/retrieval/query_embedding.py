
from typing import List
from haystack_integrations.components.embedders.ollama import OllamaTextEmbedder

class QueryEmbedder():

    def __init__(
            self,
            embedding_model: str,
            embedding_endpoint: str
    ):
        
        self._embedder = OllamaTextEmbedder(
            model=embedding_model,
            url=embedding_endpoint
        )

    def run_embedding(self, query: str) -> List[float]:

        embedding = self._embedder.run(
            text=query
        )

        return embedding["embedding"]