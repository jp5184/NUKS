from typing import Union
from fastapi import FastAPI, status
from database import engine, Base, RestaurantNames, RestaurantRatings
from sqlalchemy.orm import Session
app = FastAPI()

Base.metadata.create_all(engine)    #Generira bazo
import schemas

import requests
import json

from fastapi.middleware.cors import CORSMiddleware

# Configure CORS settings
origins = [
    "http://localhost",
    "http://0.0.0.0:8080",
    "http://localhost:8080",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return "Restaurant rating app"

@app.post("/addRestaurant", status_code=status.HTTP_201_CREATED)
def add_restaurant(restaurant: schemas.RestaurantNames):
    """
        API call for adding restaurants
    """
    session = Session(bind = engine, expire_on_commit = False)
    restaurantNamesDB = RestaurantNames(restaurant_name = restaurant.restaurant_name)
    session.add(restaurantNamesDB)
    session.commit()
    id = restaurantNamesDB.id
    session.close()

    return f"Created new restaurant item with id {id}"

@app.post("/addRestaurantRating", status_code=status.HTTP_201_CREATED)
def add_restaurant(restaurantRating: schemas.RestaurantRatings):
    """
        API call for adding restaurant ratings
    """
    session = Session(bind = engine, expire_on_commit = False)
    restaurantRatingsDB = RestaurantRatings(restaurant_id = restaurantRating.restaurant_id, rating = restaurantRating.rating)
    session.add(restaurantRatingsDB)
    session.commit()
    id = restaurantRatingsDB.id
    session.close()

    return f"Added a new rating restaurant item with id {id}"

@app.get("/getRestaurantNameList", status_code=status.HTTP_200_OK)
def get_restaurant_name_list():
    """
    API call for getting a list of restaurant names
    """
    db = Session(bind=engine, expire_on_commit=False)
    restaurants = db.query(RestaurantNames).all()
    db.close()

    return restaurants

@app.get("/getRestaurantRatingList", status_code=status.HTTP_200_OK)
def get_restaurant_rating_list():
    """
    API call for getting a list of restaurant ratings
    """
    db = Session(bind=engine, expire_on_commit=False)
    ratings = db.query(RestaurantRatings).all()
    db.close()

    return ratings


# Calls the docker service that sorts the list (returns a sorted JSON)
@app.get("/getSortedRestaurantList", status_code=status.HTTP_200_OK)
def get_sorted_restaurants():
    """
    API call for getting a sorted list of restaurants with ratings
    """
    url = 'http://localhost:8080/function/restaurant-sort'

    # make the API call to the Docker container
    response = requests.get(url)

    # parse the JSON response
    sorted_restaurants = json.loads(response.content)

    return sorted_restaurants