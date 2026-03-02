# Flask Todo App

A simple task management web application built with Flask and MySQL.

## Features

- View all tasks
- Create new tasks
- Delete tasks
- Custom 404 and 500 error pages

## Prerequisites

- Python 3.8+
- MySQL server running locally or remotely

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd flask-todo
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # Linux/macOS
venv\Scripts\activate           # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
SECRET_KEY=your-secret-key-here
DB_HOST=localhost
DB_NAME=your_database_name
DB_USER=your_mysql_username
DB_PASSWORD=your_mysql_password
```

> **Note:** Make sure the database specified in `DB_NAME` already exists in your MySQL server before proceeding.

### 5. Create the database table

```bash
python create_table.py
```

This will create the `tasks` table in your configured database.

### 6. Run the application

```bash
flask run
```

Or alternatively:

```bash
python app.py
```

The app will be available at `http://127.0.0.1:5000`.

## Project Structure

```
flask-todo/
├── app.py              # Application entry point and Flask app factory
├── db.py               # Database connection helper
├── create_table.py     # Script to initialize the database table
├── requirements.txt    # Python dependencies
├── .env                # Environment variables (not committed to version control)
├── tasks/
│   ├── __init__.py
│   └── routes.py       # Task-related routes (list, create, delete)
└── templates/
    ├── base.html        # Base template
    ├── tasks.html       # Tasks list page
    └── error.html       # Error page template
```

## API Routes

| Method | Route | Description |
|--------|-------|-------------|
| GET | `/tasks` | List all tasks |
| POST | `/tasks/create` | Create a new task |
| POST | `/tasks/<id>/delete` | Delete a task by ID |

## Dependencies

| Package | Version |
|---------|---------|
| Flask | 3.1.3 |
| mysql-connector-python | 9.6.0 |
| python-dotenv | 1.2.1 |
| Werkzeug | 3.1.6 |
| Jinja2 | 3.1.6 |
