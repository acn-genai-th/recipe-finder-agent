from typing import Dict
from fastapi import HTTPException, status
from langchain_openai import OpenAIEmbeddings
from models.chat_request import ChatRequest
from services.base_service import BaseService
from factory.embedding_model_factory import init_embedding_model
from langchain_community.vectorstores.azuresearch import AzureSearch
from factory.vector_db_factory import init_vector_db
from factory.llm_factory import init_llm
from config import (
    azure_food_recipes_index,
    food_tool_prompt_description,
    drink_tool_prompt_description,
    azure_drink_recipes_index,
)
from langchain_community.tools import Tool
from langchain.agents import load_tools, initialize_agent, AgentType
from langchain_community.agent_toolkits.openapi.spec import reduce_openapi_spec
import yaml
from langchain_community.agent_toolkits.openapi import planner
from langchain.requests import RequestsWrapper
from langchain.agents.agent import AgentExecutor
from langchain_core.messages import AIMessage, HumanMessage


class ChatService(BaseService):
    def execute(self, request: ChatRequest):
        llm = init_llm()

        embeddings: OpenAIEmbeddings = init_embedding_model()
        food_vector_store: AzureSearch = init_vector_db(
            index_name=azure_food_recipes_index,
            embedding_function=embeddings.embed_query,
        )

        drink_vector_store: AzureSearch = init_vector_db(
            index_name=azure_drink_recipes_index,
            embedding_function=embeddings.embed_query,
        )

        with open("openai_openapi.yaml") as f:
            raw_spotify_api_spec = yaml.load(f, Loader=yaml.Loader)
        api_spec = reduce_openapi_spec(spec=raw_spotify_api_spec)

        openai_agent = planner.create_openapi_agent(
            api_spec, RequestsWrapper(headers={}), llm
        )

        # TODO: 2.1 - To create a tools for agent
        food_recipes_tool = Tool(
            name="Food Recipes Index",
            func=food_vector_store.vector_search,
            description=food_tool_prompt_description,
        )

        drink_recipes_tool = Tool(
            name="Drink Recipes Index",
            func=drink_vector_store.vector_search,
            description=drink_tool_prompt_description,
        )

        openai_api_spec = Tool(
            name="Order Microservice",
            func=openai_agent.run,
            description="Order Microservice, that allows user to call an api and create order, no search of products needed, just call place order api, with action: \"place_order\", food_name and quantity specified in json format",
        )

        tools = [food_recipes_tool, drink_recipes_tool, openai_api_spec]

        # TODO: 2.2 - To create an agent
        agent_executor: AgentExecutor = initialize_agent(
            tools=tools,
            llm=llm,
            agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
            verbose=True,
        )

        # TODO: 2.3 - Create prompt template (which included chatHistory)

        # TODO: 2.4 - Invoke an agent
        if len(request.messages) == 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="No messages provided",
            )
        last_message = request.messages[request.messages.count("count") - 1]

        chat_history = []

        for message in request.messages:
            if message.role == "user":
                chat_history.append(HumanMessage(content=message.content))
            elif message.role == "assistant":
                chat_history.append(AIMessage(content=message.content))

        res: Dict = agent_executor.invoke(
            {
                "input": last_message.content,
                "chat_history": chat_history,
            }
        )

        return res.get("output", res)
