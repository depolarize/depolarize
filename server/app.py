# server/app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    text = data["text"]
    return jsonify(
        {
            "summary": test(text),
        }
    )


def test(text):
    return text


if __name__ == "__main__":
    # Listens on http://localhost:5001
    app.run(host='127.0.0.1', port=5001, debug=True)
