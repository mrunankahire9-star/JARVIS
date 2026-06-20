from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

chat_history = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot():

    data = request.get_json()

    user_message = data["message"].lower()

    # AI RESPONSES

    if "hello" in user_message:
        reply = "Hello Boss 👋"

    elif "python" in user_message:
        reply = "Python is a powerful programming language."

    elif "your name" in user_message:
        reply = "I am JARVIS 🤖"

    elif "bye" in user_message:
        reply = "Goodbye Boss 🚀"

    else:
        reply = "I am still learning 🚀"

    # SAVE CHAT

    chat_history.append({
        "user": user_message,
        "bot": reply
    })

    return jsonify({
        "reply": reply,
        "history": chat_history
    })

if __name__ == "__main__":
    app.run(debug=True)