from typing import List
from haystack import Document
from haystack.components.builders import PromptBuilder


class RAGPromptBuilder():

    def __init__(self):

        self._template ="""Given these documents, answer the question.
              Documents:
              {% for doc in documents %}
                  {{ doc.content }}
              {% endfor %}
              Question: {{query}}
              Answer:"""        

        self._prompt_builder = PromptBuilder(template=self._template)
    
    def run_prompt_builder(
            self,
            query: str,
            documents: List[Document]
    ) -> str:
        
        prompt = self._prompt_builder.run(
            query=query,
            documents=documents
        )

        return prompt["prompt"]