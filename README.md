# Module Lab: Building Full CRUD RESTful APIs with Flask

## Learning Goals

- Implement RESTful API endpoints using Flask.
- Handle HTTP POST, PATCH, and DELETE methods to manage resource data.
- Accept and process JSON input using `request.get_json()`.
- Simulate persistent data using in-memory Python objects.
- Follow RESTful route conventions and return structured JSON responses.

## Introduction

In this lab, you will build a **Full CRUD API** to manage a list of events. The API will allow users to:

- Create new events using `POST`
- Update existing events using `PATCH`
- Delete events using `DELETE`

You’ll simulate database-like behavior with in-memory Python class objects and respond to all client requests with properly formatted JSON and appropriate status codes.

This lab reinforces essential backend development skills including route design, data mutation, error handling, and RESTful conventions.

## API Routes

The Event Management API stores events in memory while the server is running. Each
event has an integer `id` and a non-empty `title`. All successful resource
responses and errors are JSON, except for the empty `204 No Content` delete
response.

| Method | Route | Description | Success response |
| --- | --- | --- | --- |
| POST | `/events` | Create an event | `201 Created` |
| PATCH | `/events/<id>` | Change an event title | `200 OK` |
| DELETE | `/events/<id>` | Remove an event | `204 No Content` |

### Examples

Create an event:

```bash
curl -X POST http://localhost:5000/events \
  -H "Content-Type: application/json" \
  -d '{"title":"Hackathon"}'
```

Response (`201 Created`):

```json
{"id": 3, "title": "Hackathon"}
```

Update that event:

```bash
curl -X PATCH http://localhost:5000/events/3 \
  -H "Content-Type: application/json" \
  -d '{"title":"Hackathon 2025"}'
```

Response (`200 OK`):

```json
{"id": 3, "title": "Hackathon 2025"}
```

Delete an event:

```bash
curl -i -X DELETE http://localhost:5000/events/2
```

The delete request returns `204 No Content`. Missing events return `404` with an
error message; missing or invalid titles return `400` with an error message.

## Setup Instructions

### Fork and Clone the Repository

1. Go to the provided GitHub repository link.
2. Fork the repository to your GitHub account.
3. Clone the forked repository to your local machine:

```bash
git clone <repo-url>
cd course-8-module-5-flask-full-crud-api-lab
```

### Install Dependencies

Ensure Python is installed:

```bash
python --version
```

Install Flask and dependencies using pipenv:

```bash
pipenv install
pipenv shell
```

Or with pip:

```bash
pip install flask
```

## Tasks

### Task 1: Define the Problem

You’re building a basic event management API. It should:

- Accept event creation via `POST /events`
- Allow updating event titles via `PATCH /events/<id>`
- Delete events using `DELETE /events/<id>`
- Respond with structured JSON and appropriate HTTP status codes

---

### Task 2: Determine the Design

The Flask API should be structured as follows:

- Use `@app.route()` with correct HTTP method decorators
- Accept input using `request.get_json()`
- Represent data using a custom `Event` class
- Store events in an in-memory list
- Use `jsonify()` for consistent JSON responses

---

### Task 3: Develop the Code

Create `app.py` and start with the following structure:

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Event class
class Event:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def to_dict(self):
        return {"id": self.id, "title": self.title}

# In-memory data store
events = [
    Event(1, "Tech Meetup"),
    Event(2, "Python Workshop")
]

# TODO: POST /events - Create a new event from JSON input
# TODO: PATCH /events/<id> - Update the title of an event
# TODO: DELETE /events/<id> - Remove an event from the list

if __name__ == "__main__":
    app.run(debug=True)
```

---

### Task 4: Test the API

Start the Flask development server:

```bash
python app.py
```

Test your endpoints using Postman or curl:

- `POST http://localhost:5000/events`
  - Body: `{ "title": "Hackathon" }`
- `PATCH http://localhost:5000/events/1`
  - Body: `{ "title": "Hackathon 2025" }`
- `DELETE http://localhost:5000/events/2`

---

## Best Practices

- Use RESTful nouns in routes (e.g., `/events`)
- Validate incoming JSON and handle missing keys gracefully
- Use helper functions to reduce code repetition
- Return:
  - `201 Created` for successful POST
  - `200 OK` or `204 No Content` for PATCH and DELETE
  - `404 Not Found` if a resource doesn't exist
- Include inline comments to explain logic

---

## Considerations

**1. Input Validation**
- Ensure the `title` field is provided.
- Return a `400 Bad Request` if missing.

**2. Event Not Found**
- Return `404 Not Found` with a clear message when the event ID doesn't exist.

**3. Reusable Logic**
- Consider writing a helper function to look up events by ID.

**4. Scalability**
- While using a single file works here, separate concerns into modules as your API grows.

---

## Conclusion

After completing this lab, you will:

✅ Know how to handle incoming JSON with Flask  
✅ Build routes that implement full CRUD behavior  
✅ Simulate persistent resource changes in memory  
✅ Return proper HTTP status codes and structured responses  

This is a critical step in your backend developer journey. Next up: persistent databases!
