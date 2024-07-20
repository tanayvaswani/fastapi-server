from fastapi import FastAPI

app = FastAPI()

@app.get('/health')
async def read_root():
    return { "status": "UP" }

@app.get('/greet/{username}')
async def greet(username: str):
   return { "message": f"Hello {username}!!!" }