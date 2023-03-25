from typing import Union
from fastapi import FastAPI
from database import engine, Base, RestaurantNames, RestaurantRatings
from sqlalchemy.orm import Session
app = FastAPI()

Base.metadata.create_all(engine)    #Generira bazo
import schemas

@app.get("/")
async def root():
    return "Restaurant rating app"

@app.post("/addRestaurant")
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

@app.post("/addRestaurantRating")
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

@app.get("/getRestaurantNameList")
def get_restaurant_name_list():
    """
    API call for getting a list of restaurant names
    """
    db = Session(bind=engine, expire_on_commit=False)
    restaurants = db.query(RestaurantNames).all()
    db.close()

    return restaurants

@app.get("/getRestaurantRatingList")
def get_restaurant_rating_list():
    """
    API call for getting a list of restaurant ratings
    """
    db = Session(bind=engine, expire_on_commit=False)
    ratings = db.query(RestaurantRatings).all()
    db.close()

    return ratings
