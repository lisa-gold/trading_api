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
collection = None
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
        for pos in data:
            positions.append({
                "name": pos.get("name", "-"),
                "position_t1": pos.get("position_t1", "-"),
                "time_t1": pos.get("time_t1"),
                "position_t2": pos.get("position_t2", "-"),
                "time_t2": pos.get("time_t2")
                })
    except Exception as e:
        positions = f"Error: {e}"

    return positions


@app.get("/instruments/{terminal}/{instrument_name}")
async def get_instrument_position(terminal, instrument_name):
    data = collection.find_one({"name": instrument_name})
    if data:
        return int(data[f"position__t{terminal}"])
    return "no such instrument"


@app.post("/instruments")
async def add_position(terminal, name, position):
    now = datetime.datetime.now()

    instrument_position = {
        "name": name,
        f"position_t{terminal}": int(position),
        f"time_t{terminal}": now
    }

    if collection.find_one({"name": name}):
        collection.update_one({"name": name},
                              {"$set": {
                                  f"position_t{terminal}": position,
                                  f"time_t{terminal}": now
                                  }
                               })
        print("updated ", name)
    else:
        collection.insert_one(instrument_position)
        print("added new instrument ", name)

    return instrument_position
