from flask import Flask, request, jsonify
from agent import analyze_text

app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze():
    text = request.json.get("text")
    result = analyze_text(text)
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)