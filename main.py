from fastapi import FastAPI
from typing import Optional

app = FastAPI()

user_list = [
   "Jerry",
   "Joey",
   "Phil"
]


@app.get('/health')
async def read_root():
    return { "status": "UP" }


@app.get('/greet/{username}')
async def greet(username: str):
   return { "message": f"Hello {username}!!!" }


@app.get('/search')
async def search_for_user(username: str):
    for user in user_list:
        if username in user_list:
            return { "message": f"details for user {username}" }
        else:
            return { "message": "User Not Found" }


@app.get('/greet/')
async def greet(username: Optional[str] = "Tanay"):
   return { "message": f"Hello {username}!" }


