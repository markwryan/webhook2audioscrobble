from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    print(request.method)
    print(request.json)
    return request.json

if __name__ == '__main__':
    app.run()