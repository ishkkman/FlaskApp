from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Flask App!_ test!!"

if __name__ == '__main__':
    app.run(debug=True)