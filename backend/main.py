from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import math
import uvicorn
import httpx

app = FastAPI()

app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:5173"], 
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
)


@app.get("/InfoData")
async def get_info_data( page: int = Query(1, ge=1)):
    api_url = f"https://dragonball-api.com/api/characters?page={page}"
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(api_url)
            response.raise_for_status()
            data = response.json()
            return data
    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail="Error en la APi externa")    
    
    
@app.get("/infoDataCharacter")
async def get_info_data_character( id: int = Query(1, ge=1)):
    api_url = f"https://dragonball-api.com/api/characters/{id}"
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(api_url)
            response.raise_for_status()
            data = response.json()
            return data
    except httpx.HTTPError as e:
        return {"error": str(e)}
    