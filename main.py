from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Mount static directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configure Jinja2
templates = Jinja2Templates(directory="templates")

# Temporary database
posts = [
    {
        "id": 1,
        "author": "Kasra",
        "title": "Learning FastAPI",
        "content": "FastAPI is a modern Python framework for building APIs.",
        "date": "November 1, 2026"
    },
    {
        "id": 2,
        "author": "Alex",
        "title": "Why Python?",
        "content": "Python is a versatile programming language.",
        "date": "November 3, 2026"
    },
    {
        "id": 3,
        "author": "John",
        "title": "Introduction to Linux",
        "content": "Linux is an open-source operating system.",
        "date": "November 5, 2026"
    }
]

# Home page
@app.get("/")
def home(request: Request, author: str = None):

    # TODO 1: Filter posts by author if author is provided.

    return templates.TemplateResponse(
        request,
        "home.html",
        {
            "posts": posts,
            "title": "MiniBlog",
            "selected_author": author
        }
    )

# Individual post page
@app.get("/posts/{post_id}")
def get_post(request: Request, post_id: int):

    # TODO 2: Find the post with the matching ID.
    # TODO 3: If it doesn't exist, return an appropriate 404 response.

    return templates.TemplateResponse(
        request,
        "post.html",
        {
            "post": post,
            "title": post["title"]
        }
    )

# API endpoint
@app.get("/api/posts")
def get_posts():
    return posts