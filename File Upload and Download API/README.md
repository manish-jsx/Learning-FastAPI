
# File Upload and Download API using FastAPI

This API allows users to upload and download files securely. It includes features such as file type validation during upload and authentication/authorization for file downloads.

## Features

- **File Upload Endpoint**: Users can upload files to the server. The API performs validation to ensure only specific file types are accepted.

- **File Download Endpoint**: Authenticated and authorized users can download files securely.

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn

## Installation

1. Install dependencies:

    ```bash
    pip install fastapi uvicorn
    ```

2. Run the API:

    ```bash
    uvicorn main:app --reload
    ```

By default, the API runs on [http://127.0.0.1:8000](http://127.0.0.1:8000).

## API Endpoints

### Upload File

- **Endpoint**: `/upload/`
- **Method**: POST
- **Description**: Upload a file with validation for specific file types.

Example:

```bash
curl -X POST "http://127.0.0.1:8000/upload/" -H "accept: application/json" -H "Content-Type: multipart/form-data" -F "file=@/path/to/file.jpg"
```

### Download File

- **Endpoint**: `/download/{file_name}`
- **Method**: GET
- **Description**: Download a file securely with authentication and authorization.

Example:

```bash
curl -X GET "http://127.0.0.1:8000/download/{file_name}" -H "accept: application/json" -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

Replace `{file_name}` with the actual file name, and provide a valid access token for authorization.

## Authentication and Authorization

The API uses OAuth2 for authentication. The token can be obtained through the `/token` endpoint.

Authorization is implemented through the `check_user_permissions` function. Adjust this function based on your specific authorization requirements.

## Customize

Feel free to customize the API to fit your specific needs. You may want to implement a proper user authentication system, secure file storage, and enhance error handling.

