from pydantic import BaseModel, Field
from typing import Optional

class BookRequest(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=3)
    author: str = Field(min_length=2)
    description: str = Field(max_length=100)
    rating: int = Field(gt=-1, lt=6) # 0 to 5
    published_date: int = Field(gt=1999,lt=2024)
    
    class Config:
        json_schema_extra = {
            "example":{
                "title": "A new book",
                "author": "Manish",
                "description": "New book",
                "rating":5,
                "published_date": 2023
            }
        }

class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    published_date: int
    
    
    def __init__(self,id,title,author,description,rating,published_date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date