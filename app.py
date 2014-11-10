from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World! Test Deploy"

@app.route("/test/")
def test():
    return "TEST ASS"

if __name__ == "__main__":
    app.run()
