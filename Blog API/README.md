
# FastAPI Blog API

This is a simple blogging API built with FastAPI, providing endpoints for creating, updating, and retrieving blog posts. It includes authentication for blog post creation/editing, pagination, filtering options, and user comments functionality.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Authentication](#authentication)
- [Pagination and Filtering](#pagination-and-filtering)
- [User Comments](#user-comments)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

- Python 3.7+
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Passlib](https://passlib.readthedocs.io/en/stable/)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/fastapi-blog-api.git
   ```

2. Navigate to the project directory:

   ```bash
   cd fastapi-blog-api
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:

   ```bash
   uvicorn main:app --reload
   ```

## Usage

Once the application is running, you can access the FastAPI documentation at `http://127.0.0.1:8000/docs` to explore and test the API.

## API Endpoints

- **POST /token:** Get an access token by providing valid credentials.
- **POST /users/:** Create a new user.
- **GET /users/me:** Get information about the current user.
- **GET /blogs/:** Retrieve a list of blog posts with pagination and filtering options.
- **POST /blogs/:** Create a new blog post.
- **POST /blogs/{blog_id}/comments/:** Add a comment to a specific blog post.

For more detailed information on each endpoint, refer to the [FastAPI documentation](https://fastapi.tiangolo.com/).

## Authentication

Authentication is required for creating and updating blog posts. Obtain an access token by making a `POST` request to `/token` with valid credentials.

## Pagination and Filtering

The `/blogs/` endpoint supports pagination with the `skip` and `limit` query parameters. You can use these parameters to control the number of blog posts retrieved.

## User Comments

Users can add comments to specific blog posts by making a `POST` request to `/blogs/{blog_id}/comments/`.

## Contributing

If you would like to contribute to this project, please follow the [Contributing Guidelines](CONTRIBUTING.md).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
