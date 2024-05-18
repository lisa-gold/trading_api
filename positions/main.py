from fastapi import FastAPI
from pymongo import MongoClient
import os
from dotenv import load_dotenv
import datetime


load_dotenv()


USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
DB = os.getenv("DB")


app = FastAPI()


status = 'started'
try:
    cluster = MongoClient(f"mongodb+srv://{USERNAME}:{PASSWORD}@{DB}")
    db = cluster['trading']
    collection = db['positions']
    status = 'connected'
except Exception as e:
    status = 'no connection with the db'
    print('no connection with the db ', e)


@app.get("/")
def index():
    return status


@app.get("/instruments")
async def get_instruments_positions():

    positions = []
    try:
        data = collection.find({})
    except  Exception as e:
        positions = f"Error: {e}"

    for pos in data:
        positions.append({
            pos["name"]: pos["position"],
            "time": pos["time"]
            })

    return positions


@app.get("/instruments/{instrument_name}")
async def get_instrument_position(instrument_name):
    data = collection.find_one({"name": instrument_name})
    if data:
        return int(data["position"])
    return "no such instrument"


@app.post("/instruments")
async def add_position(name, position):
    now = datetime.datetime.now()

    instrument_position = {
        "name": name,
        "position": int(position),
        "time": now
    }

    if collection.find_one({"name": name}):
        collection.update_one({"name": name},
                              {"$set": {
                                  "position": position,
                                  "time": now
                              }})
        print("updated ", name)
    else:
        collection.insert_one(instrument_position)
        print('added new instrument ', name)

    return instrument_position
