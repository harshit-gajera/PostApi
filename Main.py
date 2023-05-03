from fastapi import FastAPI
app = FastAPI()
@app.post("/endpoint/{string}")
async def read_item(string):
    return {"string": string}
