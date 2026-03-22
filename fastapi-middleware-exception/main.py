from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import json

app = FastAPI()

@app.get("/hello")
async def get_sample():
    return {"Hello, Welcome to FastAPI!"}

class custombackenderror(Exception):
    def __init__(self):
        print("reached the exception class")


#@app.exception_handler(custombackenderror)
#async def custom_handler(request:Request, exc: custombackenderror):
#    return JSONResponse (
#        status_code = 404,
#        content = {
#            "message":"The requested resource was not found"
#        }
#    )

@app.middleware("http")
async def middleware_activity(request:Request, call_next):
    try:
       
        if("hello" not in str(request.url)):
            raise custombackenderror()

        print(str(request.method) + str(request.base_url))
        print("before the request is processed")

        response = await call_next(request)

        print("after the response is returned")

        return response
    except custombackenderror:
        return JSONResponse (
         status_code = 404,
         content = {
             "message":"The requested resource was not found"
        }
     ) 


