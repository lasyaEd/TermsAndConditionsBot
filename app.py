import modal
import json
from flask import Flask, request
from transformers import pipeline

# Initialize the Flask app
flask_app = Flask(__name__)

# Load your model globally
model = pipeline("text-generation", model="gpt2")  # Replace with your model

# Define the API endpoint
@flask_app.route("/api/generate", methods=["POST"])
def api_endpoint():
    data = request.get_json()
    prompt = data.get("prompt", "")
    response = model(prompt, max_length=50)
    return json.dumps({"response": response[0]['generated_text']})

# Create a Modal app to deploy the Flask app
modal_app = modal.App("your-app-name")

@modal_app.function()
def run_flask_app():
    # Run the Flask app
    flask_app.run(host="0.0.0.0", port=8080)

if __name__ == "__main__":
    modal_app.deploy()
