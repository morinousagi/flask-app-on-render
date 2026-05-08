from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Define URLs
    links = {
        "rag": "https://huggingface.co/spaces/morinousagi/multiagent-rag-ai-governance",
        "intel": "https://huggingface.co/spaces/morinousagi/nlp-intelligence-analyzer",
        "chatbot": "https://web-chat.global.assistant.watson.cloud.ibm.com/preview.html?region=jp-tok&integrationID=78ea9a0d-0044-4ebe-b6b2-7a8584e8a080&serviceInstanceID=5b98a954-462a-4f7c-b268-f13bf625c0bd",
        "vit": "https://huggingface.co/spaces/morinousagi/pytorch-vit-defect-detect"
    }
    return render_template('index.html', links=links)

if __name__ == '__main__':
    app.run(debug=True)