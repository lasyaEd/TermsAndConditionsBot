# api.py
from flask import Flask, request, jsonify
from retrieval import retrieve
from simplification import simplify_text

app = Flask(__name__)

@app.route('/rag', methods=['POST'])
def rag():
    # ... (API logic)
    return jsonify({'simplified_terms': results})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)