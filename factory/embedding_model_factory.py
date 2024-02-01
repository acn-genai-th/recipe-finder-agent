from langchain_openai import AzureOpenAIEmbeddings
from langchain_core.embeddings import Embeddings
from config import azure_openai_embedding_deployment_model, azure_openai_embedding_chunk_size


def init_embedding_model() -> Embeddings:
    return AzureOpenAIEmbeddings(
        deployment=azure_openai_embedding_deployment_model,
        chunk_size=azure_openai_embedding_chunk_size,
    )
