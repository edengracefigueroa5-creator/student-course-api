"""
Student Course API
System Integration and Architecture - Lesson 3

A small, read-only REST API that serves fictional course data.
No database. No authentication. No create, update or delete routes.

Run locally:
    pip install -r requirements.txt
    python app.py

Then open http://127.0.0.1:5000/api/health
"""

import os

from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

# CORS for the classroom demo: any web page may read this API from a browser.
CORS(app, resources={r"/api/*": {"origins": "*"}})

# ---------------------------------------------------------------------------
# Sample data - completely fictional. No real student information is used.
# ---------------------------------------------------------------------------
COURSES = [
    {
        "id": 1,
        "code": "IT 101",
        "name": "Introduction to Computing",
        "description": "Computer hardware, software and how information systems support everyday organizations.",
    },
    {
        "id": 2,
        "code": "IT 205",
        "name": "Systems Integration and Architecture",
        "description": "Designing and connecting systems: APIs, middleware, integration patterns and layered architecture.",
    },
    {
        "id": 3,
        "code": "CS 210",
        "name": "Data Structures and Algorithms",
        "description": "Lists, stacks, queues, trees and graphs, with an introduction to algorithm analysis.",
    },
    {
        "id": 4,
        "code": "IT 230",
        "name": "Database Management Systems",
        "description": "Relational modelling, SQL, normalization and the role of databases in enterprise systems.",
    },
    {
        "id": 5,
        "code": "NET 240",
        "name": "Networking and Cloud Fundamentals",
        "description": "TCP/IP, HTTP and the basics of deploying an application to a cloud platform.",
    },
]


@app.get("/api/health")
def health():
    """Confirms the API is running."""
    return jsonify({
        "status": "ok",
        "service": "Student Course API",
        "version": "1.0.0",
        "message": "The API is running.",
    }), 200


@app.get("/api/courses")
def list_courses():
    """Returns every fictional course as a JSON array."""
    return jsonify(COURSES), 200


@app.get("/api/courses/<int:course_id>")
def get_course(course_id):
    """Returns one course by its integer id."""
    course = next((item for item in COURSES if item["id"] == course_id), None)

    if course is None:
        return jsonify({
            "error": "Not Found",
            "message": f"No course exists with id {course_id}.",
            "available_ids": [item["id"] for item in COURSES],
        }), 404

    return jsonify(course), 200


@app.errorhandler(404)
def not_found(error):
    """Any unknown URL answers with JSON instead of an HTML error page."""
    return jsonify({
        "error": "Not Found",
        "message": "That resource does not exist. Try GET /api/courses.",
    }), 404


@app.errorhandler(405)
def method_not_allowed(error):
    """The API is read-only, so anything other than GET is refused."""
    return jsonify({
        "error": "Method Not Allowed",
        "message": "This API is read-only. Only GET requests are supported.",
    }), 405


if __name__ == "__main__":
    # Render provides the PORT environment variable. Locally it falls back to 5000.
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
