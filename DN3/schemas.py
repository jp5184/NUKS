from pydantic import BaseModel

class RestaurantNames(BaseModel):
    restaurant_name: str

class RestaurantRatings(BaseModel):
    restaurant_id: int
    rating: int