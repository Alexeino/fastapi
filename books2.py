from fastapi import FastAPI, Path, Query, HTTPException
from models import Book, BookRequest
from starlette import status as st

app = FastAPI()


BOOKS = [
    Book(1,"CS 1","Manish","Nice Book",4,2022),
    Book(2,"CS 2","Manish","Awesome Book",5,2012),
    Book(3,"CS 3","Manish","Great Book",4,2023),
    Book(4,"CS 4","Raj","Awesome Book",5,2015),
    Book(5,"CS 5","Manish","Awesome Book",3,2021),
]


@app.get("/books")
async def read_all_books():
    return BOOKS

@app.get("/books/book_id",status_code=st.HTTP_200_OK)
async def read_book(book_id: int):
    for book in BOOKS:
        if book.id == book_id:
            return book
    else:
        return HTTPException(status_code=404,detail="Item not found!")
        
    

@app.post("/create_book",status_code=st.HTTP_201_CREATED)
async def create_book(book_request: BookRequest):
    # It's just like serializing incoming data by BookRequest
    new_book = Book(**book_request.model_dump())
    BOOKS.append(find_book_id(new_book))
    
    
def find_book_id(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book

@app.get("/books/published_date")
async def read_books(published_date: int):
    return list(filter(lambda item: item.published_date == published_date,BOOKS))

@app.get("/books/{author}")
async def read_books_by_author(author: str = Path(min_length=2,description="Minimum 2 characters must be provided")): # Path Validator
    return list(filter(lambda item: author in item.author,BOOKS))

@app.get("/books/")
async def read_books_by_published_date(published_at: int = Query(gt=1999,lt=2023,description="Must be between 1999 and 2023")):
    return list(filter(lambda item: item.published_date == published_at,BOOKS))