from flask import Flask

application = Flask(__name__)

@application.route("/")
def index():
    return "Trabalho FIAP Cloud Computing!"

@application.route("/hello")
def hello():
    return "Olá Mundo!"


if __name__ == "__main__":
    application.run(port=5000, debug=True)
