from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from your Flask app on AWS EC2!"

if __name__ == '__main__':
    app.run(debug=True)