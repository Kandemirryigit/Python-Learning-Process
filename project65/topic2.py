from flask import Flask

app=Flask(__name__)

@app.route("/")
def hello():
    return "<h1 style='text-align: center'>Hello, World!</h1>" \
            "<p>this is a cat</p>" \
            "<img src='https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExd3M4dzB6ajJycXdwd3hlOTRlNTNxc3oxcDVxZmVmbGJrcTF5d3ZoayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3oriO0OEd9QIDdllqo/giphy.gif' width=200 height=200>"

@app.route("/Bye")
def bye():
    return "<h2>Bye</h2>"

#Default input is string,you can convert it like below
@app.route("/username/<name>/<int:number>")
def greet(name,number):
    return f"Hello there {name}!,you are {number} years old"


# Debug mode is so much useful 
if __name__=="__main__":
    app.run(debug=True)  # If you open then you dont have to restart your code again and again becasue debug mode is doing that auotmaticly

