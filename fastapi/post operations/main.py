from pydantic import BaseModel
from fastapi import FastAPI
class Review(BaseModel):
    id:int
    text:str
    public: bool= False

class MovieReview(BaseModel):
        movie:str
        #Nest Review inside MovieReview
        review: Review

@app.post("/reviews", response_model=DbReview)
def create_review(review: MovieReview):
      #Persist the review to the database
      db_review= crud.create_review(review)
      #Return the review includig the id
      return db_review

