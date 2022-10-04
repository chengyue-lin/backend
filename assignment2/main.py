import json
from flask import Flask, request
import emoji

app = Flask(__name__)

@app.route("/")
def homepage():
    parameter = request.args.get("emoji")
    if parameter is None:
        return "hello, World!"
    else:
        return "Hello, " + emoji.emojize(parameter) + "!"


@app.route("/all")
def all():
    f = open("emojis.txt", "r")
    lines = f.readlines()
    emojis = {}
    for line in lines:
        line = line[:-1]
        emojis[line] = emoji.emojize(line)
    return json.dumps(emojis, ensure_ascii=False)

if __name__ == "__main__":
    app.run(debug=True)