from flask import Flask
import sentimentAnalysis

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/news')
def news():
    return {"status": "OK", "content": sentimentAnalysis.sentiment()}

@app.route("/Alex")
def alex():
    return "Cutie! <3 "


if __name__ == '__main__':
    app.run()
