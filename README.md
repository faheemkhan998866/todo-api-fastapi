# Todo API - FastAPI + MongoDB

A beginner-friendly backend Todo API built with **Python, FastAPI, MongoDB, password hashing, and JWT authentication**.

The project also includes a simple HTML page to demonstrate communication between a frontend and the FastAPI backend.

## Features

- Create a Todo
- Get all Todos
- Update a Todo
- Delete a Todo
- User registration
- Secure password hashing with Argon2
- User login
- JWT access token generation
- JWT-protected Todo endpoints
- Simple HTML/JavaScript frontend for Todo operations
- MongoDB database storage

## Technologies Used

- Python
- FastAPI
- MongoDB
- PyMongo
- Pydantic
- pwdlib + Argon2
- PyJWT
- HTML
- JavaScript

## Project Structure

```text
todo-api-fastapi/
│
├── main.py
├── database.py
├── models.py
├── models_user.py
├── security.py
├── test.html
│
├── routes/
│   ├── todos.py
│   └── users.py
│
├── requirements.txt
└── README.md
```

## How the Backend Works

```text
Client / Swagger / HTML
        ↓
      FastAPI
        ↓
     MongoDB
```

Authentication works like this:

```text
Register
   ↓
Password is hashed
   ↓
User saved in MongoDB
   ↓
Login
   ↓
JWT access token
   ↓
Protected Todo endpoints
```

## API Endpoints

### Authentication

| Method | Endpoint | Description |
|---|---|---|
| POST | `/register` | Register a new user |
| POST | `/login` | Login and receive a JWT token |

### Todo

| Method | Endpoint | Description |
|---|---|---|
| POST | `/todos` | Create a Todo |
| GET | `/todos` | Get all Todos |
| PUT | `/todos/{todo_id}` | Update a Todo |
| DELETE | `/todos/{todo_id}` | Delete a Todo |

The Todo endpoints require a valid JWT token.

## Requirements

You need the following installed on your computer:

- Python 3.10+
- MongoDB Server
- MongoDB Compass (optional, for viewing your database)

MongoDB Compass is only a graphical interface. The FastAPI application connects directly to the MongoDB Server.

## Run the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/faheemkhan998866/todo-api-fastapi.git
cd todo-api-fastapi
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv .venv
```

Activate it:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Make sure MongoDB is running

The project uses:

```text
mongodb://localhost:27017/
```

The database used by the project is:

```text
todo_database
```

### 5. Start FastAPI

```bash
uvicorn main:app --reload
```

### 6. Open Swagger UI

Go to:

```text
http://127.0.0.1:8000/docs
```

Swagger UI lets you test all API endpoints directly from your browser.

## Frontend

The repository contains `test.html`, a simple HTML/JavaScript frontend.

The HTML page sends requests to the local FastAPI server:

```text
HTML/JavaScript
      ↓
http://127.0.0.1:8000
      ↓
FastAPI
      ↓
MongoDB
```

The HTML page by itself cannot access the database. The FastAPI server must be running on the computer for the frontend requests to work.

## Why the Backend Does Not Run Directly on GitHub

GitHub is used to store and display the source code. It does **not automatically run your FastAPI server or your local MongoDB database**.

Therefore, after someone opens the repository on GitHub:

- They can view the Python backend code.
- They can view and run the HTML page.
- The FastAPI backend needs to be started locally.
- MongoDB also needs to be running locally.

To run the complete project, clone the repository, install `requirements.txt`, start MongoDB, and run Uvicorn as shown above.

## Learning Purpose

This project was created as a backend learning/internship portfolio project to practice:

- FastAPI
- REST APIs
- CRUD operations
- MongoDB
- Password hashing
- Authentication
- JWT authorization
- Connecting a simple frontend to a backend API

## Author

Faheem Khan

GitHub:
https://github.com/faheemkhan998866
