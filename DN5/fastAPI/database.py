from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:password@localhost:3306/fastapi_db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
Base = declarative_base()

class RestaurantNames(Base):
    __tablename__= "RestaurantNamesTable"
    id = Column(Integer, primary_key=True)
    restaurant_name = Column(String(100))

class RestaurantRatings(Base):
    __tablename__= "RestaurantRatingsTable"
    id = Column(Integer, primary_key=True)
    restaurant_id = Column(Integer)
    rating = Column(Integer)