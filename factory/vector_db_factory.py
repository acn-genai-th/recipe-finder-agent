from typing import Union, Callable

from langchain.vectorstores.azuresearch import AzureSearch
from config import azure_base_endpoint, azure_search_key
from langchain_core.embeddings import Embeddings


def init_vector_db(index_name: str, embedding_function: Union[Callable, Embeddings]) -> AzureSearch:
    return AzureSearch(
        azure_search_endpoint=azure_base_endpoint,
        azure_search_key=azure_search_key,
        index_name=index_name,
        embedding_function=embedding_function,
    )
