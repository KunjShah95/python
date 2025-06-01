from pydantic import BaseModel, Field
from fastapi import FastAPI,HTTPException

app= FastAPI()

class Book(BaseModel):
    title: str
    author:str
    books= [
        {"title": "1984", "author": "George Orwell"},
        {"title": "To Kill a Mockingbird", "author": "Harper Lee"},
        {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
        {"title": "Pride and Prejudice", "author": "Jane Austen"},
    ]

@app.put("/books/{book_id}")
def update_book(book_id: int, book: Book):
    for b in books:
        if b["id"] == book_id:
            b["title"] = book.title
            b["author"] = book.author
            return b
    raise HTTPException(status_code=404, detail="Book not found")