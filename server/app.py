from flask import Flask, request, jsonify
from political_alignment.classify_alignment import classify_alignment
from neutral_summarizer.generate_summary import generate_neutral_summary
from bias_calculator.bias_calculator import calculate_bias

app = Flask(__name__)


@app.route("/analyze", methods=["POST"])
def analyze():
    text = request.get_json()["text"]
    neutral_summary = generate_neutral_summary(text)
    
    return jsonify({
        "alignment": classify_alignment(text),
        "summary": neutral_summary,
        "bias": calculate_bias(text, neutral_summary),
        "raw": text,
    })


if __name__ == "__main__":
    # Listens on http://localhost:5001
    app.run(host="127.0.0.1", port=5001, debug=True)
