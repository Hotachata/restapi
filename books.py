from fastapi import FastAPI                 # importamos fastapi

app = FastAPI()                             # importamos fastapi como una variable dentro de nuestra aplicacion

@app.get("/")
async def first_api():                      # async (asynchronous) no es necesario para fastapi
    return{"message": "Hello!"}

# uvicorn Books:app --reload
# http://127.0.0.1:8000
# http://127.0.0.1:8000/docs 
# http://127.0.0.1:8000/redoc

books = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]

@app.get("/books")
async def get_all_books():
    return books

@app.get("/books/{book_title}")                             # path parameter
async def get_book_with_title(book_title: str):
    for book in books:
        if book.get('title').casefold() == book_title:      # .casefold() forces lower case
            return book                                     # return the book in the path param