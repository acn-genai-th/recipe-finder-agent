import configparser
from functools import lru_cache

from dotenv import load_dotenv


_config_object = configparser.ConfigParser()
_config_object.read("config.ini")
_config_default = _config_object

chat_history_length = _config_default["DEFAULT"]['CHAT_HISTORY_LENGTH']
llm_provider = _config_default["DEFAULT"]['LLM_PROVIDER']
openai_api_version = _config_default['AZURE_OPENAI']['OPENAI_API_VERSION']
azure_deployment = _config_default['AZURE_OPENAI']['AZURE_DEPLOYMENT']
azure_base_endpoint = _config_default['VECTOR_DB']['BASE_ENDPOINT']
azure_search_key = _config_default['VECTOR_DB']['SEARCH_KEY']
azure_drink_recipes_index = _config_default['VECTOR_DB']['DRINK_RECIPES_INDEX']
azure_food_recipes_index = _config_default['VECTOR_DB']['FOOD_RECIPES_INDEX']
azure_openai_embedding_deployment_model = _config_default['EMBEDDING_MODEL']['DEPLOYMENT_MODEL']
azure_openai_embedding_chunk_size = int(_config_default['EMBEDDING_MODEL']['CHUNK_SIZE'])
drink_tool_prompt_description = _config_default['TOOL_PROMPT']['DRINK_RECIPES']
food_tool_prompt_description = _config_default['TOOL_PROMPT']['FOOD_RECIPES']

@lru_cache
def get_runtime_configs():
    config_object = configparser.ConfigParser()
    config_object.read("config.ini")
    return config_object["DEFAULT"]


def get_configs():
    load_dotenv()
