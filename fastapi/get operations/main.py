#the key parts of a get operation in fastapi are
"""
Host: eg:www.google.com
Path: /search
Port:eg: 80
Query String: ?q=fqastapi
"""

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello, World!"}

