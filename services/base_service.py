from models.chat_request import ChatRequest


class BaseService:
    def execute(self, request: ChatRequest):
        """Overrides chat() here"""
        pass
