from fastapi import FastAPI
from fastapi import status
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from joblib import load
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
async def get_hello():
    mensaje = {"Hola": 'Mundo'}
    return mensaje


@app.post('/prediccion/{season}/{mnth}/{holiday}/{weekday}/{workingday}/{weathersit}/{temp}/{atemp}/{hum}/{windspeed}',
          status_code=status.HTTP_202_ACCEPTED,
          summary="Get a user",
          description="Get a user",
          tags=["auth"])
async def post_prediccion(season: int, mnth: int, holiday: int, weekday: int, workingday: int, weathersit: int, temp: float, atemp: float, hum: float, windspeed: float):
    model = load("model.joblib")
    data = [season, mnth, holiday, weekday, workingday, weathersit,
            temp, atemp, hum, windspeed]
    prediccion = model.predict([data])
    response = {"Rentas Calculadas": prediccion[0]}
    return response
