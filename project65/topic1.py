from flask import Flask

app=Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/Bye")
def bye():
    return "Bye"

#Default input is string,you can convert it like below
@app.route("/username/<name>/<int:number>")
def greet(name,number):
    return f"Hello there {name}!,you are {number} years old"


# Debug mode is so much useful 
if __name__=="__main__":
    app.run(debug=True)  # If you open then you dont have to restart your code again and again becasue debug mode is doing that auotmaticly

