from fastapi import FastAPI
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
@app.get("/books/{category}")
async def category_books(category: str):
    return list(filter(lambda item: item["category"] == str(category),BOOKS))

@app.get("/books/")
async def books_by_author(author:str):
    return list(filter(lambda item: item["author"] == author,BOOKS))
