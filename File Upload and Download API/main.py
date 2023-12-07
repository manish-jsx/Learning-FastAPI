from fastapi import FastAPI, File, UploadFile, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from fastapi.responses import FileResponse
from typing import List

app = FastAPI()

# OAuth2PasswordBearer is used for handling authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# Function to authenticate users based on the provided token
def get_current_user(token: str = Depends(oauth2_scheme)):
    # Here you would perform actual user authentication based on the token
    # For simplicity, we'll just return a hardcoded user for demonstration purposes
    fake_user = {"username": "fakeuser", "token": token}
    return fake_user


# Function to check if the user has the necessary permissions
def check_user_permissions(current_user: dict = Depends(get_current_user)):
    # Here you would perform actual authorization checks based on the user
    # For simplicity, we'll assume all users have permission
    return True


# Endpoint to upload files with validation
@app.post("/upload/")
async def upload_file(file: UploadFile = File(..., description="The file to upload")):
    # Check if the file type is allowed (you can modify the allowed_types list)
    allowed_types = ["image/jpeg", "image/png", "application/pdf"]
    if file.content_type not in allowed_types:
        raise HTTPException(status_code=400, detail="Invalid file type")

    # Process the uploaded file (you can save it to disk, database, etc.)
    # For now, we'll just return the file details
    return {"filename": file.filename, "content_type": file.content_type}


# Endpoint to download files with authentication and authorization
@app.get("/download/{file_name}", response_class=FileResponse)
async def download_file(
    file_name: str,
    current_user: dict = Depends(get_current_user),
    has_permissions: bool = Depends(check_user_permissions),
):
    # Check if the user has the necessary permissions
    if not has_permissions:
        raise HTTPException(status_code=403, detail="Permission denied")

    # Here you would retrieve the file from storage (e.g., database or filesystem)
    # For simplicity, we'll just assume the file exists in the current directory
    file_path = file_name
    return FileResponse(file_path, filename=file_name)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
