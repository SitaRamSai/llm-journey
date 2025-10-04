from flask import Flask, render_template, request, jsonify
from transformers import AutoTokenizer

app = Flask(__name__)

# Load a small, pre-trained tokenizer
# We'll use 'bert-base-uncased' as a common, accessible tokenizer for demonstration
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

@app.route('/')
def index():
    # This will serve our main HTML file
    return render_template('index.html')

@app.route('/tokenize', methods=['POST'])
def tokenize_text():
    data = request.json
    text = data.get('text', '')
    
    if not text:
        return jsonify({"error": "No text provided"}), 400

    # Perform tokenization
    tokens = tokenizer.tokenize(text)
    token_ids = tokenizer.convert_tokens_to_ids(tokens)

    # Create a list of dictionaries for better display in frontend
    token_data = []
    for i, token in enumerate(tokens):
        token_data.append({
            "token": token,
            "id": token_ids[i]
        })

    return jsonify({"original_text": text, "tokens": token_data})

if __name__ == '__main__':
    app.run(debug=True) # debug=True allows for automatic reloading on code changes