import random

from flask import Flask

app = Flask(__name__)
high_gif_link = "https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"
low_gif_link = "https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"
correct_gif_link = "https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"


def home_decorator(function):
    def wrapper():
        html = f'<h1>{function()}</h1>'
        html += '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'
        return html
    return wrapper


def high_low_decorator(function):
    def wrapper_fun(*args, **kwargs):
        n = kwargs.get('num')
        msg = function(n)
        if n < random_number:
            return f'<h1 style="color:blue;">{msg}</h1><img src={low_gif_link}>'
        elif n > random_number:
            return f'<h1 style="color:red;">{msg}</h1><img src={high_gif_link}>'
        else:
            return f'<h1 style="color:green;">{msg}</h1><img src={correct_gif_link}>'
    return wrapper_fun


@app.route("/")
@home_decorator
def home():
    global random_number
    random_number = random.randint(0, 9)
    return "Guess a number between 0 and 9"


@app.route("/<int:num>")
@high_low_decorator
def higher_lower(num):
    if num < random_number:
        return "Too low, try again!"
    elif num > random_number:
        return "Too high, try again!"
    else:
        return "You found me!"


if __name__ == "__main__":
    app.run(debug=True)
