from fastapi import FastAPI, Body
BOOKS = [
    {"title":"Book 1","author":"Manish","category":"math"},
    {"title":"Book 2","author":"Raj","category":"science"},
    {"title":"Book 3","author":"Manish","category":"english"},
    {"title":"Book 4","author":"Raj","category":"math"},
    {"title":"Book 5","author":"Manish","category":"math"},
    {"title":"Book 6","author":"Manish","category":"english"},
]

app = FastAPI()

@app.get("/")
async def hello():
    return {'msg':'Hello Manish, How r u?'}

@app.get("/books")
async def read_all_books():
    return BOOKS

# Static Endpoints - Such endpoints must be declared above dynamic ones
@app.get("/books/science")
async def read_science_books():
    return list(filter(lambda item: item["category"] == "science",BOOKS))

# Dynamic Endpoint - Such endpoints must be declared below static ones
@app.get("/books/{category}") #Path Parameter
async def category_books(category: str):
    return list(filter(lambda item: item["category"] == str(category),BOOKS))

@app.get("/books/") #Query Parameter
async def books_by_author(author:str):
    return list(filter(lambda item: item["author"] == author,BOOKS))

@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)

    return BOOKS

@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book
            
    return BOOKS

@app.delete("/books/delete_book")
async def delete_book(deleted_book=Body()):
    BOOKS.remove(list(filter(lambda item: item["title"] == deleted_book["title"],BOOKS))[0])
    return BOOKS