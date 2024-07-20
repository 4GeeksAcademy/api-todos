from flask import Flask


app = Flask(__name__)


@app.route("/health-check", methods=["GET"])
def health_check():
    return "ok"


@app.route("/", methods=["GET"])
def hello_world():
    return "<h1>Hola ¿qué tal? Byeee</h1>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)