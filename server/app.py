from flask import Flask, request, jsonify
from political_alignment.classify_alignment import classify

app = Flask(__name__)


@app.route("/analyze", methods=["POST"])
def analyze():
    text = request.get_json()["text"]
    return jsonify({"alignment": classify(text)})


if __name__ == "__main__":
    # Listens on http://localhost:5001
    app.run(host="127.0.0.1", port=5001, debug=True)
