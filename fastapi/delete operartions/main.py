from fastapi import FastAPI, HTTPException

app = FastAPI()

books = [
    {"id": 1, "title": "Book One", "author": "Author A"},
    {"id": 2, "title": "Book Two", "author": "Author B"}
]

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for i, b in enumerate(books):
        if b["id"] == book_id:
            deleted = books.pop(i)
            return deleted
    raise HTTPException(status_code=404, detail="Book not found")