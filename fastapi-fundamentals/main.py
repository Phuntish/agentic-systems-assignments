from fastapi import FastAPI, Query, Path
from pydantic import BaseModel, Field


#init Fast API
app = FastAPI()

class SearchParams(BaseModel):
    myname: str = Field(None)
    myage:int = Field(None)

@app.get("/search/{myname}/{myage}")
def search(params: SearchParams = Path()):
    return {
        "name": params.myname,
        "age": params.myage
    }
    