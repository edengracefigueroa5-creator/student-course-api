# Student Course API

A small read-only REST API built with **Python and Flask** for the
System Integration and Architecture course, Lesson 3.

It serves five fictional courses from an in-memory Python list. There is no
database, no authentication, and no way to create, update or delete data -
every endpoint only reads.

## Files

    app.py             the Flask application (entry point)
    requirements.txt   Python dependencies
    README.md          this file

## Requirements

- Python 3.9 or newer
- pip

## Run it locally

1. Create a folder, open a terminal in it, and create a virtual environment:

       python -m venv venv

   Activate it:

       venv\Scripts\activate          (Windows)
       source venv/bin/activate      (macOS / Linux)

2. Install the dependencies:

       pip install -r requirements.txt

3. Start the server:

       python app.py

4. Open http://127.0.0.1:5000/api/health in your browser.

## Endpoints

| Method | Path             | Status | What it returns                     |
|--------|------------------|--------|-------------------------------------|
| GET    | /                | 200    | A short index of available endpoints|
| GET    | /api/health      | 200    | Confirms the API is running         |
| GET    | /api/courses     | 200    | All five fictional courses          |
| GET    | /api/courses/1   | 200    | The single course with id 1         |
| GET    | /api/courses/9999| 404    | A JSON error message                |

Every course object has an integer id, a code, a name and a description.

Test one endpoint from the terminal:

    curl http://127.0.0.1:5000/api/courses/1

## Deploy to Render

1. Push this folder to a GitHub repository.
2. In Render, choose **New > Web Service** and connect that repository.
3. Use these settings:

   - **Environment:** Python 3
   - **Build Command:** pip install -r requirements.txt
   - **Start Command:** gunicorn app:app --bind 0.0.0.0:$PORT
   - **Health Check Path:** /api/health

4. Do not set PORT yourself. Render injects it, app.py reads it, and the
   start command binds to it.
5. Deploy, then open https://your-service.onrender.com/api/health

## Notes for the demo

- CORS is open to every origin so a classmate's page can call the API from
  the browser. That is fine for classroom work, not for production.
- All course data is fictional and lives inside app.py.
- The API is read-only on purpose: POST, PUT and DELETE return 405.
