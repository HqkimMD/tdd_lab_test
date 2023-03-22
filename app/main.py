from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

class NameRequest(BaseModel):
    name: str
    
@app.get("/")
def read_root():
    return {"Hello": "World1"}

# @app.get("/callname/{name}")
# def read_root():
#     return {"Hello": "hakim"}

@app.get("/callname/{name}")
def read_name(name: str = None):
    return {"hello": name}

@app.post("/callname", response_model=dict)
def call_name(request: NameRequest):
    return {"hello": request.name}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str = None):
#     return {"item_id": item_id, "q": q}

# @app.get("/hello/{name}")
# def read_name(name: str = None):
#     return {"hello": name}

handler = Mangum(app)
