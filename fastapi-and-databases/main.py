from fastapi import FastAPI, Query, Path, Depends
from pydantic import BaseModel, Field
import json
from db import engine


app = FastAPI()

class searchqueryvalues(BaseModel):
    q1: str = Field(...,min_length=3)
    q2: int = Field(...,gt=0)


@app.get("/search")
def searchme(params: searchqueryvalues = Query()):
    return{
        "q1":params.q1,
        "q2" : params.q2

    }

@app.get("/books/{bookid}")
def getstudents(bookid: str = Path(...,description="pass a Book ID")):
    try :
        with open('schema.json', 'r') as f:
            data = json.load(f)
            return data[bookid]
    
    except Exception as e:
        return ("error details: " + str(e))



