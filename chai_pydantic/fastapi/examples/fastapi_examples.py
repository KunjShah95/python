from fastapi import FastAPI,Depends
from pydantic import BaseModel, EmailStr

app= FastAPI()

class UserSignup(BaseModel):
    username: str
    email: EmailStr
    password: str
    
class Settings(BaseModel):
    app_name: str = "Chai App"
    admin_email: EmailStr = "admin@chai.com"
    
    
def get_settings():
    return Settings()

@app.post("/signup")
def signup(user:UserSignup):
    return {"message": f"User {user.username} signed up successfully!", "email": user.email}

@app.get("/settings")
def read_settings(settings: Settings = Depends(get_settings)):
    return {
        "app_name": settings.app_name,
        "admin_email": settings.admin_email
    }
    
@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}   
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)