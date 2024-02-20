from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__, static_folder= "templates")
CORS(app)
# Load Rasa model

@app.route("/signin")
def signin():
    pass

@app.route("/webhook", methods=["POST"])
async def webhook():
    data = request.get_json()
    user_message = data["message"]

    # Get Rasa response
    if 'hi' in user_message:
        bot_reply = "Hi Dear"
    else:
        bot_reply = "love u darling"

    # Extract the bot's reply

    return jsonify({"message": bot_reply})

@app.route("/home", methods=["GET"])
def home():
    return render_template('chatui.html')

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
