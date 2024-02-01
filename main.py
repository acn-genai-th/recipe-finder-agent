from fastapi import FastAPI

from config import get_configs
from routers import chat

get_configs()
app = FastAPI()

app.include_router(chat.router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=7071)
