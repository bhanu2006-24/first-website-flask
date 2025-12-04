# Flask Application

A full-featured Flask application with User Authentication, Blogging capabilities, and a Todo List manager.

## Features

- **User Authentication**: Secure login and registration system.
- **Blog System**: Create, read, and manage blog posts.
- **Todo List**: Manage your daily tasks with a simple todo list.
- **Database Integration**: Uses SQLAlchemy for efficient data management.

## Getting Started

### Prerequisites

- Python 3.x
- pip (Python package manager)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd first-flask-app/First\ App
    ```

2.  **Create a virtual environment (optional but recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the application:**
    ```bash
    python main.py
    ```
    The app will be available at `http://localhost:5555`.

## Deployment on Vercel

This application is configured for easy deployment on Vercel.

1.  **Install Vercel CLI:**
    ```bash
    npm install -g vercel
    ```

2.  **Deploy:**
    Run the following command from the `First App` directory:
    ```bash
    vercel
    ```

### Environment Variables

For production, you should configure the following environment variables in your Vercel project settings:

- `SECRET_KEY`: A secret key for session security.
- `DATABASE_URL`: Connection string for your production database (e.g., PostgreSQL).
- `DEBUG`: Set to `False` for production.

## Technologies Used

- **Flask**: Micro web framework for Python.
- **Flask-SQLAlchemy**: ORM for database interactions.
- **Flask-Login**: User session management.
