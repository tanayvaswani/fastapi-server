from fastapi import FastAPI

app = FastAPI()

@app.get('/health')
async def read_root():
    return { "status": "UP" }