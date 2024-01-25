from fastapi import FastAPI
from server import api 

# Initialize the app
app = FastAPI()

app.include_router(api.router)

# GET operation at route '/'
@app.get("/", tags=["Root"])
async def read_api():
    return {"message": "Welcome to XConnections!"}
