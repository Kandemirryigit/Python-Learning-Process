from flask import Flask

app=Flask(__name__)

def make_bold(function):
    def wrapper():
        return "<b>"+function()+"</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return "<em>"+function()+"</em>"
    return wrapper

def make_underline(function):
    def wrapper():
        return "<u>"+function()+"</u>"
    return wrapper
    


@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/Bye")
@make_bold
@make_emphasis
@make_underline
def bye():
    return "Bye"


#Default input is string,you can convert it like below
@make_emphasis
@app.route("/username/<name>/<int:number>")
def greet(name,number):
    return f"Hello there {name}!,you are {number} years old"


# Debug mode is so much useful 
if __name__=="__main__":
    app.run(debug=True)  # If you open then you dont have to restart your code again and again becasue debug mode is doing that auotmaticly

