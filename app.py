from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Docker! I am running on Flask. This is crazy !!!!!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)