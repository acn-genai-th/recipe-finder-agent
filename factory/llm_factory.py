from langchain_core.language_models import BaseChatModel
from langchain_openai import AzureChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI

from common.constants import OPEN_AI
from config import llm_provider, openai_api_version, azure_deployment


def init_llm() -> BaseChatModel:
    _llm_provider = llm_provider
    if _llm_provider == OPEN_AI:
        return AzureChatOpenAI(
            openai_api_version=openai_api_version,
            azure_deployment=azure_deployment,
        )
    else:
        return ChatGoogleGenerativeAI(model="gemini-pro")
