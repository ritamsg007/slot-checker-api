from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample slot data
available_slots = {
    "2025-06-27": ["9", "10", "11", "14"],
    "2025-06-28": ["10", "11", "15"]
}

# Home route to confirm the app is running
@app.route('/', methods=['GET'])
def index():
    return "✅ Slot Checker API is up and running!"

# API endpoint to check availability
@app.route('/check_slots', methods=['POST'])
def check_slots():
    data = request.get_json()
    print(f"[INFO] Incoming request JSON: {data}")  # Log input

    date = data.get("date")
    time = data.get("time")

    if not date or not time:
        error_msg = {"error": "Missing date or time"}
        print(f"[ERROR] {error_msg}")  # Log error
        return jsonify(error_msg), 400

    available = time in available_slots.get(date, [])
    response = {"available": available}
    print(f"[INFO] Response sent: {response}")  # Log output
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
