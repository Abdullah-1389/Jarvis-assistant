from flask import Flask, render_template, request, jsonify
from jarvis_core import process_command

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    
    if not user_message.strip():
        return jsonify({"reply": "I didn't hear anything. Try again."})

    reply = process_command(user_message)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
