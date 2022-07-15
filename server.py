from flask import Flask

app = Flask(__name__)


def home_decorator(function):
    def wrapper():
        html = f'<h1>{function()}</h1>'
        html += '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'
        return html
    return wrapper


@app.route("/")
@home_decorator
def home():
    return "Guess a number between 0 and 9"


if __name__ == "__main__":
    app.run(debug=True)
