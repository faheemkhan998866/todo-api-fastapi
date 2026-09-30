from fastapi import APIRouter, Depends
from bson import ObjectId

from models import Todo
from database import todos_collection
from security import get_current_user

router = APIRouter()


# CREATE TODO
@router.post("/todos")
def create_todo(
    todo: Todo,
    current_user: str = Depends(get_current_user)
):
    todo_data = todo.model_dump()

    todos_collection.insert_one(todo_data)

    return {
        "message": "Todo created successfully",
        "title": todo.title,
        "completed": todo.completed
    }


# GET TODOS
@router.get("/todos")
def get_todos(
    current_user: str = Depends(get_current_user)
):
    todos = list(todos_collection.find())

    for todo in todos:
        todo["_id"] = str(todo["_id"])

    return todos


# UPDATE TODO
@router.put("/todos/{todo_id}")
def update_todo(
    todo_id: str,
    todo: Todo,
    current_user: str = Depends(get_current_user)
):
    result = todos_collection.update_one(
        {"_id": ObjectId(todo_id)},
        {"$set": todo.model_dump()}
    )

    if result.matched_count == 0:
        return {
            "message": "Todo not found"
        }

    return {
        "message": "Todo updated successfully"
    }


# DELETE TODO
@router.delete("/todos/{todo_id}")
def delete_todo(
    todo_id: str,
    current_user: str = Depends(get_current_user)
):
    result = todos_collection.delete_one(
        {"_id": ObjectId(todo_id)}
    )

    if result.deleted_count == 0:
        return {
            "message": "Todo not found"
        }

    return {
        "message": "Todo deleted successfully"
    }