from fastapi import APIRouter
from models_user import User
from database import users_collection
from security import hash_password, verify_password, create_access_token
router = APIRouter()


@router.post("/register")
def register_user(user: User):

    existing_user = users_collection.find_one({
        "email": user.email
    })

    if existing_user:
        return {
            "message": "User already exists"
        }

    hashed_password = hash_password(user.password)

    users_collection.insert_one({
        "email": user.email,
        "password": hashed_password
    })

    return {
        "message": "User registered successfully"
    }


@router.post("/login")
def login_user(user: User):

    existing_user = users_collection.find_one({
        "email": user.email
    })

    if not existing_user:
        return {
            "message": "Invalid email or password"
        }

    password_correct = verify_password(
        user.password,
        existing_user["password"]
    )

    if not password_correct:
        return {
            "message": "Invalid email or password"
        }

    access_token = create_access_token(user.email)

    return {
        "message": "Login successful",
        "access_token": access_token,
        "token_type": "bearer"
    }