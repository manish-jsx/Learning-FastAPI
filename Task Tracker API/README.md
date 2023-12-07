
# Task Tracker API

This is a simple RESTful API for a task tracker application built using FastAPI. It provides endpoints for creating, updating, deleting, and retrieving tasks. The API also includes authentication using OAuth2 for secure access.

## Features

- Create, update, delete, and retrieve tasks.
- Secure access using OAuth2 authentication.

## Getting Started

### Prerequisites

- Python 3.7 or later
- [FastAPI](https://fastapi.tiangolo.com/) (`pip install fastapi`)
- [Uvicorn](https://www.uvicorn.org/) (`pip install uvicorn`)
- [HTTPie](https://httpie.io/) (optional, for testing)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/task-tracker-api.git
   ```

2. Change into the project directory:

   ```bash
   cd task-tracker-api
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Running the API

Use the following command to start the development server:

```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

### Obtaining an OAuth2 Token

To interact with the protected endpoints, you need to obtain an OAuth2 token. Use the `/token` endpoint with valid credentials (e.g., testuser/password123).

Example using HTTPie:

```bash
http --form POST http://127.0.0.1:8000/token username=testuser password=password123 grant_type=password
```

### Endpoints

- **Create Task:** `POST /tasks/`
- **Get Tasks:** `GET /tasks/`
- **Update Task:** `PUT /tasks/{task_id}`
- **Delete Task:** `DELETE /tasks/{task_id}`

## Authentication

- Include the obtained OAuth2 token in the Authorization header:

  ```
  Authorization: Bearer your_token_here
  ```

## Sample Request (HTTPie)

### Create Task

```bash
http POST http://127.0.0.1:8000/tasks/ title="Task Title" description="Task Description" Authorization:"Bearer your_token_here"
```

### Get Tasks

```bash
http http://127.0.0.1:8000/tasks/ Authorization:"Bearer your_token_here"
```

### Update Task

```bash
http PUT http://127.0.0.1:8000/tasks/{task_id} title="Updated Title" description="Updated Description" Authorization:"Bearer your_token_here"
```

### Delete Task

```bash
http DELETE http://127.0.0.1:8000/tasks/{task_id} Authorization:"Bearer your_token_here"
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
