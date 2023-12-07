from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from typing import List

app = FastAPI()

# Secret key to sign JWT
SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"

# Define OAuth2 password bearer for authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Sample User model (Replace it with your User model)
class User:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

# Sample database (Replace it with your database)
fake_users_db = {
    "testuser": User(username="testuser", password="password123")
}

# Function to create JWT token
def create_jwt_token(data: dict):
    to_encode = data.copy()
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Function to get user from the database
def get_user(db, username: str):
    if username in db:
        return db[username]
    return None

# Dependency to get the current user using JWT token
def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Invalid credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = {"sub": username}
    except JWTError:
        raise credentials_exception
    return token_data

# Sample task model (Replace it with your Task model)
class Task:
    def __init__(self, title: str, description: str):
        self.title = title
        self.description = description

# Sample database for tasks (Replace it with your database)
tasks_db = []

# Endpoint to create a new task
@app.post("/tasks/", response_model=Task)
async def create_task(task: Task, current_user: User = Depends(get_current_user)):
    tasks_db.append(task)
    return task

# Endpoint to get all tasks
@app.get("/tasks/", response_model=List[Task])
async def get_tasks(current_user: User = Depends(get_current_user)):
    return tasks_db

# Endpoint to update a task by ID
@app.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: int, task: Task, current_user: User = Depends(get_current_user)):
    if task_id < 0 or task_id >= len(tasks_db):
        raise HTTPException(status_code=404, detail="Task not found")
    
    tasks_db[task_id] = task
    return task

# Endpoint to delete a task by ID
@app.delete("/tasks/{task_id}", response_model=Task)
async def delete_task(task_id: int, current_user: User = Depends(get_current_user)):
    if task_id < 0 or task_id >= len(tasks_db):
        raise HTTPException(status_code=404, detail="Task not found")
    
    deleted_task = tasks_db.pop(task_id)
    return deleted_task
