from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("ready.html", url=None)

@app.route("/add", methods=['POST'])
def execute_parse():
    pass


if __name__ == "__main__":
    app.run(debug=True)
