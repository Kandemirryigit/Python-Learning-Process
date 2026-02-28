from flask import Flask
import random

app=Flask(__name__)

random_number=random.randint(0,9)

def make_bold(function):
    def wrapper():
        return "<b>"+function()+"</b>"
    return wrapper


@app.route("/")
@make_bold
def hello():
    return "<h1>Guess a number between 0 and 9</h1>" \
    "<img src='https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExazZuemJkeWkxcTZoNzczMm8xd2NtYmNpNmIzeWFjaWNnYmVpZjhiNCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7aCSPqXE5C6T8tBC/giphy.gif' >"


@app.route("/<int:number>")
def num(number):
    if random_number>number:
        return "<h1 style= 'color: purple'>your guess is low</h1>" \
        "<img src='https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExMmUxMTFtemJxdmtibWQzZTE3bnNtdXdyZ3AwcWIxeWtmaWMyOHNidSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/vMbC8xqhIf9ny/giphy.gif'>"
    elif random_number==number:
        return "<h1 style= 'color: green'>You found me</h1>" \
        "<img src='https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExMTh0MjM5czZhemx2d25jMXFudHJ5ZWxvdWV6OXU5OTNmcjY2ZWxmbiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Puc4FZWExJc0E/giphy.gif' width=200 height=200>"
    else:
        return "<h1 style= 'color: red'>your guess is high</h1>" \
        "<img src='https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExdjkzMmFydWQyejRwaHp6dHNuZTlueWg2cTg3N3FtZGUzM3lyZ2NlMCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7btPitD723wPmVsk/giphy.gif'>"
    




# Debug mode is so much useful 
if __name__=="__main__":
    app.run(debug=True)  # If you open then you dont have to restart your code again and again becasue debug mode is doing that auotmaticly

