from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulated data
class Event:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def to_dict(self):
        return {"id": self.id, "title": self.title}

# In-memory "database"
events = [
    Event(1, "Tech Meetup"),
    Event(2, "Python Workshop")
]

# Return the matching event so each route can keep its own work focused.
def find_event(event_id):
    return next((event for event in events if event.id == event_id), None)


# Create a new event from JSON input.
@app.route("/events", methods=["POST"])
def create_event():
    data = request.get_json(silent=True)
    title = data.get("title") if isinstance(data, dict) else None

    if not isinstance(title, str) or not title.strip():
        return jsonify({"error": "A non-empty 'title' field is required."}), 400

    # Generate an ID that remains unique even if an event was deleted.
    next_id = max((event.id for event in events), default=0) + 1
    event = Event(next_id, title.strip())
    events.append(event)
    return jsonify(event.to_dict()), 201


# Update the title of an existing event.
@app.route("/events/<int:event_id>", methods=["PATCH"])
def update_event(event_id):
    event = find_event(event_id)
    if event is None:
        return jsonify({"error": f"Event {event_id} was not found."}), 404

    data = request.get_json(silent=True)
    title = data.get("title") if isinstance(data, dict) else None
    if not isinstance(title, str) or not title.strip():
        return jsonify({"error": "A non-empty 'title' field is required."}), 400

    event.title = title.strip()
    return jsonify(event.to_dict()), 200


# Remove an event from the list.
@app.route("/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):
    event = find_event(event_id)
    if event is None:
        return jsonify({"error": f"Event {event_id} was not found."}), 404

    events.remove(event)
    # A 204 response must not contain a response body.
    return "", 204

if __name__ == "__main__":
    app.run(debug=True)
