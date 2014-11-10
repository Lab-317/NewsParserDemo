from flask import Flask, render_template, request
from newsParser import NewsParser

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("ready.html", url=None)

@app.route("/parse", methods=['POST'])
def execute_parse():
    parse_obj = NewsParser(request.form['newsUrl'])
    title = parse_obj.getTitle()
    content = parse_obj.getContent()
    author = parse_obj.getAuthor()
    pub_time = parse_obj.getPublishDate()
    return render_template("show_detail.html",
        title=title, content=content, author=author, pub_time=pub_time)



if __name__ == "__main__":
    app.run(debug=True)
