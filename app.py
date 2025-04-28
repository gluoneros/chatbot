from flask import Flask, request, render_template
from chatbot import get_response

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['message']
    response = get_response(user_input)
    return {'response': response}

if __name__ == '__main__':
    app.run(debug=True)