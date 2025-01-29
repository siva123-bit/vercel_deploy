from fastapi import FastAPI,Query
from fastapi.responses import  JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import json 

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

with open('q-vercel-python.json' , 'r') as file:
    data = json.load(file)

@app.get("/api")
async def get_marks(names: list[str]= Query([])):
    response=[]
    for person in data:
        if str(person["name"]) in names:
            response.append(person["marks"])
    return JSONResponse(content={"marks" : response})
