from fastapi import FastAPI
app = FastAPI()
@app.post("/endpoint")
async def read_item(string: str):
    return {"string": string}
