from fastapi import FastAPI
from database import todos_collection
from fastapi.middleware.cors import CORSMiddleware
from routes.todos import router as todos_router
from routes.users import router as user_router

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "Todo API is running"}
app.include_router(todos_router)
app.include_router(user_router)

@app.get("/test-db")
def test_database():
    todos_collection.find_one()
    return{"message":"Mongo DB Connected successfully",
           "database":"todo_database"}
