# Blog Application

A simple blog application with a Flask backend and HTML/CSS/JavaScript frontend.

## Project Structure
```
blog-app/
├── backend/
│   ├── app.py
│   └── requirements.txt
└── frontend/
    ├── index.html
    └── style.css
```

## Setup and Installation

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the Flask server:
```bash
python app.py
```

The backend server will start at `http://localhost:5000`

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. You can serve the frontend using any static file server. For example, using Python's built-in server:
```bash
python -m http.server 8000
```

The frontend will be available at `http://localhost:8000`

## Features

- Create new blog posts
- View all posts
- Delete posts
- Responsive design
- SQLite database for data persistence

## API Endpoints

- GET `/api/posts` - Get all posts
- GET `/api/posts/<id>` - Get a specific post
- POST `/api/posts` - Create a new post
- PUT `/api/posts/<id>` - Update a post
- DELETE `/api/posts/<id>` - Delete a post

## Technologies Used

- Backend:
  - Flask
  - Flask-SQLAlchemy
  - Flask-CORS
  - SQLite

- Frontend:
  - HTML
  - CSS
  - JavaScript (Vanilla)
