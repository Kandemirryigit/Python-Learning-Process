from flask import Flask

app=Flask(__name__)

@app.route("/")  # / means home page  www.google.com/ means google's home page 
def home():
    return "Hello, World!"

if __name__=="__main__":
    app.run()