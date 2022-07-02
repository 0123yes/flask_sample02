from flask import Flask


app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello,world"


@app.route("/menber")
def hello_menber():
    return "Hello,Menber"


@app.route("/owner")
def hello_owner():
    return "Hello Owner"


if __name__ == "__main__":
    app.run()
