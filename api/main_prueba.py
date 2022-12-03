from fastapi import *
from fastapi.security import *
from fastapi.middleware.cors import CORSMiddleware
from typing import Union
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from joblib import *
import numpy as np
import pandas as pd

app = FastAPI()

origins = ["*"]

bike_data = pd.read_csv("daily-bike-share.csv")
x = bike_data[['season', 'mnth', 'holiday',
               'weekday', 'workingday', 'weathersit', 'temp', 'atemp', 'hum', 'windspeed']].values
y = bike_data['rentals'].values

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.30, random_state=0)

model = LinearRegression().fit(x_train , y_train)
predictions = model.predict(x_test)

print(x_test[0])
print(predictions[0])


dump(model, 'model.joblib') 

model_load = load('model.joblib') 
predictions = model_load.predict(x_test)
print(predictions[:2])

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
async def get_saludo():
    mensaje = "hola mundo"
    return mensaje
