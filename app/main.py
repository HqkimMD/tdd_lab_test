from fastapi import FastAPI, Form
from mangum import Mangum 

app = FastAPI()

# class NameRequest(BaseModel):
#     name: str
    
@app.get("/")
def read_root():
    return {"Hello": "World1"}

@app.get("/callname/{name}")
def read_name(name: str = None):
    return {"hello": name}

@app.post("/callname")
def call_name(name = "Hakim"):
    return {"hello": name}

handler = Mangum(app)
