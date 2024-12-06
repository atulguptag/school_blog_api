# School Blog API

A RESTful API for managing a school blog, built with FastAPI and MongoDB using the Motor driver. This API allows creating, reading, updating, and deleting blog posts.

## Features

- **Create Blog Posts**: Add new posts to the blog.
- **Read Blog Posts**: Retrieve single or multiple blog posts.
- **Update Blog Posts**: Modify existing posts.
- **Delete Blog Posts**: Remove posts from the blog.

## Prerequisites

Before setting up this project, ensure you have the following installed:

- Python 3.7+
- MongoDB

## Setup Instructions

### Clone the Repository

```bash
git clone https://github.com/atulguptag/school_blog_api
cd school_blog_api
```

### Create a Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment:

- On Windows:

  ```bash
  .\venv\Scripts\activate
  ```

- On macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

### Install Dependencies

Install the required Python packages:

```bash
pip install fastapi[all] motor pymongo
```

### Setup MongoDB

- Ensure MongoDB is running locally. You can start MongoDB with the following command:

  ```bash
  mongod
  ```

### Project Structure

```
school_blog_api/
│
├── main.py           # Main application code
└── models.py         # Pydantic models
```

### models.py

Define Pydantic models for validating the data:

```python
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime, timezone

class BlogPost(BaseModel):
    title: str
    content: str
    published_at: Optional[datetime] = Field(default_factory=lambda: datetime.now(timezone.utc))
    tags: List[str] = []

class BlogPostInDB(BlogPost):
    id: Optional[str] = None
```

### Running the Application

Run the FastAPI server using Uvicorn:

```bash
uvicorn main:app --reload
```

The API documentation with Swagger UI is accessible at `http://127.0.0.1:8000/docs`.

## API Endpoints

- **Create a Post**: `POST /posts/`
- **Get a Post by ID**: `GET /posts/{post_id}`
- **List all Posts**: `GET /posts/`
- **Update a Post by ID**: `PUT /posts/{post_id}`
- **Delete a Post by ID**: `DELETE /posts/{post_id}`

### Example Usage

Using `curl` or similar tools to interact with the API:

- **Create a Post**:

  ```bash
  curl -X POST "http://127.0.0.1:8000/posts/" -H "Content-Type: application/json" -d '{"title": "New Post", "content": "This is a new post.", "tags": ["intro", "first"]}'
  ```

- **Get a Post by ID**:

  ```bash
  curl "http://127.0.0.1:8000/posts/{post_id}"
  ```

- **List All Posts**:

  ```bash
  curl "http://127.0.0.1:8000/posts/"
  ```

- **Update a Post**:

  ```bash
  curl -X PUT "http://127.0.0.1:8000/posts/{post_id}" -H "Content-Type: application/json" -d '{"title": "Updated Post", "content": "Updated content."}'
  ```

- **Delete a Post**:
  ```bash
  curl -X DELETE "http://127.0.0.1:8000/posts/{post_id}"
  ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
